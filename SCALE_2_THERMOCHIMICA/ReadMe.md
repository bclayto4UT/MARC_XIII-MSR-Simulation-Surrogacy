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
