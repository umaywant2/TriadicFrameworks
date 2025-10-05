#!/bin/bash
read -p "Enter project name: " name
cp -r docs/_template docs/$name
find docs/$name -type f -exec sed -i "s/{{PROJECT_NAME}}/$name/g" {} +
echo "Project '$name' initialized from MMR v1.1 template."
