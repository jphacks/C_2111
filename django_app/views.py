from django.shortcuts import render
from django_app.pytorch_utils import OnnxPredictor
from django.http import HttpResponse
from django.template import loader
from django_app.forms import UploadForm, MemberForm
from django_app.models import Member
import csv
import io
import pandas as pd


def index(request):
    return render(request, 'index.html')


def load_model(model_path: str = "./onnx_model/epoch=9-valid_loss=0.6226-valid_acc=0.8033.onnx"):
    predictor = OnnxPredictor(model_path=model_path, device="cpu")
    return predictor


def to_csv(df):
    response = HttpResponse(content_type='text/csv; charset=UTF-8')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'

    df.to_csv(path_or_buf=response, encoding='utf-8-sig', index=False)

    return response

# Create your views here.


def index(request):
    if request.method == 'POST':
        upload = UploadForm(request.POST, request.FILES)
        if upload.is_valid():
            data = pd.read_csv(io.StringIO(
                request.FILES['testfile'].read().decode('utf-8')), delimiter=',')
            model = load_model()
            l = []
            for text in data["tweet"]:
                l.append(model.predict(text)[0][0][0])
            data["score"] = l
            return render(request, 'result.html', {'result': data.to_html()})
    else:
        upload = UploadForm()
        return render(request, "index.html", {'form': upload})

def new(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            params['message'] = '再入力してください'
            params['form'] = form
    else: 
        params['form'] = MemberForm()
    return render(request, '../templates/user/new.html', params)

