# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Article(models.Model): # создание таблицы
    class Meta():
        db_table = u"Темы" # называем таблицу
        verbose_name = u'Темы'
    "создаем столбцы таблицы:"
    article_title = models.CharField(u'Название темы',max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)

class Comments(models.Model):
    class Meta():
        db_table = "comments"
    comments_text = models.TextField(verbose_name=u'Текст комментария', max_length=50)
    comments_article = models.ForeignKey(Article)

