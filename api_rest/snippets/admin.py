# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from snippets.models import Snippet, Post, Comment, Category

# Register your models here.
admin.site.register(Snippet)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)