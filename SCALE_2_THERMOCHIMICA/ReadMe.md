# Thermochimica Workflow Automation

This repository contains a workflow automation script for the Thermochimica analysis pipeline. The script automates the execution of all modules in the correct sequence while handling dependencies.

## Overview

The Thermochimica workflow processes nuclear fuel salt data through multiple analytical steps, generating reports and processed data for thermochemical analysis. The automation script handles the entire pipeline from nuclide vector processing to decoupled species processing.

## Requirements

- Python 3.x
- Thermochimica and its dependencies
- Various Python modules including:
  - `nuclide_vector_processor_v2.py`
  - `Surogate_Processing.py`
  - `Input_Generator_and_Execution_Multi.py`
  - And others listed in the workflow

## Usage

Run the workflow with the default input file:

```bash
./run_scale2thermochimica_workflow.py
```

Or specify a custom input file:

```bash
./run_scale2thermochimica_workflow.py custom_input.json
```

By default, the script uses `ThEIRENE_FuelSalt_NuclideDensities.json` as the input file if none is specified.

## Workflow Steps

The automation executes the following steps in sequence:

1. Process nuclide vector from input file
2. Process surrogate vector
3. Generate and execute Thermochimica inputs
4. Generate condensed Thermochimica report
5. Generate phase analysis report
6. Generate MSFL phase report
7. Analyze redox ratios
8. Process phase-specific data
9. Decouple gas phase data
10. Decouple solids phase data
11. Decouple salt phase data
12. Decouple salt nuclides
13. Process decoupled species

## Output

The script creates the following output directories if they don't exist:
- `output`: Contains generated reports and processed data
- `msfl_output`: Contains MSFL-specific outputs
- `tc_inputs`: Contains generated Thermochimica input files
- `analysis_output`: Contains generated reports for decoupled phases 

## Logging

The script generates detailed logs for each run with timestamps. Logs are saved to:
- `thermochimica_workflow_YYYYMMDD_HHMMSS.log`

Log entries include start and completion times for each step, stdout and stderr output, and error messages if any step fails.

## Error Handling

The workflow continues executing subsequent steps even if a step fails. A summary of successes and failures is provided at the end of execution.

## Contributing

Please feel free to submit issues or pull requests to improve the workflow automation.

## Acknowledgments

- Developers of Thermochimica
- [Add any other acknowledgments here]

------

# File Specifics:

## Data_Load_and_Parse.py

**Type:** Python script (Component 1: Data Loader and Parser)

**Purpose:** Loads and parses all input files required for the Post-Processing module of the Thermochimica workflow.

**Inputs:**
- Base directory path containing all input files
- Command-line arguments for input and output directories

**Outputs:**
- Processed JSON files saved to the output directory:
  - `processed_fuel_salt_data.json`
  - `processed_surrogate_vector.json`
  - `thermochimica_data_summary.json`
- Console output with statistics about loaded data
- Logging information

**Key Features:**
- Parses three primary data sources:
  1. Element_Vector.json: Contains element data with atom densities and mole percentages
  2. surrogate_vector.json: Contains surrogate mappings with atom densities and contribution percentages
  3. Thermochimica output files: Contains thermodynamic calculation results for each timestep
- Validates data structure integrity
- Provides logging of all operations
- Organizes timestep data from multiple Thermochimica runs
- Supports command-line usage through an argparse interface

**File Structure Dependencies:**
- Expects the following structure:
  ```
  base_directory/
  ├── Element_Vector.json
  ├── surrogate_vector.json
  └── tc_inputs/
      ├── timestep_0/
      │   ├── ThEIRNE_Cycle_t0.ti       # Input file
      │   ├── ThEIRNE_Cycle_t0.log      # Text output
      │   └── ThEIRNE_Cycle_t0.json     # Primary data source
      └── timestep_1/
          └── ...
  ```

**Usage Example:**
```bash
python Data_Load_and_Parse.py /path/to/input_directory --output-dir /path/to/output
```

This script serves as the foundation for the post-processing pipeline, ensuring all necessary data is properly loaded and validated before subsequent analysis steps in the Thermochimica workflow.

## CondensedReportGenerator2.py
This Python script is the second component in the Thermochimica workflow automation pipeline, responsible for creating consolidated reports from Thermochimica output data. The script processes and combines data from multiple timesteps into a single organized file without modifying the underlying data structure.

### Key Features:
- Stitches together Thermochimica outputs across all timesteps in chronological order
- Detects and logs missing timesteps
- Generates summary reports with phase information
- Identifies salt phases (MSFL) in the processed data

### Inputs:
- `thermochimica_data`: Dictionary containing Thermochimica output data organized by timestep
- `output_directory`: Directory where reports will be saved
- `filename`: Optional name for the output report file (defaults to "Condensed_Thermochimica_Report.json")

