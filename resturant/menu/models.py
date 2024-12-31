from django.db import models

class Menu(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to="images",blank=True,null=True)


    def __str__(self):
        return self.name
