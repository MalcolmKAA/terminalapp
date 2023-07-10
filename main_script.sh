#!/bin/bash

echo "Setting up and running the project..."

# Check Python version, install if necessary
# You can adjust the required version as per your project
required_python_version=3.8
python_version=$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)
if [ $python_version != $required_python_version ]
then
    echo "Required Python version not found. Please install Python $required_python_version."
    exit 1
fi

# Create a virtual environment and activate it
python3 -m venv env
source env/bin/activate

chmod +x test.py

# Run tests
echo "Running tests..."
python3 ./test.py

# Make main.py executable
chmod +x main.py

# Run main.py
echo "Running weightlifting program program..."
python3 ./main.py



