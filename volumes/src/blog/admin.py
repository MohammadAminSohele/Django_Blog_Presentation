from django.contrib import admin

from .import models

# Register your models here.

def make_published(modeladmin, request, queryset):
    row_updated=queryset.update(status="p")
    if row_updated==1:
        message_bit='منتشر شد'
    else:
        message_bit='منتشر شدند'
    modeladmin.message_user(request,"{} مقاله {}".format(row_updated,message_bit))
make_published.short_description ="مقالات انتخاب شده انتشار شد"

def make_draft(modeladmin, request, queryset):
    row_updated=queryset.update(status="d")
    if row_updated==1:
        message_bit='پیش نویس شد'
    else:
        message_bit='پیش نویس شدند'
    modeladmin.message_user(request,"{} مقاله {}".format(row_updated,message_bit))
make_draft.short_description ="مقالات انتخاب شده پیش نویس شد"

class ArticleManager(admin.ModelAdmin):
    list_display = ('title','slug','is_special','status','author','Jpublish','thumbnail_tag')
    list_filter = ('published','status','author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-published']
    actions=[make_published,make_draft]

class CatagoryManager(admin.ModelAdmin):
    list_display = ('position', 'title','slug', 'parent','status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Article,ArticleManager)
admin.site.register(models.Catagory,CatagoryManager)
admin.site.register(models.IP_Address)
