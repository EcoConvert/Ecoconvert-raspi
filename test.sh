#!/bin/bash

# Define the repository URL and the branch you want to fetch
REPO_URL="https://github.com/EcoConvert/Ecoconvert-raspi.git"
BRANCH_NAME="deployment"
DIR_NAME="./Ecoconvert-raspi"

# Check if the directory already exists
if [ -d "$DIR_NAME" ]; then
  echo "Directory $DIR_NAME already exists. Fetching updates from branch '$BRANCH_NAME'..."
  cd "$DIR_NAME" || exit
  git fetch origin "$BRANCH_NAME:$BRANCH_NAME"  # Fetch the specific branch
else
  echo "Cloning the repository..."
  git clone -b "$BRANCH_NAME" "$REPO_URL" "$DIR_NAME"
  cd "$DIR_NAME" || exit
fi

# Ensure the branch is checked out
git checkout "$BRANCH_NAME"

echo "Fetch completed for branch '$BRANCH_NAME'."