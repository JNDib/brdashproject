from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from .models import BatchRecord, BatchRecordHistory
from .forms import BatchRecordCreateForm, BatchRecordChangeStatusForm
from .utils import render_to_pdf


class BatchRecordListView(ListView):
	model = BatchRecord
	context_object_name = 'batch_records'
	template_name = "batchrecords/br_list.html"
	
	# def get_context_data(self, **kwargs):
		# context = super(ListView, self).get_context_data(**kwargs)
		# context['batch_records'] = BatchRecord.objects.all()
		# context['batch_records_history'] = BatchRecordHistory.objects.all()


@method_decorator(login_required, name='dispatch')
class BatchRecordCreateView(CreateView):
	form_class = BatchRecordCreateForm
	success_url = reverse_lazy('batchrecords:home')
	template_name = "batchrecords/br_create_form.html"
	
	def form_valid(self, form):
		user = self.request.user
		form.instance.created_by = user # sets to user when new br is created
		form.instance.updated_by = user # sets to user when new br is created
		return super().form_valid(form)

	
@method_decorator(login_required, name='dispatch')
class BatchRecordChangeStatusView(UpdateView):
	model = BatchRecord
	form_class = BatchRecordChangeStatusForm
	success_url = reverse_lazy('batchrecords:home')
	template_name = "batchrecords/br_update_form.html"

	def form_valid(self, form):
		object_id = form.instance.pk
		object = BatchRecord.objects.get(pk=object_id)
		user = self.request.user
		form.instance.updated_at = timezone.now()
		form.instance.updated_by = user # sets to user when new br is created
		form.instance.status_changes += 1
		BatchRecord.log_batch_record_history(object, form.data.get('current_status'), form.instance.updated_at)
		return super().form_valid(form)

		
class BatchRecordHistoryView(DetailView):
	model = BatchRecord
	template_name = "batchrecords/br_history.html"
		
		
# class BatchRecordHistoryView(ListView):
	# model = BatchRecordHistory
	# template_name = "batchrecords/br_history.html"
	
	# def get_queryset(self):
		# return BatchRecordHistory.objects.filter(batchrecord=self.kwargs['pk'])


class BatchRecordDetailView(DetailView):
	model = BatchRecord

def some_view(request):
	results = ["testing pdf",]
	return render_to_pdf(
		'batchrecords/mytemplate.html',
		{
			'pagesize':'A4',
			'mylist': results,
		}
	)	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
