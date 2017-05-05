# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#import for http response
from django.http import HttpResponse

def index(request):
	return HttpResponse('<p>In index view</p>')

def item_detail(request,id):
	return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id))
