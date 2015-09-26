# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from django.db import models


class Imageline(admin.StackedInline):
    model = Image
    extra = 1

class Videoline(admin.StackedInline):
    model = Video
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug', 'published', 'ordering', 'parent')
    list_editable = ( 'slug', 'published', 'ordering')
    list_filter = ('parent', 'published')

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug', 'show', 'published', 'ordering')
    list_editable = ( 'slug', 'show', 'published', 'ordering')
    inlines = [Imageline, Videoline,]
    search_fields = ['name', 'slug']
    list_filter = ('category', 'published')
    # class Media:
    # 		js = ('/static/js/nicEdit.js', '/static/js/textarea_content.js')
		

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        user = request.user
        qs = qs.filter(user=user)
        return qs

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if request.user.is_superuser:
            pass
        else:
            self.readonly_fields = ('comments_count','raiting','count_view', 'reit', 'count_votes')
            self.exclude.append('user', )
        return super(PostAdmin, self).get_form(request, obj, **kwargs)
        
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        
        user = request.user
        if not instance.user:
            instance.user = user
                
        instance.save()
        return instance
        

class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    
class GaleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug', 'published', 'ordering', 'parent')
    list_editable = ( 'slug', 'published', 'ordering')
    list_filter = ('parent', 'published')
    inlines = [Imageline,]


class MediaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug', 'published', 'ordering', 'parent')
    list_editable = ( 'slug', 'published', 'ordering')
    list_filter = ('parent', 'published')
    inlines = [Videoline,]

   
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Galery, GaleryAdmin)
admin.site.register(Media, MediaAdmin)