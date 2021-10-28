from django.contrib import admin

from .models import DailyReport


class DailyReportAdmin(admin.ModelAdmin):
    fields = [
        'organization_name',
        'department_name',
        'person_name',
        'text',
        'date',
        'person_id',
        'score',
    ]


admin.site.register(DailyReport, DailyReportAdmin)
