# Task Tracker

A simple command-line task management tool that allows you to create, update, delete, and track the status of your tasks. 

https://roadmap.sh/projects/task-tracker

## Features

- Create new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as in-progress or done
- List all tasks or filter by status
- Persistent storage using JSON file

## Installation

```bash
git clone https://github.com/nichney/task-tracker.git
cd task-tracker
#virtual env - optionally
pipenv shell
pip install .
```

## Usage

### Adding a task
```bash
task-tracker add "Buy groceries"
```

### Updating a task
```bash
task-tracker update 1 "Buy more groceries"
```

### Deleting a task
```bash
task-tracker delete 1
```

### Marking task as in-progress
```bash
task-tracker mark-in-progress 1
```

### Marking task as done
```bash
task-tracker mark-done 1
```

### Listing tasks
```bash
# List all tasks
task-tracker list

# List tasks by status
task-tracker list todo
task-tracker list in-progress
task-tracker list done
```

## Task Status

Tasks can have one of the following statuses:
- `todo`: Task is not started
- `in-progress`: Task is being worked on
- `done`: Task is completed

## Data Storage

Tasks are stored in a JSON file (`tasks.json`) in the following format:
```json
[
  {
    "id": 1,
    "description": "Task description",
    "status": "todo",
    "createdAt": 1234567890,
    "updatedAt": 1234567890
  }
]
```

## Testing project with tox
``` bash 
pip install tox
tox
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
