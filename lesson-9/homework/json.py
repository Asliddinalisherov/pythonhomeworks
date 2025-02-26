import json
import csv

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks saved to {filename}.")

def display_tasks(tasks):
    print("\nTasks:")
    print("{:<5} {:<20} {:<15} {:<10}".format("ID", "Task Name", "Completed Status", "Priority"))
    print("-" * 50)
    for task in tasks:
        print("{:<5} {:<20} {:<15} {:<10}".format(task['id'], task['task'], str(task['completed']), task['priority']))

def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Completion Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def json_to_csv(tasks, csv_filename):
    try:
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['ID', 'Task Name', 'Completed Status', 'Priority']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for task in tasks:
                writer.writerow({
                    'ID': task['id'],
                    'Task Name': task['task'],
                    'Completed Status': task['completed'],
                    'Priority': task['priority']
                })
        print(f"Task data saved to {csv_filename}.")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def main():
    tasks = load_tasks('tasks.json')
    if not tasks:
        return

    display_tasks(tasks)
    calculate_stats(tasks)
    tasks[0]['completed'] = True
    save_tasks('tasks.json', tasks)
    json_to_csv(tasks, 'tasks.csv')

if __name__ == "__main__":
    main()