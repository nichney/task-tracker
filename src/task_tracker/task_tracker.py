#!/usr/bin/python
# A simple CLI Task Tracker
import argparse
import json
from time import time, gmtime, strftime
from contextlib import contextmanager

@contextmanager
def open_tasks():
    all_tasks = []
    try:
        with open('tasks.json', 'r') as f:
            all_tasks = json.load(f)
    except Exception as e:
        all_tasks = []

    yield all_tasks

    try:
        with open('tasks.json', 'w') as f:
            json.dump(all_tasks, f)
    except Exception as e:
        print(f'Error while saving tasks: {e}')
        


def on_add(args):
    with open_tasks() as all_tasks:
        if all_tasks:
            last_id = all_tasks[-1]['id']
        else:
            last_id = 0
        task_text = ' '.join(args.text)
        if not task_text:
            print('Error: the description cannot be empty')
            return
        all_tasks.append({ 'id': last_id+1,
                     'description': task_text,
                     'status': 'todo',
                     'createdAt': time(),
                     'updatedAt': time()
                })

def on_update(args):
    with open_tasks() as all_tasks: 
        new_task_text = ' '.join(args.text)
        if not new_task_text:
            print('Error: the description cannot be empty')
            return
        for task in all_tasks:
            if task['id'] == args.id:
                task['description'] = new_task_text
                task['updatedAt'] = time()
                return
        else:
            print(f'Error: task {args.id} not found')

def on_delete(args):
    with open_tasks() as all_tasks:
        for task in all_tasks:
            if task['id'] == args.id:
                all_tasks.remove(task)
                return
        else:
            print(f'Error: task {args.id} not found')

def mark_in_progress(args):
    with open_tasks() as all_tasks:
        for task in all_tasks:
            if task['id'] == args.id:
                task['status'] = 'in-progress'
                task['updatedAt'] = time()
                return
        else:
            print(f'Error: task {args.id} not found')
            return

def mark_done(args):
    with open_tasks() as all_tasks:
        for task in all_tasks:
            if task['id'] == args.id:
                task['status'] = 'done'
                task['updatedAt'] = time()
                return
        else:
            print(f'Error: task {args.id} not found')
            return

def list_tasks(args):
    with open_tasks() as all_tasks:
    
        ID_WIDTH = 5
        DESC_WIDTH = max((len(task['description']) for task in all_tasks), default=20)
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
            creation_date = strftime('%Y-%m-%d %H:%M:%S', gmtime(task['createdAt']))
            update_date = strftime('%Y-%m-%d %H:%M:%S', gmtime(task['updatedAt']))
            row = (
                f"{str(task['id']).ljust(ID_WIDTH)} | "
                f"{task['description'].ljust(DESC_WIDTH)} | "
                f"{task['status'].ljust(STATUS_WIDTH)} | "
                f"{str(creation_date).ljust(TIME_WIDTH)} | "
                f"{str(update_date).ljust(TIME_WIDTH)}"
            )
            print(row)


def main():
    parser = argparse.ArgumentParser(
            prog='task-tracker',
            description='A simple CLI Task Tracker')
    subparsers = parser.add_subparsers(required=True)

    commands = [
        ('add', 'Add a new task', on_add, [('text', '+', 'Task text')]),
        ('update', 'Update a task', on_update, [('id', 'int', 'Task ID'), ('text', '+', 'New task text')]),
        ('delete', 'Delete a task', on_delete, [('id', 'int', 'Task ID')]),
        ('mark-in-progress', 'Mark task as in-progress', mark_in_progress, [('id', 'int', 'Task ID')]),
        ('mark-done', 'Mark task as done', mark_done, [('id', 'int', 'Task ID')]),
        ('list', 'List tasks', list_tasks, [('status', '?', 'List tasks by status', ['done', 'todo', 'in-progress'])])
    ]

    for cmd, help_text, func, args in commands:
        subparser = subparsers.add_parser(cmd, help=help_text)
        for arg_name, arg_type, arg_help, *choices in args:
            if arg_type == '+':
                subparser.add_argument(arg_name, nargs='+', help=arg_help)
            elif arg_type == 'int':
                subparser.add_argument(arg_name, type=int, help=arg_help)
            elif arg_type == '?':
                subparser.add_argument(arg_name, nargs='?', choices=choices[0], help=arg_help)
        subparser.set_defaults(func=func)

    args=parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
