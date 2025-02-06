#!/bin/bash

# Clean previous builds
cd docs
make clean

# Generate API documentation
sphinx-apidoc -o source/api ../src

# Build HTML documentation
make html

# Print success message
echo "Documentation built successfully at docs/build/html/index.html"