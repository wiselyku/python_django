from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class ToDoList(models.Model):
    taskName = models.CharField(max_length=300)
    createdDatetime = models.DateTimeField("task created datetime")
    finishedDatetime = models.DateTimeField(null=True)
    taskDone = models.BooleanField(default=False)
    taskContent = models.TextField(null=True)

    def __str__(self):
        datetime = timezone.localtime(self.createdDatetime)
        return f"'{self.taskName}' is created at {createdDatetime.strftime('%A, %d %B, %Y at %X')}"