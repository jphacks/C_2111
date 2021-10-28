from django import forms
from .models import DailyReport


class UploadForm(forms.Form):
    testfile = forms.FileField()


class DailyReportForm(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = (
            'organization_name',
            'department_name',
            'person_name',
            'text',
        )
