#!/usr/bin/python
# A simple CLI Task Tracker
import argparse
import sys

def on_add(args):
    pass

def on_update(args):
    pass

def on_delete(args):
    pass

def mark_in_progress(args):
    pass

def mark_done(args):
    pass

def list_tasks(args):
    pass


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
