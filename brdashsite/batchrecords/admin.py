from django.contrib import admin

from .models import Product, BatchRecord


class ProductAdmin(admin.ModelAdmin):
	fields = ['family', 'id', 'description', 'total_target_time']
	
	
class BatchRecordAdmin(admin.ModelAdmin):
	readonly_fields = ['created_at', 'updated_at']
	date_hierarchy = 'created_at'
	list_display = ('pk', 'workorder', 'product', 'lot', 'manufacture_date', 'expiration_date', 'current_status')
	list_filter = ['manufacture_date', 'current_status']
	
	fieldsets = (
		(None, {
			'fields': ['workorder', 'product', 'lot', 'manufacture_date', 'expiration_date', 'current_status']
		}),
		('Advanced options', {
			'classes': ('collapse',),
			'fields': ['created_by', 'created_at', 'updated_by', 'updated_at', 'status_changes']
		}),
	)

# admin.site.register(Product, SimpleHistoryAdmin)
# admin.site.register(BatchRecord, SimpleHistoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BatchRecord, BatchRecordAdmin)