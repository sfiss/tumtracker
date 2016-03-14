from itertools import zip_longest

from django.utils import timezone

class DashboardContext(object):
	subject_list = []

	def __init__(self,subject_list = []):
		self.subject_list = subject_list

	def subjects_all(self):
		return self.subject_list

	def combined_subject_list(self):
		return zip_longest(self.subjects_taken, self.subjects_planned, self.subjects_watching)
		#return zip_longest([], self.subjects_planned(), [22,33,])

	@property
	def subjects_taken(self):
		return list(filter(lambda subject: subject.sem_taken and subject.sem_taken_date <= timezone.now(), self.subject_list))

	@property
	def subjects_planned(self):
		return list(filter(lambda subject: subject.sem_taken and subject.sem_taken_date > timezone.now(), self.subject_list))

	@property
	def subjects_watching(self):
		return list(filter(lambda subject: not subject.sem_taken or subject.sem_taken.isspace(), self.subject_list))

