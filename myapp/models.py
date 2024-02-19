from django.db import models

# Create your models here.
class Project(models.Model): 
    name = models.CharField(max_length=200)

    #? Es como el toString
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #? Eliminación en cascada, cuando hay relación
    done = models.BooleanField(default=False)

    #? self es una referencia al la misma clase
    def __str__(self):
        return self.title + ' - ' + self.project.name