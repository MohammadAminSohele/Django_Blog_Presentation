from django import template

from django.db.models import Q , Count
from datetime import timedelta , datetime
from django.contrib.contenttypes.models import ContentType

from ..models import Catagory , Article

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگویی"

@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
        'catagory':Catagory.objects.filter(status=True)
    }

@register.inclusion_tag("blog/partials/slidebar.html")
def popular_articles():
    last_month = datetime.today() - timedelta(30)
    return {
        'articles':Article.objects.published().annotate(count=Count('hits'),filter=Q(article_hits__created__gt=last_month)).order_by('-count','-published')[:5], # gt : grater thann
        'title' : 'مقالات پربازدید ماه'
    }

@register.inclusion_tag("blog/partials/slidebar.html")
def hot_articles():
    last_month = datetime.today() - timedelta(30)
    content_type_id = ContentType.objects.get(app_label='blog', model='article').id
    return {
        'articles':Article.objects.published().annotate(count=Count('hits'),filter=Q(comments__posted__gt=last_month) and Q(comments__content_type__id = content_type_id)).order_by('-count','-published')[:5],
        'title' : 'مقالات داغ ماه'
    }    

@register.inclusion_tag("registration/partials/link.html")
def Link(request, link_name, content,classes):
	return {
		"request": request,
		"Link_name": link_name,
		"Link": "account:{}".format(link_name),
		"Content": content,
		"classes": classes,
	}