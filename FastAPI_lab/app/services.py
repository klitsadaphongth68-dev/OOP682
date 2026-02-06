from fastapi import HTTPException
from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        # Business logic could go here
        return self.repo.create(task_in)
    
    def update_task(self, task_id: int):
        # Business logic could go here
        return self.repo.update(task_id)
    
    def get_by_title(self, title: str):
        tasks = self.repo.get_all()
        return [task for task in tasks if task.title == title]