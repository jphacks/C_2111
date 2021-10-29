from django.shortcuts import render
from django_app.pytorch_utils import OnnxPredictor
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django_app.forms import UploadForm, DailyReportForm
from django_app.models import DailyReport
from django.contrib.auth.decorators import login_required
import csv
import io
import pandas as pd
from goo_lab.goo_apis import Goo


def index(request):
    return render(request, 'index.html')


def load_model(model_path: str = "./onnx_model/epoch=9-valid_loss=0.1356-valid_acc=0.9745_quant.onnx"):
    predictor = OnnxPredictor(model_path=model_path, device="cpu")
    return predictor


def new(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = DailyReportForm(request.POST)
        if form.is_valid():
            form.save()
            model = load_model()
            score = model.predict(form["text"].value())
            DailyReport.objects.values().filter(
                organization_name = form["organization_name"].value(),
                department_name = form["department_name"].value(),
                person_name = form["person_name"].value(),
                text = form["text"].value(),
            ).update(score = score[0][0][1])
        else:
            params['message'] = '再入力してください'
            params['form'] = form
    else:
        params['form'] = DailyReportForm()
    return render(request, 'user/new.html', params)


@login_required
def info(request):
    return render(request, 'info.html')
