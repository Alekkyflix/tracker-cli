import json 

#add, update and delete tasks
#def main():
    #print(f'Running Tracker CLI...')
    #task_file_path = "intents.json"
    #saving to file path
   # save_task(task_file_path)


def add_task(task):
    print('Add task')
    with open('intents.json','r+') as f:
        data = json.load(f)
        data.append({'task':task, 'completed':False})
        f.seek(0)
        json.dump(data, f, indent=4)

        #my brain :)
    #task = input(f'Add task:\n' )
    #task_date = input('date:')
    #print('Task description')
    #task_desc = input('Task description')
    #print(f'{task}, {task_date}, {task_desc}')

def view_tasks(task):
    
    with open('intents.json', 'r+') as f:
        data = json.load()
        for i, in enumerate(data):
            print(f'{i+1}.{task["task"]}{"(completed)" if task["completed"] else ""}')
            f.seek(0)
            json.dump(data, f, indent=4)
    

#def update_task(task):
    #new_task = str
    #task.append(new_task)

def mark_task_completed(index):
    with open ('intents.json','r+') as f:
        data = json.load()
        data[index-1]['completed']=True
        f.seek(0)
        json.dump(data, f, indent=4)

def delete_task(index):
    with open ('intents.json','r+') as f:
        data = json.load()
        del data[index - 1]
        f.seek(0)
        json.dump(data, f, indent=4)

    #my brain :)
    # mark a task as in progress or done
#def task_done(task):
    #for task_done in enumerate(task):
        #print(f" {task_done}")
    #if task_done in task == 1:
        #print(f"{task_done}")
    #elif task in task >= 0.1 <=0.9:
       # print("Task incomplete")
    #else:
       # print("Task incomplete")
    

def save_task(task_file_path, task):
    print(f'Saving to file path... :{task} to {task_file_path}')
    


        # list all tasks
def list_all_tasks(task):
    print(f"{task}")

while True:
    command = input('Enter a command(add, view, mark, delete):')
    if command == 'add':
        task = input('Enter the task: ')
        add_task(task)
    elif command == 'view':
        view_tasks()
    elif command == 'mark':
        index = int(input('Enter the task index: '))
        mark_task_completed(index)
    elif command == 'delete':
        index = int(input('Enter the task index: '))
        delete_task(index)
    else: print('Invalid command')
    
    




