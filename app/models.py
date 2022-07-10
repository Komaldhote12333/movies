from django.db import models

# Create your models heretype  
 
 
class Category(models.Model):
    NAM = models.CharField(max_length=2336)
    def __str__(self):
        return self.NAM
    
    
    
class Movie(models.Model):
    name = models.CharField(max_length=53)
    moviesimagelink = models.TextField()
    downloadlink = models.CharField(max_length=9) 
    movitype = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    
    
class Team(models.Model):
    image =  models.ImageField(upload_to ="komal")   
    link = models.CharField(max_length=355555555555)
    