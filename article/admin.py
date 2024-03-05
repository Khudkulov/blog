from django.contrib import admin
from .models import Tag, Article, Category, Comment, Author, Content


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user',)


class ContentInline(admin.TabularInline):
    model = Content
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'created_date', 'category',)
    readonly_fields = ('created_date', 'slug', 'modified_date')
    search_fields = ('name',)
    date_hierarchy = 'created_date'
    list_filter = ('category', 'tags')
    filter_horizontal = ('tags',)
    save_on_top = True
    inlines = [ContentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'website', 'created_date')
    readonly_fields = ('created_date',)
    search_fields = ('name', 'article__name')
    date_hierarchy = 'created_date'

