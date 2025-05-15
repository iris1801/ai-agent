def log_output(task, output):
    with open("logs/actions.log", "a") as f:
        f.write(f"--- TASK: {task} ---\n{output}\n\n")
