import random
import datetime


today = datetime.date.today().strftime("%d/%m/%Y")


with open('project_list.txt', 'r') as file:
    project_list = file.readlines()

if len(project_list) != 0:
    random.shuffle(project_list)
    new_project = random.choice(project_list)

    with open('current_projects.txt', 'a') as file:
        file.write(f'{today} - {new_project}')
        print('New project saved to file: current_projects.txt')

    project_list.remove(new_project)
    with open('project_list.txt', 'w') as file:
        for item in project_list:
            file.write(f'{item}')

else:
    print('Project list is empty. Please add more projects.')