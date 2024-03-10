"""Определяет схемы Url для blogs"""

from django.urls import path
from . import views


app_name = 'blogs'

urlpatterns = [
    # Домашняя страница
    path('', views.feed, name='feed'),
    # Комментарии под каждым постом
    path('post/<int:post_id>/', views.post, name='post'),
    # Страница для создания нового поста
    path('new_post/', views.new_post, name='new_post'),
    # Страница для создания комментария
    path('new_comment/<int:post_id>/', views.new_comment, name='new_comment'),
    # Страница для редактирования поста
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    # Страница для редактирования комментария
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment')
]

