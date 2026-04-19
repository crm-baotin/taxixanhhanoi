from django.http import HttpResponse
from openpyxl import Workbook
from .models import Lead


def export_leads_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Leads"

    # Header
    ws.append([
        "Họ tên",
        "Số điện thoại",
        "Giới tính",
        "Nơi sinh sống",
        "Ngành nghề",
        "Thời gian đăng ký",
    ])

    # Data
    for lead in Lead.objects.all().order_by("-created_at"):
        ws.append([
            lead.full_name,
            lead.phone,
            lead.sex,
            lead.location,
            lead.job,
            lead.created_at.strftime("%d/%m/%Y %H:%M"),
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="leads.xlsx"'

    wb.save(response)
    return response
