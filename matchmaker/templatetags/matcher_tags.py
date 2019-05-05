import datetime
from django import template
from django.conf import settings

register = template.Library()

# @register.filter
# def settingVariable(var):
# 	val = getattr(var, settings)
# 	if val:
# 		return val
# 	else:
# 		return False

@register.simple_tag
def use_cdn():
	print('cdn config is', settings.USE_CDN)
	return settings.USE_CDN
	# return  getattr(var, settings)