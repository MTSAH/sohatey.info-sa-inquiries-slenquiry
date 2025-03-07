from django.db import models

class Inquiry(models.Model):
    service_code = models.CharField(max_length=20, verbose_name="رمز الخدمة")
    patient_id = models.CharField(max_length=20, verbose_name="رقم الهوية / الإقامة")
    patient_name = models.CharField(max_length=100, verbose_name="اسم المريض")
    sick_leave_date = models.DateField(verbose_name="تاريخ إصدار الإجازة")
    duration = models.IntegerField(verbose_name="مدة الإجازة بالأيام")
    date_from = models.DateField(verbose_name="تبدأ من")
    date_to = models.DateField(verbose_name="تنتهي في")
    doctor_name = models.CharField(max_length=100, verbose_name="اسم الطبيب")
    job_title = models.CharField(max_length=100, verbose_name="المسمى الوظيفي")

    def __str__(self):
        return f"{self.patient_name} - {self.service_code}"
