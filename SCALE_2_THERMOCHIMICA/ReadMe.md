# SCALE 2 Thermochimica Workflow

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

## Input_Generator_and_Execution_Multi.py

This script generates Thermochimica input files from surrogate vector JSON data and can execute Thermochimica calculations in parallel. It serves as an interface between processed salt composition data and the Thermochimica thermodynamic analysis tool.

**Purpose:** Generates and optionally runs Thermochimica input files for each time step in a surrogate vector JSON file.

**Inputs:**
- JSON file containing surrogate vector data with element compositions at different time steps
- Optional parameters for temperature, pressure, output directory, and scale factor
- Paths to Thermochimica data file and binary (optional)

**Outputs:**
- Thermochimica input (.ti) files for each time step
- JSON output files containing thermodynamic calculation results (when run mode is enabled)
- Log files for each calculation

**Key Features:**
- Multiprocessing support for parallel execution
- Customizable directory structure for outputs
- Element validation against known periodic table elements
- Detailed error handling and logging

## Salt_Nuclide_Decoupler.py

This script processes phase-specific salt data and decouples it into nuclide-level composition information, creating detailed analyses of the nuclide distribution across different phases of the salt.

**Purpose:** Converts element-level phase data into nuclide-level distribution data for comprehensive analysis of salt composition.

**Inputs:**
- `output/Decoupled_Salt.json`: Contains phase-specific element data for different time steps
- `Element_Vector.json`: Contains nuclide contribution percentages for each element

**Outputs:**
- `Salt_Nuclides.json`: Detailed breakdown of nuclide distributions in different salt phases

**Key Features:**
- High-precision decimal calculations to maintain numerical accuracy
- Separate handling of cations and anions in each salt phase
- Special handling for dimers (contributes twice the normal amount)
- Comprehensive error checking for mismatched time steps
I'll write an introduction for the MSFL_Phase_Report.py file based on its content and intended function:

## MSFL_Phase_Report.py

This Python script implements the `MSFLPhaseAnalysisReportGenerator` class which analyzes and generates reports specifically for molten salt fuel (MSFL) phases from Thermochimica output data. It works with condensed report data produced by the `CondensedReportGenerator` class.

### Functionality:
- Extracts and analyzes MSFL phase presence, mole amounts, and compositions over time
- Generates various CSV reports showing phase presence and mole amounts
- Creates visualization plots for MSFL phase data including:
  - Mole amounts vs. time plots
  - Species composition plots (regular and log-scale)
  - Cation composition plots (regular and log-scale)

### Inputs:
- `condensed_report`: An OrderedDict containing the condensed output data from Thermochimica simulations
- `output_directory`: Directory where output files (reports and plots) will be saved

### Outputs:
- CSV files:
  - `MSFL_Phase_Presence_Report.csv`: Shows which MSFL phases are present at each timestep
  - `MSFL_Phase_Mole_Amounts_Report.csv`: Details the mole amounts of each MSFL phase at each timestep
  - `MSFL_Phase_Composition_Report.csv`: Contains detailed species composition data for each phase
  - `MSFL_Cation_Composition_Report.csv`: Lists cation compositions for each MSFL phase

- Visualization plots:
  - `MSFL_Mole_Amounts.png`: Plot showing mole amounts of all MSFL phases over time
  - Multiple composition plots showing species distribution within phases
  - Cation composition plots (both regular and logarithmic scale)

### Usage:
The script can be run as a standalone module with command-line arguments or imported and used as part of a larger workflow. When run directly, it requires specifying an input directory containing Thermochimica data and optionally an output directory for saving results.

```bash
python MSFL_Phase_Report.py path/to/input_dir --output-dir path/to/msfl_output
```

This script is an important component in the Thermochimica workflow, specifically focused on analyzing the molten salt phases that are critical for nuclear fuel salt assessments.

## nuclide_vector_processor_v2.py
This Python script processes nuclide data from JSON files to calculate element atom densities and mole percentages. It converts isotope-specific nuclide data into elemental compositions.

**Inputs:**
- JSON file containing nuclide density data across multiple time steps
- Optional element filter list
- Plot type selection ('stackplot', 'semilog', 'combined', or 'all')

**Outputs:**
- Processed JSON file with elemental atom densities and mole percentages
- Optional isotopic contribution percentages
- Visualization plots showing elemental abundance over time

The script supports various command-line options for filtering elements, selecting plot types, and controlling output verbosity. It can generate stacked plots for major elements and semi-log plots for trace elements with very low concentrations.

## Surogate_Processing.py
This Python module maps element data to surrogate elements based on a provided mapping configuration. It's designed to condense complex elemental compositions into a smaller set of surrogate elements for simplified thermochemical analysis.

**Inputs:**
- Surrogate configuration file (`surrogates_and_candidates.json`) defining which elements map to which surrogates
- Processed element data file (output from `nuclide_vector_processor_v2.py`)

