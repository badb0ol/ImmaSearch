from django.db import models

# Import modules to shell when editing with: from amazonSearch.models import Item, ToDoList
# ID index starts at 1

# Create your models here.
class ToDoList(models.Model): # adding a database object and attributing entries for each model
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    #each todolist is equipped with a set of items

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
