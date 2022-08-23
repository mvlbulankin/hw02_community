from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group


def index(request):
    template = "posts/index.html"
    title = "Последние обновления на сайте"
    posts = Post.objects.order_by("-pub_date")[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        "posts": posts,
        "title": title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    # return HttpResponse(f'Мороженое номер {slug}')
    # template = 'group/<slug:slug>/'
    # title = 'Здесь будет информация о группах проекта Yatube'
    # context = {
    #     'title': title,
    # }
    # return render(request, template, context)
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    template = "posts/group_list.html"
    title = "Записи сообщества"
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:10]
    context = {
        "group": group,
        "posts": posts,
        "title": title,
    }
    return render(request, template, context)
