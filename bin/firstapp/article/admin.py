from django.contrib import admin
from article.models import Article, Comments
# Register your models here.


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleInline]
    list_filter = ['article_date']

"""Регистрируем модель Article и говорим, что ArticleAdmin отвечает за её настройку"""
admin.site.register(Article, ArticleAdmin)
