from django import forms
from .models import Member

class UploadForm(forms.Form):
    testfile = forms.FileField()

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('id', 'name', 'data1', 'data2', 'data3', 'data4', 'data5', 'data6', 'data7', 'data8', 'data9', 'data10', 'data11', 'data12', 'data13', 'data14', 'data15', 'data16', 'data17', 'data18', 'data19', 'data20')