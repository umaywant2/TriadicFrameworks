# Tops — Orchestrates coin tasks and agent execution

class Tops:
    def __init__(self):
        self.task_queue = []

    def add_task(self, coin_id, agent_name):
        task = {"coin": coin_id, "agent": agent_name}
        self.task_queue.append(task)
        print(f"[Tops] Task added: {task}")

    def execute_next(self):
        if self.task_queue:
            task = self.task_queue.pop(0)
            print(f"[Tops] Executing task: {task}")
            # Placeholder: trigger agent logic here
        else:
            print("[Tops] No tasks to execute.")
