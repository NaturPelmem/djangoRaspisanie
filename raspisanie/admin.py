from django.contrib import admin
from .models import Prepod, Group, Cabinet, TimeTable


@admin.register(TimeTable)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['number', 'prepod', 'date', 'group', 'cabinet', 'reduction']
    list_editable = ['prepod', 'date', 'group', 'cabinet', 'reduction']
    ordering = ['prepod', 'date', 'number']
    search_fields = ['prepod__full_name', 'date']
    list_filter = ['date', 'prepod__full_name']
    save_as_continue = True
    save_as = True
    # fields = (('number', 'prepod', 'group', 'cabinet'), ('date', 'reduction'))


@admin.register(Prepod)
class PrepodAdmin(admin.ModelAdmin):
    search_fields = ['full_name__startswith']
    ordering = ['full_name']


@admin.register(Group)
class PrepodAdmin(admin.ModelAdmin):
    search_fields = ['group_name__startswith']
    ordering = ['group_name']


@admin.register(Cabinet)
class PrepodAdmin(admin.ModelAdmin):
    search_fields = ['cabinet_name__startswith']
    ordering = ['cabinet_name']
