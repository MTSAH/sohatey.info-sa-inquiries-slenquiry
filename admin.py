from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("service_code", "patient_name", "sick_leave_date", "doctor_name", "duration")
    search_fields = ("service_code", "patient_id", "patient_name")

admin.site.site_header = "لوحة إدارة الاستعلامات"
