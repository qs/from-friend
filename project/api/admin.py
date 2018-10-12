from django.contrib import admin
from .models import Category, Subscription


@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscription)
class AuthorAdmin(admin.ModelAdmin):
    pass
