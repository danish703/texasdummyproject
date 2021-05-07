from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'



class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    postedDate = models.DateField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

