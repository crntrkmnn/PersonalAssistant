# tasks.py

import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task_text):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks[task_id] = task_text
    save_tasks(tasks)
    print("Görev eklendi!")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Henüz görev yok.")
    for task_id, task_text in tasks.items():
        print(f"{task_id}: {task_text}")
