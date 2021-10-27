from django.shortcuts import render
from django_app.pytorch_utils import OnnxPredictor
from django.http import HttpResponse
from django.template import loader
from django_app.forms import UploadForm
import csv,io
import pandas as pd


def index(request):
    return render(request, 'index.html')

def load_model(model_path:str = "./onnx_model/epoch=9-valid_loss=0.6320-valid_acc=1.0000_quant.onnx"):
    predictor = OnnxPredictor(model_path=model_path, device="cpu")
    return predictor


def to_csv(df):
    response = HttpResponse(content_type='text/csv; charset=UTF-8')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'

    df.to_csv(path_or_buf = response, encoding = 'utf-8-sig', index=False)

    return response

# Create your views here.
def index(request):
    if request.method == 'POST':
        upload = UploadForm(request.POST, request.FILES)
        if upload.is_valid():
            data = pd.read_csv(io.StringIO(request.FILES['testfile'].read().decode('utf-8')), delimiter=',')

            response = to_csv(data)

            return response
    else:
        upload = UploadForm()
        return render(request, "index.html", {'form':upload})