var resultsDiv = document.getElementById('resultsDiv'); // عرض النتائج
var submit = document.getElementById('submit'); // زر الاستعلام
var toggleButton = document.getElementById('toggleButton'); // زر إعادة الاستعلام
var alerterror = document.getElementById('alerterror'); // رسالة الخطأ لا يوجد نتائج
var alerterror2 = document.getElementById('alerterror2'); // رسالة خطأ أخرى

function convertDate(dateString) {
    var arabicNumbers = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩'];
    var englishNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    var convertedDateString = "";

    for (var i = 0; i < dateString.length; i++) {
        var char = dateString[i];
        var index = arabicNumbers.indexOf(char);
        if (index !== -1) {
            char = englishNumbers[index];
        }
        convertedDateString += char;
    }

    var dateParts = convertedDateString.split("-");
    if (dateParts.length === 3) {
        convertedDateString = dateParts[2] + "-" + dateParts[1] + "-" + dateParts[0];
    }
    return convertedDateString;
}

// عند الضغط على زر "استعلام"
submit.addEventListener('click', function () {
    var inputnormalizedservicecode = document.getElementById("normalizedservicecode");
    var inputpsl = inputnormalizedservicecode.value.trim();
    var inputpatientid = document.getElementById("patientid");
    var inputid = inputpatientid.value.trim();

    // التحقق من أن الحقول غير فارغة
    if (inputpsl === "" || inputid === "") {
       
        alerterror2.style.display = "grid";
        return;
    }

    // إرسال الطلب إلى API لاستعلام البيانات من قاعدة البيانات
    fetch('/api/get_inquiry/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          service_code: inputpsl,
          patient_id: inputid
      })
  })
    .then(response => response.json())
    .then(data => {
        if (!data || data.message === 'error') {
            alerterror.textContent = "لا يوجد نتائج مطابقة!";
            alerterror.style.display = "grid";
            toggleButton.style.display = "inline";
            submit.style.display = "none";
        } else {
            // عرض البيانات المسترجعة
            document.getElementById('patientname').textContent = data.patient_name;
            document.getElementById('sickleavedate').textContent = convertDate(data.sick_leave_date);
            document.getElementById('duration').textContent = data.duration;
            document.getElementById('from1').textContent = data.date_from;
            document.getElementById('to1').textContent = data.date_to;
            document.getElementById('doctorname').textContent = data.doctor_name;
            document.getElementById('jobtitle').textContent = data.job_title;

            resultsDiv.style.display = 'flex';
            toggleButton.style.display = 'inline';
            submit.style.display = 'none';
            alerterror.style.display = 'none';
            alerterror2.style.display = 'none';
        }
    })
    .catch(error => {
        console.error("حدث خطأ أثناء جلب البيانات:", error);
        alerterror2.textContent = "حدث خطأ في الاتصال بالسيرفر!";
        alerterror2.style.display = "grid";
    });
});

// عند الضغط على زر "استعلام جديد"
toggleButton.addEventListener('click', function () {
    document.getElementById("normalizedservicecode").value = "";
    document.getElementById("patientid").value = "";
    toggleButton.style.display = 'none';
    resultsDiv.style.display = 'none';
    submit.style.display = 'inline';
    alerterror.style.display = 'none';
    alerterror2.style.display = 'none';
});
