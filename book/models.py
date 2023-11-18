from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Book(models.Model):
    author=models.ForeignKey(User,related_name='book_author',on_delete=models.CASCADE)    
   
    name=models.CharField(max_length=100)
    publish_date=models.DateTimeField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=100)
    birthdate_date=models.DateTimeField()
    biography=models.TextField(max_length=20000)

class Review(models.Model):
    book=models.ForeignKey(Book,related_name='Review_book',on_delete=models.CASCADE)    
   
    Reviewer_name=models.CharField(max_length=100)
    content=models.TextField(max_length=20000)  
