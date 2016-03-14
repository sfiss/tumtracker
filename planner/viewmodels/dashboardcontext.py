from django.utils import timezone

class DashboardContext(object):
	subject_list = []

	def __init__(self,subject_list = []):
		self.subject_list = subject_list

	def subjects_all(self):
		return self.subject_list

	def subjects_taken(self):
		return filter(lambda subject: subject.sem_taken and subject.sem_taken_date <= timezone.now(), self.subject_list)

	def subjects_planned(self):
		return filter(lambda subject: subject.sem_taken and subject.sem_taken_date > timezone.now(), self.subject_list)

	def subjects_watching(self):
		return filter(lambda subject: not subject.sem_taken or subject.sem_taken.isspace(), self.subject_list)

