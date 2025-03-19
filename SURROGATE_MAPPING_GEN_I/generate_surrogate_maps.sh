#!/bin/bash

# Surrogate Map Generation Automation Script
# This script automates the process of generating surrogate maps and visualizations

# Set the working directory to the current directory
WORKING_DIR=$(pwd)
echo "Working directory: $WORKING_DIR"

# Step 1: Run the Mapping_At_1.py script and save output to Report.out
echo "Running Mapping_At_1.py..."
python Mapping_At_1.py > Report.out
if [ $? -eq 0 ]; then
    echo "✓ Successfully generated Report.out"
else
    echo "✗ Error running Mapping_At_1.py"
    exit 1
fi

# Step 2: Run the Mapping_Plotter.py script to generate the surrogate periodic table
echo "Running Mapping_Plotter.py..."
python Mapping_Plotter.py
if [ $? -eq 0 ]; then
    echo "✓ Successfully generated Surrogate_periodic_table.png"
else
    echo "✗ Error running Mapping_Plotter.py"
    exit 1
fi

# Step 3: Run the Json_Map_Creation.py script to generate the JSON file
echo "Running Json_Map_Creation.py..."
python Json_Map_Creation.py
if [ $? -eq 0 ]; then
    echo "✓ Successfully converted CSV to JSON (surrogates_and_candidates.json)"
else
    echo "✗ Error running Json_Map_Creation.py"
    exit 1
fi

# Check if all output files exist
echo "Verifying output files..."
if [ -f "Report.out" ] && [ -f "Surrogate_periodic_table.png" ] && [ -f "surrogates_and_candidates.json" ]; then
    echo "All output files successfully generated!"
    echo "- Report.out"
    echo "- Surrogate_periodic_table.png"
    echo "- surrogates_and_candidates.json"
else
    echo "Some output files are missing!"
fi

echo "Surrogate Map Generation complete!"