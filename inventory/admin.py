# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display = ['title', 'amount']

admin.site.register(Item, ItemAdmin)
