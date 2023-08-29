from django.contrib.auth import get_user_model
from django.db import models

from .max_length import MAX_LEGTH

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name="Текст",
        help_text='Введите текст поста')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Дата публикации")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts', verbose_name="Автор"
    )
    group = models.ForeignKey('Group',
                              on_delete=models.SET_NULL,
                              blank=True, null=True,
                              related_name='posts',
                              max_length=MAX_LEGTH, verbose_name="Группа",
                              help_text=(
                                  'Группа, к которой будет относиться пост'))

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ('-pub_date',)

    def __str__(self):
        return str(self.text)


class Group(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    description = models.TextField(
        verbose_name="Описание",
        help_text='Введите текст поста')

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
