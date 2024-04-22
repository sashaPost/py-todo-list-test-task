from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tags')

    class Meta:
        ordering = ["is_done", "created_at"]