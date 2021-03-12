from django.contrib import admin
from .models import Article, Category
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('crated_at', 'updated_at')
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)