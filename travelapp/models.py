from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    package=models.FloatField()
    descr=models.TextField()
   


    def __str__(self):
        return self.name