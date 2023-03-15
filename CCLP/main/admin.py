from django.contrib import admin
from .models import Student, Class, Person


# Register your models here.
admin.site.register(Student)
admin.site.register(Class)


class PersonAdmin(admin.ModelAdmin):
	list_display = ('student', 'section', 'teacher', 'points', 'description')

admin.site.register(Person, PersonAdmin)
