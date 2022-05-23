import tkinter as tk
import json


projects = []
with open('Projects.txt') as f:
    for line in f:
        if line[-1] == "\n":
            projects.append(line[:-1])
        else:
            projects.append(line)

master = tk.Tk()

buttons = [tk.Button(master), tk.Button(master), tk.Button(master), tk.Button(master), tk.Button(master),
           tk.Button(master), tk.Button(master), tk.Button(master), tk.Button(master), tk.Button(master)]

for index, project in enumerate(projects):
    tk.Label(master, text=project).grid(row=index)
    buttons[index].grid(row=index, column=1, ipadx=20, ipady=20)

data = {
  'index1': 1,
  'index2': 2
}
with open('logged_time.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

tk.mainloop()
