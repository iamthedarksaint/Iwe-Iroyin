from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on', )
    list_filter = ("status",)
    search_fields = ['title', 'body']

admin.site.register(Article, ArticleAdmin)
