from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=123)
    image = models.ImageField(upload_to='article/author/')
    bio = RichTextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=123)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    image = models.ImageField(upload_to='article/')
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Content(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='contents')
    content = RichTextField()
    checkbox = models.BooleanField(default=False)


class Comment(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='parent', null=True, blank=True)
    top_comment = models.IntegerField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    name = models.CharField(max_length=123)
    email = models.EmailField()
    message = models.TextField()
    website = models.URLField()
    image = models.ImageField(upload_to='article/comment', null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)


def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name + "-" + str(timezone.now().date()))


def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent:
        parent = instance.parent
        if parent.top_comment:
            instance.top_comment = parent.top_comment.id
        else:
            instance.top_comment = parent.id


def children(sender, instance, *args, **kwargs):
    if not instance.top_comment:
        children_1 = Comment.objects.filter(top_comment=instance.id)
        return children_1
    else:
        return None


pre_save.connect(article_pre_save, sender=Article)
