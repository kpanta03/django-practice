from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Recipe)
# ORM ko
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
# Report cart ko models
admin.site.register(Subject)
# admin mai report dekhauna ko lagi
class SubjectMarkAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']#list_display lai overwrite gareko
# admin.site.register(SubjectMarks)#mathi ko class xaina vani simply yesto natra muniko
admin.site.register(SubjectMarks,SubjectMarkAdmin)

