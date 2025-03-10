#!/usr/bin/python
# A simple CLI Task Tracker
import argparse
import sys

def on_add(args):
    pass

def on_update(args):
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

    args=parser.parse_args()
    args.func(args)
