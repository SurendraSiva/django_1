from django.db import models
class Note(models.Model):
    title=models.CharField(max_length=300,default='Defalt Title')
    content=models.CharField(max_length=1000)





