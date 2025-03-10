#!/usr/bin/python
# A simple CLI Task Tracker
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog='task-tracker',
            description='A simple CLI Task Tracker')
    commands = ('add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list')
    for command in commands:
        parser.add_argument(command) 
