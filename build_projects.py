# this script go outside this folder and check on folder projects 
# check how many folder are there 
# ffor each folder check if there is a project.json file 
# if there is a project.json file read it 
# then got to main folder and add the project to projects.json file 
import os 
import json

def main(): 
    projects_folder = "/home/cukjahp/Desktop/portofolio/projects"
    print(os.path.exists(projects_folder))
    print(os.path.isdir(projects_folder))
    print(os.listdir("/home/cukjahp/Desktop/portofolio/projects"))
    
    projects = []

    for folder in os.listdir(projects_folder):
        print(folder)
        full_path = os.path.join(projects_folder, folder)
        print(full_path)
        print(f'Is is a directory/folder:  {os.path.isdir(full_path)}')
        if not os.path.isdir(full_path):
            continue
        project_json_path = os.path.join(full_path, "project.json")
        print(f'Does project.json exist: {os.path.exists(project_json_path)}')
        if not os.path.exists(project_json_path):
            print(f'Project {folder} or folder with the name {folder} does not have a project.json file please create it ')
            continue
        with open(project_json_path, "r") as f:
            project_data = json.load(f)
            print(json.dumps(project_data, indent=4))
        print(f.closed)
        projects.append(project_data)
        
    print(f'Projects list from global variable is:  \n{projects}' )
    main_projects_json_path  = "/home/cukjahp/Desktop/portofolio/portofolioMain/projects.json"
    with open(main_projects_json_path, 'w') as f:
        json.dump(projects, f, indent=4)

main()