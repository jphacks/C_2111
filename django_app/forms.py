from django import forms
from .models import DailyReport, Questionnaire


class UploadForm(forms.Form):
    testfile = forms.FileField()


class DailyReportForm(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = (
            'text',
        )


class CreateQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = (
            'title',
        )
