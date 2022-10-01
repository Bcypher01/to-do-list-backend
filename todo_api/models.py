from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class ToDo(models.Model):
    name = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', 'created']
    
    def __str__(self):
        return self.name
        