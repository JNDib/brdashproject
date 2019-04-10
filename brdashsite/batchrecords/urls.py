from django.urls import include, path

from .views import BatchRecordListView, BatchRecordCreateView, BatchRecordChangeStatusView, BatchRecordDetailView, BatchRecordHistoryView, some_view

app_name = 'batchrecords'
urlpatterns = [
    path('', BatchRecordListView.as_view(), name='home'),
	path('create/', BatchRecordCreateView.as_view(), name='create'),
	path('changestatus/<int:pk>/', BatchRecordChangeStatusView.as_view(), name='changestatus'),
	path('detail/<int:pk>/', BatchRecordDetailView.as_view(), name='detail'),
	path('history/<int:pk>/', BatchRecordHistoryView.as_view(), name='history'),
	path('pdf/', some_view, name='pdfview'),
]