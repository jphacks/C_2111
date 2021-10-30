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
from graph.word_cloud import create_wordcloud_base64
from graph.psn_freq_graph import create_psn_freq_graph_base64


def index(request):
    return render(request, 'index.html')


def load_model(model_path: str = "./onnx_model/epoch=9-valid_loss=0.1356-valid_acc=0.9745_quant.onnx"):
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
            return HttpResponseRedirect(reverse('django_app:index'))
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
    texts = []
    for dr in list(daily_reports):
        texts.append(dr.text)
    wc_base64Img = create_wordcloud_base64(texts)
    psn_freq_base64Img = create_psn_freq_graph_base64(texts)
    return render(request, 'info.html', {'questionnaire': questionnaire,
                                         'daily_reports': daily_reports,
                                         'exists_wordcloud': bool(wc_base64Img is not None),
                                         'wc_base64Img': wc_base64Img,
                                         'exists_psn_freq': bool(psn_freq_base64Img is not None),
                                         'psn_freq_base64Img': psn_freq_base64Img, })
