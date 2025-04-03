from django import template

from ..models import Catagory

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگویی"

@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
        'catagory':Catagory.objects.filter(status=True)
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