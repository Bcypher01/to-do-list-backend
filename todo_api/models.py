from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class ToDo(models.Model):
    name = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    progress = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    due_date = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return self.name
        