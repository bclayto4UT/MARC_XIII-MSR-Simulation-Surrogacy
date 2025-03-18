import os
import json
import logging
from typing import Dict, Any, List, Optional, Tuple, Set

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('Phase-Specific-Data-Processor')

class PhaseSpecificDataProcessor:
    """
    Component 5: Phase-Specific Data Processor
    Generates phase-specific JSON files with phase percentages and compositions.
    
    Main functions:
    - extract_phase_data: Extracts and categorizes phases by type (salt, gas, solid)
    - extract_phase_compositions: Extracts species or cation/anion compositions
    - calculate_phase_mole_percent: Calculates phase mole percentages
    - generate_phase_json: Creates phase-specific JSON file
    """
    
    def __init__(self, condensed_report: Dict[str, Dict[str, Any]], surrogate_vector: Dict[str, Any]):
        """
        Initialize the Phase-Specific Data Processor.
        
        Args:
            condensed_report (Dict[str, Dict[str, Any]]): Condensed Thermochimica report from Component 2
            surrogate_vector (Dict[str, Any]): Surrogate vector data from Component 1
        """
        self.condensed_report = condensed_report
        self.surrogate_vector = surrogate_vector
        
        # Initialize phase data categorization
        self.phase_data = {
            "salt": {},  # MSFL phases (molten salt)
            "gas": {},   # Gas phases 
            "solid": {}  # Solid phases (pure condensed phases)
        }
        
        # Timesteps for easier iteration
        self.timesteps = sorted([int(ts) for ts in self.condensed_report.keys()])
        self.str_timesteps = [str(ts) for ts in self.timesteps]
    
    def extract_phase_data(self) -> Dict[str, Dict[str, Dict]]:
        """
        Extract and categorize data for all phases by type (salt, gas, solid).
        Based on approach from Phase_Analysis_and_Report_Gen2.
        
        Returns:
            Dict[str, Dict[str, Dict]]: Dictionary of phase data by type and timestep
        """
        logger.info("Extracting and categorizing phase data by type")
        
        result = {
            "salt": {},
            "gas": {},
            "solid": {}
        }
        
        # Initialize data structures for all timesteps
        for phase_type in result.keys():
            for timestep in self.str_timesteps:
                if timestep not in result[phase_type]:
                    result[phase_type][timestep] = {}
        
        # Process each timestep in the condensed report
        for timestep in self.str_timesteps:
            data = self.condensed_report[timestep]
            first_key = next(iter(data))
            
            # Process solution phases (can be salt, gas, or solid)
            if "solution phases" in data[first_key]:
                solution_phases = data[first_key]["solution phases"]
                for phase_name, phase_data in solution_phases.items():
                    if phase_data.get("moles", 0) <= 0:
                        continue  # Skip phases with 0 moles
                    
                    # Determine phase type based on name
                    if phase_name.startswith("MSFL"):
                        # Salt phases have MSFL prefix
                        result["salt"][timestep][phase_name] = phase_data
                    elif phase_name.lower() == "gas_ideal":
                        # Only "ideal gas" is a gas phase
                        result["gas"][timestep][phase_name] = phase_data
                    else:
                        # All other solution phases are solids
                        result["solid"][timestep][phase_name] = phase_data
            
            # Process pure condensed phases (always solids)
            if "pure condensed phases" in data[first_key]:
                pure_phases = data[first_key]["pure condensed phases"]
                for phase_name, phase_data in pure_phases.items():
                    if phase_data.get("moles", 0) <= 0:
                        continue  # Skip phases with 0 moles
                    
                    # All pure condensed phases are solids
                    result["solid"][timestep][phase_name] = phase_data
        
        # Log the results
        for phase_type, timestep_data in result.items():
            total_phases = sum(len(phases) for phases in timestep_data.values())
            logger.info(f"Extracted {total_phases} {phase_type} phases across {len(timestep_data)} timesteps")
        
        self.phase_data = result
        return result
    
    def extract_phase_compositions(self, phase_type: str) -> Dict[str, Dict[int, Dict]]:
        """
        Extracts phase compositions for each phase at each timestep.
        For salt phases, extracts cation and anion compositions.
        For gas and solid phases, extracts species compositions.
        
        Args:
            phase_type (str): Type of phase to extract ("salt", "gas", or "solid")
        
        Returns:
            Dict: Dictionary with composition data specific to the phase type
        """
        logger.info(f"Extracting {phase_type} phase compositions")
        
        # Structure depends on phase type
        compositions = {}
        
        for timestep_str in self.str_timesteps:
            timestep = int(timestep_str)
            
            # Get phases of the requested type for this timestep
            phases = self.phase_data.get(phase_type, {}).get(timestep_str, {})
            
            for phase_name, phase_data in phases.items():
                if phase_name not in compositions:
                    compositions[phase_name] = {}
                
                # Special handling for salt phases (MSFL)
                if phase_type == "salt":
                    compositions[phase_name][timestep] = {
                        "cations": {},
                        "anions": {}
                    }
                    
                    # Extract cation data
                    if "cations" in phase_data:
                        for cation, cation_data in phase_data["cations"].items():
                            if "mole fraction" in cation_data:
                                mole_percentage = float(cation_data["mole fraction"]) * 100
                                compositions[phase_name][timestep]["cations"][cation] = mole_percentage
                    
                    # Extract anion data
                    if "anions" in phase_data:
                        for anion, anion_data in phase_data["anions"].items():
                            if "mole fraction" in anion_data:
                                mole_percentage = float(anion_data["mole fraction"]) * 100
                                compositions[phase_name][timestep]["anions"][anion] = mole_percentage
                
                # Process solution phases (gas)
                elif "species" in phase_data:
                    compositions[phase_name][timestep] = {}
                    for species, species_data in phase_data["species"].items():
                        if "mole fraction" in species_data:
                            mole_percentage = float(species_data["mole fraction"]) * 100
                            compositions[phase_name][timestep][species] = mole_percentage
                
                # Process pure condensed phases (solid)
                elif "moles" in phase_data and float(phase_data["moles"]) > 0:
                    if phase_name not in compositions:
                        compositions[phase_name] = {}
                    
                    # Pure phases are 100% of themselves
                    compositions[phase_name][timestep] = {phase_name: 100.0}
        
        logger.info(f"Extracted composition data for {len(compositions)} {phase_type} phases")
        return compositions
    
    def calculate_phase_mole_percent(self, phase_type: str, timestep: str) -> Dict[str, float]:
        """
        Calculate phase mole percentages within a given phase type for a timestep.
        
        Args:
            phase_type (str): The phase type (salt, gas, solid)
            timestep (str): The timestep to process
            
        Returns:
            Dict[str, float]: Dictionary mapping phase names to their mole percentages
        """
        phase_mole_percents = {}
        
        # Get all phases of this type for the timestep
        timestep_phases = self.phase_data.get(phase_type, {}).get(timestep, {})
        
        # Calculate total moles across all phases of this type
        total_moles = 0
        for phase_name, phase_data in timestep_phases.items():
            moles = float(phase_data.get("moles", 0))
            total_moles += moles
        
        # Calculate percentage for each phase
        if total_moles > 0:
            for phase_name, phase_data in timestep_phases.items():
                moles = float(phase_data.get("moles", 0))
                phase_mole_percents[phase_name] = (moles / total_moles) * 100
        
        return phase_mole_percents
    
    def generate_phase_json(self, phase_type: str) -> Dict[str, Dict[str, Any]]:
        """
        Create a phase-specific JSON structure.
        
        Args:
            phase_type (str): The phase type (salt, gas, solid)
            
        Returns:
            Dict[str, Dict[str, Any]]: Phase-specific JSON structure
        """
        logger.info(f"Generating {phase_type} phase JSON")
        
        # Extract phase compositions
        phase_compositions = self.extract_phase_compositions(phase_type)
        
        phase_json = {}
        
        # Process each timestep
        for timestep_str in self.str_timesteps:
            timestep = int(timestep_str)
            
            # Calculate phase mole percentages for this timestep
            phase_mole_percents = self.calculate_phase_mole_percent(phase_type, timestep_str)
            
            timestep_data = {}
            
            # Process each phase in this timestep that has composition data
            for phase_name, timestep_compositions in phase_compositions.items():
                if timestep not in timestep_compositions:
                    continue
                
                composition_data = timestep_compositions[timestep]
                
                # Get the phase percentage
                phase_percent = phase_mole_percents.get(phase_name, 0)
                
                # Get original phase data
                original_phase_data = self.phase_data[phase_type][timestep_str].get(phase_name, {})
                
                # Build the phase entry based on phase type
                phase_entry = {
                    "phase_percent": phase_percent,
                    "moles": float(original_phase_data.get("moles", 0)),
                    "type": phase_type
                }
                
                # Add specific composition data based on phase type
                if phase_type == "salt":
                    phase_entry["cation_mole_percent"] = composition_data["cations"]
                    phase_entry["anion_mole_percent"] = composition_data["anions"]
                else:
                    phase_entry["species_mole_percent"] = composition_data
                
                # Add to timestep data
                timestep_data[phase_name] = phase_entry
            
            if timestep_data:
                phase_json[timestep_str] = timestep_data
        
        logger.info(f"Generated {phase_type} phase JSON with {len(phase_json)} timesteps")
        return phase_json
    
    def process_all_phases(self) -> Tuple[Dict, Dict, Dict]:
        """
        Process all phase types and generate their respective JSON structures.
        
        Returns:
            Tuple[Dict, Dict, Dict]: Tuple of salt, gas, and solid phase JSON structures
        """
        logger.info("Processing all phases")
        
        # Extract phase data by type
        self.extract_phase_data()
        
        # Generate JSON for each phase type
        salt_json = self.generate_phase_json("salt")
        gas_json = self.generate_phase_json("gas")
        solid_json = self.generate_phase_json("solid")
        
        return salt_json, gas_json, solid_json
    
    def save_phase_jsons(self, output_directory: str) -> Dict[str, str]:
        """
        Save phase-specific JSON files.
        
        Args:
            output_directory (str): Directory to save the JSON files
            
        Returns:
            Dict[str, str]: Dictionary mapping phase types to their output file paths
        """
        logger.info(f"Saving phase JSON files to {output_directory}")
        
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        # Process all phases
        salt_json, gas_json, solid_json = self.process_all_phases()
        
        # Save the JSON files
        output_paths = {}
        
        salt_path = os.path.join(output_directory, "Salt.json")
        with open(salt_path, 'w') as f:
            json.dump(salt_json, f, indent=2)
        output_paths["salt"] = salt_path
        
        gas_path = os.path.join(output_directory, "Gas.json")
        with open(gas_path, 'w') as f:
            json.dump(gas_json, f, indent=2)
        output_paths["gas"] = gas_path
        
        solid_path = os.path.join(output_directory, "Solids.json")
        with open(solid_path, 'w') as f:
            json.dump(solid_json, f, indent=2)
        output_paths["solid"] = solid_path
        
        logger.info(f"Saved phase JSON files: {', '.join(output_paths.values())}")
        return output_paths