**Outputs:**
- JSON file containing:
  - Surrogate vector data with atom densities and mole percentages
  - Surrogate percentages showing each element's contribution to its surrogate

The `SurrogateProcessor` class handles the mapping of elements to surrogates and calculates the corresponding surrogate percentages. This processing step is critical for reducing computational complexity in downstream thermochemical analysis.


## Phase_Analysis_and_Report_Gen2.py

This Python script generates detailed reports and visualizations for phase presence, mole amounts, and composition data from Thermochimica output. The script works alongside the CondensedReportGenerator to analyze condensed data reports.

### Inputs:
- A condensed report from CondensedReportGenerator containing Thermochimica phase data
- Output directory path for saving reports and plots

### Outputs:
Multiple report files and visualization plots:
- **Phase_Presence_Report.csv**: Documents which phases have moles > 0 at each timestep
- **Phase_Mole_Amounts_Report.csv**: Contains mole quantities for each phase at each timestep
- **Phase_Composition_Report.csv**: Detailed breakdown of species composition within each phase
- **Non_Salt_Mole_Amounts.png**: Plot showing how non-salt phase quantities change over time
- Multiple composition plots showing major components for each phase with direct labeling

### Key Features:
- Separates solution phases from pure condensed phases in reports
- Filters out salt phases (MSFL) when focusing on non-salt analysis
- Provides significance threshold filtering for composition plots
- Uses direct labeling on plots for improved readability
- Comprehensive logging for tracking analysis process

The script can be run as a standalone module with input directory specification or integrated into the larger Thermochimica workflow.

## RedoxAnalyzer4.py

### Description
RedoxAnalyzer4.py is a Python script that serves as Component 3 in the Thermochimica workflow. It analyzes redox potentials within nuclear fuel salt systems by calculating and reporting UF3/UF4 and Cr2+/Cr3+ ratios from processed thermochimica data.

### Inputs
- **condensed_thermochimica_report.json**: A JSON file containing condensed thermochimica calculation results with detailed information about solution phases, specifically focusing on the MSFL (Molten Salt Fuel Loop) phase and its cations.
- **Command line arguments**:
  - `input_file`: Path to the condensed thermochimica report JSON file (required)
  - `--output-dir`: Directory to save output files (default: 'output')
  - `--plot-gibbs`: Optional flag to generate plots of integral Gibbs energy

### Outputs
The script generates several outputs in the specified output directory:
1. **CSV files**:
   - `uf3_uf4_ratios.csv`: Contains timestep-by-timestep UF3/UF4 ratio data
   - `cr2_cr3_ratios.csv`: Contains timestep-by-timestep Cr2+/Cr3+ ratio data
   - `gibbs_energy.csv`: Contains integral Gibbs energy values (if --plot-gibbs is specified)

2. **Plot images**:
   - `uf3_uf4_ratio_plot.png`: Semi-log plot of UF3/UF4 ratios over time
   - `cr2_cr3_ratio_plot.png`: Semi-log plot of Cr2+/Cr3+ ratios over time
   - `combined_redox_ratios_plot.png`: Combined plot of both ratio types
   - `gibbs_energy_semilog_plot.png`: Semi-log plot of Gibbs energy (if --plot-gibbs is specified)
   - `gibbs_energy_linear_plot.png`: Linear plot of Gibbs energy (if --plot-gibbs is specified)

3. **Summary files**:
   - `uf3_uf4_summary.json`: Statistical summary of UF3/UF4 ratios
   - `cr2_cr3_summary.json`: Statistical summary of Cr2+/Cr3+ ratios

### Key Features
- Calculates UF3/UF4 and Cr2+/Cr3+ redox ratios from MSFL cation data
- Handles problematic timesteps where ratios cannot be calculated
- Generates high-quality visualizations of redox trends
- Provides statistical analysis of redox behavior
- Optional analysis of Gibbs energy for thermodynamic assessment
- Comprehensive logging of analysis process and results

### Usage Example
```bash
python RedoxAnalyzer4.py path/to/condensed_thermochimica_report.json --output-dir results --plot-gibbs
```

This component is crucial for understanding the redox chemistry within molten salt fuel systems, which directly impacts corrosion behavior, fuel stability, and overall reactor safety.

## Salt_Nuclide_Decoupler.py
A Python script that processes phase-specific salt data by combining information from decoupled salt phases with nuclide vector data. The script calculates nuclide-specific mole percentages for both cations and anions in each salt phase across all timesteps.

**Inputs:**
- `output/Decoupled_Salt.json`: Contains salt phase data with cation and anion mole percentages
- `Element_Vector.json`: Contains processed fuel data with surrogate percentages by element

**Outputs:**
- `Salt_Nuclides.json`: A JSON file containing detailed nuclide-specific mole percentages for cations and anions in each salt phase at each timestep

The script uses high-precision decimal calculations to accurately distribute element compositions to their constituent nuclides while handling special cases like dimers (which contribute twice the amount). It preserves full numerical precision throughout the calculations and in the output file.

