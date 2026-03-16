#!/bin/bash

echo "Script started at $(date)"

echo "Current directory: $(pwd)"


readarray -t projects_titles < <(jq -r '.[].title' projects.json)
count=${#projects_titles[@]}
echo "Projects: ${projects_titles[@]}"
echo "Number of project: $count"

cd ../projects
echo "Current directory: $(pwd)"
find . -maxdepth 1 -type d ! -path .
readarray -t folders_names < <(find . -maxdepth 1 -type d ! -path .)
echo "Array of folders names: ${folders_names[@]}"
count_folders=${#folders_names[@]}
echo "Number of fodlers: $count_folders"

if [ $count = $count_folders ]; then 
    echo "The number of Json titles is: $count the same with the number of folders 
    in directory projects which is: $count_folders so script will do nothing else"
else 
    echo "Current directory $(pwd)"
    cd ../portofolioMain 
    python3 build_projects.py
    echo "Current directory $(pwd)"
    git add .
    git commit -m "New project added name ${projects_titles[0]}"
    git status
    echo "The project title is: ${projects_titles[0]}"
    git push -u origin HEAD --dry-run
fi








# Add the shebang line (#!/bin/bash)
# Print a message so you know the script started (use echo)
# Run python3 build_projects.py to regenerate projects.json
# cd into projects folder and we print if we in the right folder
# count the number of object in projects.json and maybe you can print out that one 


