# -*- coding: utf-8 -*-
from django.db import models
import random
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

def make_upload_path(instance, filename, prefix = False):
    # Переопределение имени загружаемого файла.
    n1 = random.randint(0,10000)
    n2 = random.randint(0,10000)
    n3 = random.randint(0,10000)
    c = filename.split(".")
    filename = str(n1)+"_"+str(n2)+"_"+str(n3) + '.' + c[-1]
    return u"%s/%s" % (settings.IMAGE_UPLOAD_DIR, filename)



class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True, unique=True, blank=True, default="", verbose_name="Название Категории")
    title = models.CharField(max_length=250, blank=True, verbose_name="Заголовок в браузере")
    metakey = models.CharField(max_length=250, blank=True, verbose_name="Ключевые слова")
    metadesc = models.CharField(max_length=250, blank=True, verbose_name="Мета описание")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="Родительская категория")
    published = models.BooleanField(verbose_name="Опубликован", default=0)
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    count_posts = models.IntegerField(verbose_name="Количество постов", default=0, blank=True, null=True)
    
    @property
    def name2(self):
        return self.name + self.title

    

    
    def get_url(self):
        return "/blog/%s/" % self.slug

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
        ordering = ['ordering']

class Tags(models.Model):
    name = models.CharField(max_length=250, db_index=True, unique=True, blank=False, verbose_name="Название тэга")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    
    published = models.BooleanField(verbose_name="Опубликован")
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    count_posts = models.IntegerField(verbose_name="Количество постов", default=0, blank=True, null=True)
    

    def get_url(self):
        return "/blog/tag/%s/" % self.slug

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Теги"
    
class Post(models.Model):
    NEW = 1
    ACTIVE = 2
    ARHIV = 3
    
    STATE_CHOICES = (
        (NEW, 'Новый'),
        (ACTIVE, 'Активный'),
        (ARHIV, 'Архив'),
        
    )
    name = models.CharField(max_length=250, verbose_name="Название RU")
    user = models.ForeignKey(User, blank=True, null=True, verbose_name=u"Пользователь")
    
    title = models.CharField(max_length=250, blank=True, verbose_name="Заголовок в браузере")
    
    metakey = models.CharField(max_length=250, blank=True, verbose_name="Ключевые слова")
    
    metadesc = models.CharField(max_length=250, blank=True, verbose_name="Мета описание")
    image = models.ImageField(upload_to=make_upload_path, blank=True,  verbose_name="Изображение")
    category = models.ForeignKey(Category, blank=True, related_name="c1", null=True, verbose_name="Категория")
    tags = models.ManyToManyField(Tags, related_name="c2", blank=True, verbose_name="Теги")
    state = models.IntegerField(verbose_name="Состояние", default=NEW, blank=True, null=True,choices=STATE_CHOICES)
    
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    short_text = models.TextField(blank=True, verbose_name="Короткое описание RU")
    short_text_en = models.TextField(blank=True, verbose_name="Короткое описание EN")
    video = models.CharField(max_length=250, blank=True, verbose_name="Видео id в кратком описании")
    full_text = models.TextField(blank=True, verbose_name="Полное описание RU")
    full_text_en = models.TextField(blank=True, verbose_name="Полное описание EN")
    date = models.DateField(auto_now_add=True,  blank=True, verbose_name="Дата публикации")
    published = models.BooleanField(verbose_name="Опубликован")
    show = models.BooleanField(verbose_name="Всегда вверху")
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    comments_count = models.IntegerField(verbose_name="Количество коментариев", default=0, blank=True, null=True)
    raiting =  models.DecimalField(max_digits=3, decimal_places=2, default=0.00, verbose_name="Рейтинг")
    count_view = models.IntegerField(verbose_name="Количество просмотров", default=0, blank=True, null=True)
    reit = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Рейтинг", blank=True, null=True, default=0.0)
    count_votes = models.IntegerField(verbose_name="Количество голосов", blank=True, null=True, default=0)
    

    def get_url(self):
        return "/blog/%s/%s/" % (self.category.slug, self.slug)
    
    def save(self):
        super(Post, self).save()
        c = Post.objects.filter(category=self.category, published=1).count()
        self.category.count_posts = c
        self.category.save()
        tags = self.tags.all()
        for t in tags:
            t.count_posts = Post.objects.filter(tags=t, published=1).count()
            t.save()

        

    def pic(self):
        if self.image:
            return u'<img src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'
    pic.short_description = u'Большая картинка'
    pic.allow_tags = True
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Посты"
        verbose_name = "Пост"




