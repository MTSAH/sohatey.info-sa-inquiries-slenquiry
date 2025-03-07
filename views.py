from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Inquiry
from datetime import datetime
from django.http import HttpResponseRedirect


def slenquiry(request):
     return render(request, 'inquiries/slenquiry.html')
@csrf_exempt
def add_inquiry(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            inquiry = Inquiry.objects.create(
                service_code=data.get('service_code'),
                patient_id=data.get('patient_id'),
                patient_name=data.get('patient_name'),
                sick_leave_date=datetime.strptime(data.get('sick_leave_date'), "%Y-%m-%d").date(),
                duration=int(data.get('duration')),
                date_from=datetime.strptime(data.get('date_from'), "%Y-%m-%d").date(),
                date_to=datetime.strptime(data.get('date_to'), "%Y-%m-%d").date(),
                doctor_name=data.get('doctor_name'),
                job_title=data.get('job_title'),
            )
            return JsonResponse({"message": "تمت إضافة البيانات بنجاح", "id": inquiry.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "يجب إرسال الطلب عبر POST"}, status=400)
@csrf_exempt
def get_inquiry(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            service_code = data.get('service_code')
            patient_id = data.get('patient_id')

            inquiry = Inquiry.objects.filter(service_code=service_code, patient_id=patient_id).first()

            if inquiry:
                return JsonResponse({
                    "patient_name": inquiry.patient_name,
                    "sick_leave_date": inquiry.sick_leave_date.strftime("%Y-%m-%d"),
                    "duration": inquiry.duration,
                    "date_from": inquiry.date_from.strftime("%Y-%m-%d"),
                    "date_to": inquiry.date_to.strftime("%Y-%m-%d"),
                    "doctor_name": inquiry.doctor_name,
                    "job_title": inquiry.job_title
                })
            else:
                return JsonResponse({"message": "error"})  # لا يوجد نتائج
            
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "يجب إرسال الطلب عبر POST"}, status=400)
# Create your views here.