def main():
    """
    Main function to demonstrate the usage of the PhaseSpecificDataProcessor.
    """
    import argparse
    from CondensedReportGenerator2 import CondensedReportGenerator
    from Data_Load_and_Parse import DataLoaderParser
    
    parser = argparse.ArgumentParser(description='Phase-Specific Data Processor')
    parser.add_argument('input_dir', help='Directory containing input files')
    parser.add_argument('--output-dir', default='output', help='Directory to save output files')
    args = parser.parse_args()
    
    # Load the data using DataLoaderParser from Component 1
    loader = DataLoaderParser(args.input_dir)
    fuel_salt_data, surrogate_vector, thermochimica_data = loader.load_all_data()
    
    # Generate condensed report using CondensedReportGenerator from Component 2
    report_generator = CondensedReportGenerator(thermochimica_data)
    condensed_report = report_generator.generate_condensed_report()
    
    # Create an instance of the PhaseSpecificDataProcessor
    processor = PhaseSpecificDataProcessor(condensed_report, surrogate_vector)
    
    # Save the phase-specific JSON files
    output_paths = processor.save_phase_jsons(args.output_dir)
    
    # Log the output paths
    for phase_type, path in output_paths.items():
        logger.info(f"{phase_type.capitalize()} phase data saved to {path}")


if __name__ == "__main__":
    main()