class Galery(models.Model):
    name = models.CharField(max_length=250, db_index=True, unique=True, blank=True, default="", verbose_name="Название Галереи")
    title = models.CharField(max_length=250, blank=True, verbose_name="Заголовок в браузере")
    image = models.ImageField(upload_to=make_upload_path, blank=True, default="",  verbose_name="Изображение")
    metakey = models.CharField(max_length=250, blank=True, verbose_name="Ключевые слова")
    metadesc = models.CharField(max_length=250, blank=True, verbose_name="Мета описание")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="Родительская категория")
    category = models.ForeignKey(Category, blank=True, related_name="c11", null=True, verbose_name="Категория")
    post = models.ForeignKey(Post, blank=True, related_name="c8", null=True, verbose_name="Статья")
    published = models.BooleanField(verbose_name="Опубликован", default=0)
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    count_posts = models.IntegerField(verbose_name="Количество постов", default=0, blank=True, null=True)
    
    @property
    def name2(self):
        return self.name + self.title

    

    
    def get_url(self):
        return "/galery/%s/" % self.slug

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Галереи"
        verbose_name = "Галерея"
        ordering = ['ordering']


class Image(models.Model):
    name = models.CharField(max_length=250, blank=True, default="", verbose_name="Название")
    image = models.ImageField(upload_to=make_upload_path, blank=True, default="",  verbose_name="Изображение")
    post = models.ForeignKey(Post, blank=True, related_name="c3", null=True, verbose_name="Пост")
    galery = models.ForeignKey(Galery, blank=True, related_name="c4", null=True, verbose_name="Галерея")

    def pic(self):
        if self.image:
            return u'<img src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'
    pic.short_description = u'Большая картинка'
    pic.allow_tags = True
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Изображения"
        verbose_name = "Изображение"



class Media(models.Model):
    name = models.CharField(max_length=250, db_index=True, unique=True, blank=True, default="", verbose_name="Название Видео")
    title = models.CharField(max_length=250, blank=True, verbose_name="Заголовок в браузере")
    image = models.ImageField(upload_to=make_upload_path, blank=True, default="",  verbose_name="Видео")
    metakey = models.CharField(max_length=250, blank=True, verbose_name="Ключевые слова")
    metadesc = models.CharField(max_length=250, blank=True, verbose_name="Мета описание")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="Родительская категория")
    published = models.BooleanField(verbose_name="Опубликован", default=0)
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    count_posts = models.IntegerField(verbose_name="Количество постов", default=0, blank=True, null=True)
    
    @property
    def name2(self):
        return self.name + self.title

    

    
    def get_url(self):
        return "/media/%s/" % self.slug

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Видеотеки"
        verbose_name = "Видеотека"
        ordering = ['ordering']


class Video(models.Model):
    name = models.CharField(max_length=250, blank=True, default="", verbose_name="Название")
    video = models.FileField(upload_to=make_upload_path, blank=True, default="",  verbose_name="Видео")
    preview = models.ImageField(upload_to=make_upload_path, blank=True, default="",  verbose_name="Изображение видео")
    post = models.ForeignKey(Post, blank=True, related_name="c5", null=True, verbose_name="Пост")
    media = models.ForeignKey(Media, blank=True, related_name="c6", null=True, verbose_name="Галерея")

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Видео"
        verbose_name = "Видео"


