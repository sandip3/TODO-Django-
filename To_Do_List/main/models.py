from django.db import models

# Create your models here.


class To_do(models.Model):

    todo_title = models.TextField(null= True)
    todo_task = models.TextField(null= True)

    def __str__(self):
        return self.todo_title
