
from django.contrib import admin
from django.db.models import fields

from .models import DailyReport, Questionnaire


class QuestionnaireAdmin(admin.ModelAdmin):
    readonly_fields = [
        'date',
    ]
    fields = [
        'title',
    ]


class DailyReportAdmin(admin.ModelAdmin):
    readonly_fields = ['date']
    fields = [
        'questionnaire',
        'text',
        'author',
        'score',
    ]


admin.site.register(DailyReport, DailyReportAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)
