from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Пост, который будет отображаться в ленте"""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text[:200]}...' if len(self.text) > 200 else self.text

class Comment(models.Model):
    """Комментарий под постом"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.text[:50]}...'