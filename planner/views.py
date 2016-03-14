from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from .viewmodels.dashboardcontext import DashboardContext
from .models import Subject


# Create your views here.
def dashboard(request):
	ctx = dict(context=DashboardContext(subject_list=Subject.objects.all()))
	return render(request, 'planner/dashboard.html', ctx)

class SubjectView(generic.DetailView):
	model = Subject
	template_name = 'planner/subject.html'
	context_object_name = 'context'

	def get(self, request, *args, **kwargs):
		"""
        Instead of 404, create new object iff pk=0
        """
		try:
			self.object = self.get_object()
		except Http404:
			self.object = Subject
		context = self.get_context_data(object=self.object)
		return self.render_to_response(context)