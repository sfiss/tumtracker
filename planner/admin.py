from django.contrib import admin
from django import forms

# Register your models here.
from planner.models import Subject


class SubjectAdminForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = ['name', 'ects', 'sem_taken', 'area']
		#widgets = {
		#	'sem_taken': forms.Select(choices=[
		#		('','---'), ('WS2015','WS 2015'),('SS2016','SS 2016'),('WS2016','WS 2016'),('SS2017','SS 2017')]),
		#}


class SubjectAdmin(admin.ModelAdmin):
	form = SubjectAdminForm


admin.site.register(Subject, SubjectAdmin)
