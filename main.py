import time
import tkinter as tk
import json
from datetime import datetime, timedelta
import math
master = tk.Tk()


def update_active(local_index):
    global currentProjectIndex
    print("prev:", currentProjectIndex)
    currentProjectIndex = local_index
    print("curr:", currentProjectIndex)


def log_data():
    data = {"Logged time": datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
            }
    for local_index, local_project in enumerate(projects):
        timeArray[local_index] -= timedelta(microseconds=timeArray[local_index].microseconds)
        data[local_project] = str(timeArray[local_index])
    json.dump(data, json_file, ensure_ascii=False, indent=4)


def background_task():
    global updated_time
    timeArray[currentProjectIndex] += (datetime.now() - updated_time)
    updated_time = datetime.now()
    print("Time:", datetime.now().strftime("%d/%m/%Y - %H:%M:%S"))
    print(timeArray)
    master.after(1000, background_task)


currentProjectIndex = 0
timeArray = []
projects = []
start_time = datetime.now()
updated_time = datetime.now()
json_file = open('logged_time.json', 'a', encoding='utf-8')
projects_file = open('Projects.txt')
for line in projects_file:
    if line[-1] == "\n":
        projects.append(line[:-1])
        timeArray.append(datetime.now()-datetime.now())
    else:
        projects.append(line)
        timeArray.append(datetime.now()-datetime.now())
timeArray.append(datetime.now()-datetime.now())
currentProjectIndex = len(timeArray)-1

buttons = [tk.Button(master, command=lambda: update_active(0)), tk.Button(master, command=lambda: update_active(1)),
           tk.Button(master, command=lambda: update_active(2)), tk.Button(master, command=lambda: update_active(3)),
           tk.Button(master, command=lambda: update_active(4)), tk.Button(master, command=lambda: update_active(5)),
           tk.Button(master, command=lambda: update_active(6)), tk.Button(master, command=lambda: update_active(7)),
           tk.Button(master, command=lambda: update_active(8)), tk.Button(master, command=lambda: update_active(9))]

for index, project in enumerate(projects):
    tk.Label(master, text=project).grid(row=index)
    buttons[index].grid(row=index, column=1, ipadx=20, ipady=20)

tk.Label(master, text="Log the time in the Json file").grid(row=index+1)
logger = tk.Button(master,command=log_data)
logger.grid(row=index+1, column=1, ipadx=20, ipady=20)

background_task()
master.mainloop()
