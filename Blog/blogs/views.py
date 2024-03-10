from django.shortcuts import render, redirect

from .models import Post, Comment
from .forms import PostForm, CommentForm


def feed(request):
    """Домашняя страница"""
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/feed.html', context)


def post(request, post_id):
    """Страница c постом и комментами к нему"""
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.order_by('date_added')
    context = {'post': post, 'comments': comments}
    return render(request, 'blogs/post.html', context)


def new_post(request):
    """Создание нового поста"""
    if request.method != 'POST':
        # Данные не отправились; создается пустая форма
        form = PostForm()
    else:
        # Отправлены данные POST; обработать данные
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:feed')

    # Вывести пустую или недейственную форму
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def new_comment(request, post_id):
    """Добавляет новый комментарий к записи"""
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        # Если данные на отправлялись
        form = CommentForm()
    else:
        # Данные отправлялись; обработать данные
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('blogs:post', post_id=post_id)

    # Вывести пустую или недействительную форму
    context = {'post': post, 'form': form}
    return render(request, 'blogs/new_comment.html', context)


def edit_post(request, post_id):
    """Редактирует существующий пост"""
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        # Исходный запрос; Форма заполняется данными текущей записи
        form = PostForm(instance=post)
    else:
        # Отправка данных POST; обработать данные
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post_id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

def edit_comment(request, comment_id):
    """Редактирует существующий комментарий"""
    comment = Comment.objects.get(id=comment_id)
    post = comment.post

    if request.method != 'POST':
        # Исходный запрос; форма заполняется текущими данными
        form = CommentForm(instance=comment)
    else:
        # Отправда данных POST; обработать данные
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)

    context = {'comment': comment, "post": post, 'form': form}
    return render(request, 'blogs/edit_comment.html', context)
