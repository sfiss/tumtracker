from django.db import models
from django.utils import timezone

from enum import Enum, unique
from datetime import datetime
from dateutil.relativedelta import relativedelta

@unique
class SpecializationArea(Enum):
	software_engineering = 'SE'
	databases_and_information_systems = 'DBI'
	artificial_intelligence_and_robotics = 'AIR'
	computer_graphics_and_vision = 'CGV'
	computer_architecture = 'CA'
	distributed_systems_networks_and_security = 'DNS'
	formal_methods_and_applications = 'FMA'
	algorithms_and_scientific_computing = 'ASC'
	orientation = 'OR'
	interdisciplinary_project = 'IDP'
	support_electives = 'SUPP'
	master_seminar = 'SEM'
	master_practical = 'PRAC'


# Create your models here.
class Subject(models.Model):
	# fields
	name = models.CharField(max_length=200)
	ects = models.IntegerField()
	sem_taken = models.CharField(max_length=6,blank=True,choices=[
				('','---'), ('WS2015','WS 2015'),('SS2016','SS 2016'),('WS2016','WS 2016'),('SS2017','SS 2017')])
	area = models.CharField(max_length=4, choices=[(member.value,name + ' (' + member.value + ')') for name, member in SpecializationArea.__members__.items()])

	def __str__(self):
		return self.name.capitalize()

	@property
	def sem_taken_date(self):
		'''
		Parses the Date as: Year plus 4 Months offset for summer, 10 Months offset for winter
		'''
		sem_date =  datetime.strptime(self.sem_taken[2:], "%Y")
		offset = 4 if self.sem_taken[:2] == 'SS' else 10
		return timezone.get_current_timezone().localize(sem_date + relativedelta(months=offset))





