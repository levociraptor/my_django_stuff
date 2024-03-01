from django.db import models

class Post(models.Model):
    """Пост, который будет отображаться в ленте"""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text[:50]}...'

class Comment(models.Model):
    """Комментарий под постом"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.text[:50]}...'