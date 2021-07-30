from django.contrib import admin
from .models import m_SprMenu, m_Category, m_Trening


class mMenu(admin.ModelAdmin):
    list_display = ['order', 'title', 'icons', 'cansw', 'links']
    ordering = ('order',)
    search_fields = ('title',)


class mCategory(admin.ModelAdmin):
    list_display = ['order', 'name', 'image', 'cansw', 'slug']
    ordering = ('order',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}



class mTrening(admin.ModelAdmin):
    list_display = ['order', 'name', 'image', 'cansw', 'slug']
    ordering = ('order',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(m_Category, mCategory)
admin.site.register(m_SprMenu, mMenu)
admin.site.register(m_Trening, mTrening)
