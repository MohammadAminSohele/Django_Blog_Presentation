from django.db import models

from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse

from account.models import User
from extentions.utils import JalaliConverter

class CatagoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

# Create your models here.
class Catagory(models.Model):
    parent=models.ForeignKey('self',default=None,blank=True,null=True,on_delete=models.CASCADE,related_name='children',verbose_name='زیر دسته')
    title=models.CharField(max_length=100,verbose_name='عنوان')
    slug=models.SlugField(max_length=50,verbose_name='عنوان در url')
    status=models.BooleanField(default=True,verbose_name='فعال/غیرفعال')
    position=models.IntegerField(default=1,verbose_name='اولویت')

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
        ordering=['parent__id','position']

    def __str__(self):
        return self.title
    
    objects=CatagoryManager()
class Article(models.Model):
    STATUS_CHOICES=(
        ('p','پابلیش'),
        ('d','پیش نویس')
    )
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='articles',verbose_name='نویسنده')
    title=models.CharField(max_length=100,verbose_name='عنوان')
    slug=models.SlugField(max_length=50,verbose_name='عنوان در url')
    cataogry= models.ManyToManyField(Catagory,verbose_name='دسته بندی',related_name='articles')
    description=models.TextField(verbose_name='توضیحات')
    images=models.ImageField(upload_to='images',verbose_name='عکس')
    published=models.DateTimeField(default=timezone.now,verbose_name='تاریخ انتشار')
    created=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ساخت')
    updated=models.DateTimeField(auto_now=True,verbose_name='تاریخ ویرایش')
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name='حالت')

    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقالات'
        ordering=['-published']    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('account:home')
    
    def Jpublish(self):
        return JalaliConverter(self.published)
    
    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.images.url))
    thumbnail_tag.short_description='عکس'

    def category_to_str(self):
        return "، ".join([cataogry.title for cataogry in self.cataogry.active()])
    category_to_str.short_description = "دسته‌بندی"
    
    objects=ArticleManager()
    