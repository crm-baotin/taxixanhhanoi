from openpyxl import Workbook
from django.http import HttpResponse


def export_leads_excel(modeladmin, request, queryset):
    wb = Workbook()
    ws = wb.active
    ws.title = "Leads"

    ws.append([
        "Họ tên",
        "Số điện thoại",
        "Giới tính",
        "Nơi sinh sống",
        "Ngành nghề",
        "Thời gian đăng ký",
    ])

    for lead in queryset.order_by("-created_at"):
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


export_leads_excel.short_description = "📥 Xuất Excel (leads đã chọn)"
