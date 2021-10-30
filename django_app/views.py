from django.shortcuts import get_object_or_404, redirect, render
from django_app.pytorch_utils import OnnxPredictor
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django_app.forms import UploadForm, DailyReportForm, CreateQuestionnaireForm
from django_app.models import DailyReport, Questionnaire
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse
import csv
import io
import pandas as pd
from goo_lab.goo_apis import Goo


def index(request):
    return render(request, 'index.html')


def load_model(model_path: str = "./onnx_model/epoch=9-valid_loss=0.4620-valid_acc=0.7831_quant.onnx"):
    predictor = OnnxPredictor(model_path=model_path, device="cpu")
    return predictor


@login_required
def create(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = CreateQuestionnaireForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('django_app:index'))
        else:
            params['message'] = '再入力してください'
            params['form'] = form
    else:
        params['form'] = CreateQuestionnaireForm()
    return render(request, 'create.html', params)


@login_required
def questionnaires(request):
    params = {"questionnaires": Questionnaire.objects.filter(
        author=request.user)}
    return render(request, 'questionnaires.html', params)


model = load_model()
@login_required
def new(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
    params = {'message': '', 'form': None, 'questionnaire': questionnaire}
    if request.method == 'POST':
        form = DailyReportForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            score = model.predict(form["text"].value())
            post.score = score[0][0][1]
            post.questionnaire = questionnaire
            post.author = request.user
            post.save()
        else:
            params['message'] = '再入力してください'
            params['form'] = form
    else:
        params['form'] = DailyReportForm()
    return render(request, 'user/new.html', params)


@login_required
def info(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
    daily_reports = DailyReport.objects.all().filter(questionnaire=questionnaire)
    print(daily_reports, 0)
    return render(request, 'info.html', {'questionnaire': questionnaire, 'daily_reports': daily_reports})
