# Surrogate Map Generation

This repository contains tools for generating surrogate maps and visualizations for thermochemistry research. The toolkit processes chemical element data to create surrogate mappings, visualize them as a periodic table, and convert the data to JSON format.

## Contents

- `Mapping_At_1.py`: Generates surrogate mappings for chemical elements
- `Mapping_Plotter.py`: Creates a visualization of the surrogate periodic table
- `Json_Map_Creation.py`: Converts CSV data to JSON format
- `PubChemElements_all.csv`: Database of all chemical elements
- `PubChemElements_with_surrogates.csv`: Chemical elements with surrogate mappings
- `generate_surrogate_maps.sh`: Automation script to run the entire workflow

## Requirements

- Python 3.x
- Required Python packages (consider adding a `requirements.txt` file)
- Bash shell (for running the automation script)

## Usage

### Manual Execution

You can run each script individually:

```bash
# Generate surrogate mappings
python Mapping_At_1.py > Report.out

# Create surrogate periodic table visualization
python Mapping_Plotter.py

# Convert data to JSON format
python Json_Map_Creation.py
```

### Automated Execution

For convenience, use the provided automation script:

```bash
# Make the script executable (first time only)
chmod +x generate_surrogate_maps.sh

# Run the complete workflow
./generate_surrogate_maps.sh
```

## Output Files

The scripts generate the following output files:

- `Report.out`: Detailed report of the surrogate mapping process
- `Surrogate_periodic_table.png`: Visualization of the surrogate periodic table
- `surrogates_and_candidates.json`: JSON file containing surrogate mappings and candidates

## Notes

- The current implementation may show identical styles for some elements (e.g., Kr and Br)
- This is Generation I of the Surrogate Map Generation toolkit, as such it has several known flaws that have been accepted for the demonstration of this framework, improved mapping methodologies will be forthcoming.

