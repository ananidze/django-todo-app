from datetime import datetime

from django.db import models


class Todo(models.Model):
    title: str = models.CharField(max_length=80)
    is_completed: bool = models.BooleanField(default=False)
    created_at: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