### Outputs:
- Primary JSON report file containing all timestep data in its original structure
- Summary file with statistics about timesteps and phase information
- Returns paths to saved files for downstream processing

When run as a standalone script, it accepts command-line arguments for input and output directories, loading data through the DataLoaderParser component from Component 1.


I'll provide short introductions for each of the attached Python files, explaining their inputs, outputs, and purpose.


## Decouple_Gas.py
This script processes a Gas.json file to decouple species mole percentages based on surrogate vector data. It handles both simple elements and molecular species by parsing molecular formulas and substituting elements according to their surrogate contributions.

**Inputs:**
- `gas_path`: Path to the Gas.json file containing original gas phase data (default: "output/Gas.json")
- `surrogate_vector_path`: Path to surrogate_vector.json containing element surrogate percentages (default: "surrogate_vector.json")
- `output_path`: Path for writing the decoupled output (default: "output/Decoupled_Gas.json")

**Outputs:**
- Decoupled Gas.json file with species mole percentages redistributed according to surrogate contributions
- Console logging of decoupling process

## Decouple_Salt.py
This script decouples ion mole percentages in salt phases based on surrogate vector data. It handles both cations and anions by extracting the primary element from each ion formula and substituting it with appropriate surrogates.

**Inputs:**
- `salt_path`: Path to the Salt.json file containing original salt phase data (default: "output/Salt.json")
- `surrogate_vector_path`: Path to surrogate_vector.json containing element surrogate percentages (default: "surrogate_vector.json")
- `output_path`: Path for writing the decoupled output (default: "output/Decoupled_Salt.json")

**Outputs:**
- Decoupled Salt.json file with ion mole percentages redistributed according to surrogate contributions
- Statistics on processed ions, including counts of decoupled ions and elements

## Decouple_Solids.py
This script processes a Solids.json file to decouple species mole percentages in solid phases based on surrogate vector data. Unlike the other scripts, it transforms species_mole_percent into element_mole_percent in the output.

**Inputs:**
- `solids_path`: Path to the Solids.json file containing original solid phase data (default: "output/Solids.json")
- `surrogate_vector_path`: Path to surrogate_vector.json containing element surrogate percentages (default: "surrogate_vector.json")
- `output_path`: Path for writing the decoupled output (default: "output/Decoupled_Solids.json")

**Outputs:**
- Decoupled Solids.json file with element_mole_percent values derived from decoupled species
- Console logging of decoupling process

## Decoupled_Species_Processor.py

### Description
This Python script processes and analyzes decoupled phase data from salt, gas, and solid JSON files. It generates comprehensive reports and visualizations that track phase presence, composition, and evolution over time.

### Inputs
- **Salt Data**: JSON file containing salt phase data (`Decoupled_Salt.json`)
- **Gas Data**: JSON file containing gas phase data (`Decoupled_Gas.json`)
- **Solids Data**: JSON file containing solid phase data (`Decoupled_Solids.json`)

### Outputs
The script generates several output files in the specified directory:
- **CSV Reports**:
  - `Phase_Presence_Report.csv`: Indicates which phases are present at each timestep
  - `Phase_Mole_Amounts_Report.csv`: Details mole amounts for each phase at each timestep
  - `Phase_Composition_Report.csv`: Detailed report of phase compositions (species/elements percentages)

- **Visualization Plots**:
  - `Phase_Mole_Amounts.png`: Graph showing all phase mole amounts over time
  - `Composition_[phase_type]_[phase_name]_[label_method].png`: Individual phase composition plots
  - `Composition_LogScale_[phase_type]_[phase_name]_[label_method].png`: Log-scale composition plots showing trace components

### Usage
The script can be run from the command line with optional arguments:
```bash
python Decoupled_Species_Processor.py --input-dir output --output-dir analysis_output --significance 1.0
```

- `--input-dir`: Directory containing input JSON files (default: 'output')
- `--output-dir`: Directory to save output files (default: 'analysis_output')
- `--significance`: Significance threshold for component reporting in percentage (default: 1.0)

### Core Functionality
- Tracks all salt, gas, and solid phases across timesteps
- Calculates phase presence/absence at each timestep
- Measures mole amounts for each phase over time
- Analyzes detailed composition data:
  - Ion percentages (cations/anions) for salt phases
  - Species percentages for gas phases
  - Element percentages for solid phases
- Creates both regular and logarithmic-scale plots to visualize both major and trace components
- Generates tabular reports suitable for spreadsheet analysis

This script serves as the final step in the Thermochimica workflow, providing comprehensive analysis of the decoupled phase data generated in previous workflow steps.

