from django.shortcuts import render
from django_app.pytorch_utils import OnnxPredictor
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django_app.forms import UploadForm, DailyReportForm
from django_app.models import DailyReport
import csv
import io
import pandas as pd
from goo_lab.goo_apis import Goo


def index(request):
    return render(request, 'index.html')


def load_model(model_path: str = "./onnx_model/epoch=9-valid_loss=0.6226-valid_acc=0.8033.onnx"):
    predictor = OnnxPredictor(model_path=model_path, device="cpu")
    return predictor


def new(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = DailyReportForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            params['message'] = '再入力してください'
            params['form'] = form
    else:
        params['form'] = DailyReportForm()
    return render(request, 'user/new.html', params)


@login_required
def info(request):
    return render(request, 'info.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('top')

    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS, '会員登録に成功しました')
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form) -> HttpResponse:
        messages.add_message(self.request, messages.ERROR, '会員登録に失敗しました')
        return super().form_invalid()
