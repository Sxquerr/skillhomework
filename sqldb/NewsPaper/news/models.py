from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique= True)

news = 'Новости'
artical = 'Статья'


POSITIONS = [
    (news, 'Новости'),
    (artical, 'Статья')
 ]


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    news = models.CharField(max_length=8, choices= POSITIONS, default=news)
    time = models.DateTimeField(auto_now_add = True)
    theme = models.CharField(max_length=255, default='Статья без заголовка!')
    text = models.TextField(default='Ничего не указано')
    rating = models.IntegerField(default=0)
    Posts = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating + 1

    def dislike(self):
        self.rating - 1

    def preview(self):
        print(self.text[0:123], '...')

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    time = models.DateField(auto_now_add= True)
    rating = models.IntegerField(default=0)
    
    def like(self):
        self.rating + 1

    def dislike(self):
        self.rating - 1
     