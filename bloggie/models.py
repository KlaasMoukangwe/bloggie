from datetime import datetime
from turtle import title
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

#category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField((""), unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

# Post model 
class Post(models.Model):
    title = models.CharField(('Post Title'), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    date_published = models.DateTimeField(auto_now= True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete= models.CASCADE,)
    content = RichTextField()
    image = models.ImageField(('Featured Image'), upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_published']
        verbose_name_plural = "posts"   


# Comment Model
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    reply = models.TextField()
    comment_date = models.DateTimeField(datetime.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.reply

    class Meta:
        verbose_name_plural = "comments"
        ordering = ['comment_date']
