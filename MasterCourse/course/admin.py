from django.contrib import admin

from .models import Data


class CourseAdmin(admin.ModelAdmin):
    fields = ['id', 'name','field','organization','properties','classification','duration','point','teacher','session','area']
    list_display = ('id','name','organization', 'teacher', 'area')
#     ,'class_field','organization','properties','classification','period','point','teacher','schedule','area'



admin.site.register(Data, CourseAdmin)