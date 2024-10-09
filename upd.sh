#!/bin/bash

echo "Updating requirements.txt"
source env/bin/activate
python -m pip freeze >requirements.txt