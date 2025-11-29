from django.db import models


class Task(models.Model):
    """
    Represents a unit of work that can be prioritized by the Smart Task Analyzer.
    """

    title = models.CharField(max_length=200)
    due_date = models.DateField()
    importance = models.IntegerField(default=5)  # Scale 1-10
    estimated_hours = models.IntegerField(default=1)

    # Simple JSON field to store dependency IDs, e.g. [1, 2, 3]
    dependencies = models.JSONField(default=list, blank=True)

    def __str__(self) -> str:
        return self.title
