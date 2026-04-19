from django.contrib import admin
from django.utils import timezone
from datetime import timedelta


class CreatedAtRangeFilter(admin.SimpleListFilter):
    title = "Thời gian đăng ký"
    parameter_name = "created_at_range"

    def lookups(self, request, model_admin):
        return (
            ("today", "Hôm nay"),
            ("7days", "7 ngày gần nhất"),
            ("30days", "30 ngày gần nhất"),
        )

    def queryset(self, request, queryset):
        now = timezone.now()

        if self.value() == "today":
            return queryset.filter(created_at__date=now.date())

        if self.value() == "7days":
            return queryset.filter(created_at__gte=now - timedelta(days=7))

        if self.value() == "30days":
            return queryset.filter(created_at__gte=now - timedelta(days=30))

        return queryset
