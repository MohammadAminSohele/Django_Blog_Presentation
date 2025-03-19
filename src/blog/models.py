from django.db import models

from django.utils import timezone

from account.models import User

# Create your models here.
class Catagory(models.Model):
    parent=models.ForeignKey('self',default=None,blank=True,null=True,on_delete=models.CASCADE,related_name='children',verbose_name='زیر دسته')
    title=models.CharField(max_length=100,verbose_name='عنوان')
    slug=models.SlugField(max_length=50,verbose_name='عنوان در url')
    status=models.BooleanField(default=True,verbose_name='فعال/غیرفعال')
    position=models.IntegerField(default=1,verbose_name='اولویت')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
        ordering=['parent__id','position']
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

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقالات'
        ordering=['-published']
        