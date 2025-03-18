#!/usr/bin/env python3
"""
Thermochimica Workflow Automation Script

This script automates the execution of the Thermochimica analysis pipeline,
running all modules in the correct sequence while handling dependencies.

Usage:
    ./run_scale2thermochimica_workflow.py [input_file]
    
    If input_file is not specified, it defaults to "ThEIRENE_FuelSalt_NuclideDensities.json"
"""

import os
import sys
import subprocess
import time
import logging
import argparse
from datetime import datetime

# Setup argument parser
parser = argparse.ArgumentParser(description="Thermochimica Workflow Automation Script")
parser.add_argument("input_file", nargs="?", default="ThEIRENE_FuelSalt_NuclideDensities.json",
                    help="Input file for nuclide vector processing (default: ThEIRENE_FuelSalt_NuclideDensities.json)")
args = parser.parse_args()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"thermochimica_workflow_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Thermochimica-Workflow")

def run_command(command, description, check=True):
    """Execute a shell command and log its output."""
    logger.info(f"Starting: {description}")
    start_time = time.time()
    
    try:
        result = subprocess.run(
            command,
            check=check,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Log stdout and stderr
        if result.stdout:
            for line in result.stdout.splitlines():
                logger.info(f"STDOUT: {line}")
        
        if result.stderr:
            for line in result.stderr.splitlines():
                logger.warning(f"STDERR: {line}")
        
        elapsed_time = time.time() - start_time
        logger.info(f"Completed: {description} in {elapsed_time:.2f} seconds")
        return True
    
    except subprocess.CalledProcessError as e:
        logger.error(f"Error in {description}: {e}")
        logger.error(f"STDOUT: {e.stdout}")
        logger.error(f"STDERR: {e.stderr}")
        elapsed_time = time.time() - start_time
        logger.error(f"Failed: {description} after {elapsed_time:.2f} seconds")
        return False

def ensure_directories_exist():
    """Create necessary output directories if they don't exist."""
    directories = ["output", "msfl_output", "tc_inputs"]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")

def main():
    """Main workflow execution function."""
    input_file = args.input_file
    logger.info(f"Starting Thermochimica workflow automation with input file: {input_file}")
    
    if not os.path.exists(input_file):
        logger.error(f"Input file does not exist: {input_file}")
        sys.exit(1)
        
    start_time = time.time()
    
    # Make sure required directories exist
    ensure_directories_exist()
    
    # Define the workflow steps
    workflow = [
        {
            "command": f"python nuclide_vector_processor_v2.py -i {input_file} -o Element_Vector.json",
            "description": f"Process nuclide vector from {input_file}"
        },
        {
            "command": "python Surogate_Processing.py",
            "description": "Process surrogate vector"
        },
        {
            "command": "python Input_Generator_and_Execution_Multi.py surrogate_vector.json --run",
            "description": "Generate and execute Thermochimica inputs",
            "check": False  # Some errors are expected and handled appropriately as noted in logs
        },
        {
            "command": "python CondensedReportGenerator2.py .",
            "description": "Generate condensed Thermochimica report"
        },
        {
            "command": "python Phase_Analysis_and_Report_Gen2.py .",
            "description": "Generate phase analysis report"
        },
        {
            "command": "python MSFL_Phase_Report.py .",
            "description": "Generate MSFL phase report"
        },
        {
            "command": "python RedoxAnalyzer4.py output/Condensed_Thermochimica_Report.json",
            "description": "Analyze redox ratios"
        },
        {
            "command": "python Phase_Speceific_Data_Processor.py .",
            "description": "Process phase-specific data"
        },
        {
            "command": "python Decouple_Gas.py",
            "description": "Decouple gas phase data"
        },
        {
            "command": "python Decouple_Solids.py",
            "description": "Decouple solids phase data"
        },
        {
            "command": "python Decouple_Salt.py",
            "description": "Decouple salt phase data"
        },
        {
            "command": "python Salt_Nuclide_Decoupler.py",
            "description": "Decouple salt nuclides"
        }
    ]
    
    # Execute each step in the workflow
    success_count = 0
    failure_count = 0
    
    for i, step in enumerate(workflow, 1):
        logger.info(f"Step {i}/{len(workflow)}: {step['description']}")
        
        # Get check parameter (default to True if not specified)
        check = step.get("check", True)
        
        # Run the command
        if run_command(step["command"], step["description"], check):
            success_count += 1
        else:
            failure_count += 1
            logger.warning(f"Step {i} failed. Continuing with next step...")
    
    # Summarize the results
    total_time = time.time() - start_time
    logger.info(f"Workflow completed in {total_time:.2f} seconds")
    logger.info(f"Summary: {success_count} steps succeeded, {failure_count} steps failed")
    
    if failure_count == 0:
        logger.info("Thermochimica workflow completed successfully!")
    else:
        logger.warning(f"Thermochimica workflow completed with {failure_count} failures")

if __name__ == "__main__":
    main()