# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from . import views
from .models import PlaceholderOperation


@admin.register(PlaceholderOperation)
class PlaceholderOperationAdmin(admin.ModelAdmin):

    def get_model_perms(self, request):
        return {}

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):
        # This sucks but its our only way to register the internal
        # undo/redo urls without asking users to configure them
        urlpatterns = [
            url(r'^undo/$', views.undo, name='djangocms_history_undo'),
            url(r'^redo/$', views.redo, name='djangocms_history_redo'),
        ]
        return urlpatterns
