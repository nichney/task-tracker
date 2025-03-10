#!/usr/bin/python
# A simple CLI Task Tracker
import argparse
import json
from time import time

def load_tasks():
    try:
        f = open('tasks.json', 'r')
        return json.load(f)
    except FileNotFoundError:
        return []    

def write_tasks(tasks):
    data = json.dumps(tasks)
    with open('tasks.json', 'w') as f:
        f.write(data)


def on_add(args):
    all_tasks = load_tasks()
    if all_tasks:
        last_id = all_tasks[-1]['id']
    else:
        last_id = 0
    all_tasks.append({ 'id': last_id+1,
                 'description': args.text[0],
                 'status': 'todo',
                 'createdAt': time(),
                 'updatedAt': time()
            })
    write_tasks(all_tasks)

def on_update(args):
    pass

def on_delete(args):
    pass

def mark_in_progress(args):
    pass

def mark_done(args):
    pass

def list_tasks(args):
    all_tasks = load_tasks()
    
    ID_WIDTH = 5
    DESC_WIDTH = 20
    STATUS_WIDTH = 15
    TIME_WIDTH = 20
    header = (
        f"{'ID'.ljust(ID_WIDTH)} | "
        f"{'Description'.ljust(DESC_WIDTH)} | "
        f"{'Status'.ljust(STATUS_WIDTH)} | "
        f"{'Created At'.ljust(TIME_WIDTH)} | "
        f"{'Updated At'.ljust(TIME_WIDTH)}"
    )
    print(header)
    print('-' * len(header))
    # Filter tasks by status if required 
    tasks_to_show = [task for task in all_tasks if task['status'] == args.status] if args.status else all_tasks
    
    for task in tasks_to_show:
        row = (
            f"{str(task['id']).ljust(ID_WIDTH)} | "
            f"{task['description'].ljust(DESC_WIDTH)} | "
            f"{task['status'].ljust(STATUS_WIDTH)} | "
            f"{str(task['createdAt']).ljust(TIME_WIDTH)} | "
            f"{str(task['updatedAt']).ljust(TIME_WIDTH)}"
        )
        print(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog='task-tracker',
            description='A simple CLI Task Tracker')
    subparsers = parser.add_subparsers(required=True)

    # for add
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('text', nargs='+', help='Task text')
    add_parser.set_defaults(func=on_add)

    # for update
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument('text', nargs='+', help='New task text')
    update_parser.set_defaults(func=on_update)

    # for delete
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')
    delete_parser.set_defaults(func=on_delete)

    # for mark-in-progress
    in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark task as in-progress')
    in_progress_parser.add_argument('id', type=int, help='Task ID')
    in_progress_parser.set_defaults(func=mark_in_progress)

    # for mark-done
    done_parser = subparsers.add_parser('mark-done', help='Mark task as done')
    done_parser.add_argument('id', type=int, help='Task ID')
    done_parser.set_defaults(func=mark_done)

    # for list
    list_parser = subparsers.add_parser('list', help='Mark task as done')
    list_parser.add_argument('status', 
                            nargs='?', 
                            choices=['done', 'todo', 'in-progress'], 
                            help='List tasks by status')
    list_parser.set_defaults(func=list_tasks)
  

    args=parser.parse_args()
    args.func(args)
