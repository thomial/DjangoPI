# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from . import LogicProgram
from forms import Document
from models import *

# Create your views here.

def home(request):

    return render (request, 'home/home.html', {})

def upload_file_csv(request):
    if request.method == 'POST':
        form = Document(request.POST, request.FILES)
        if form.is_valid():
            save = form.save()
            id = save.id
            return redirect('proccess', id = id)
    else:
        form = Document()

    return render (request, 'home/upload_file_csv.html', {'form' : form})

def process_input(request, id):
    import csv

    Upload = table_post_description.objects.get(id = id)
    upload_doc = Upload.document
    nil_imp = Import_Nilai
    hit_kor_reg = regresi_korelasi

    with open('media/%s' %upload_doc) as file :
        reader = csv.DictReader(file)
        for row in reader :
            a = nil_imp(
                tahun=row['tahun'],
                bulan=row['bulan'],
                nilai=row['nilai'],
                berat=row['berat'],
                post_id=Upload
            )
            a.save()
    hitung = LogicProgram.Hitung_Regresi_korelasi(id)
    a, b, kor = hitung.hitung()

    reg_a = regresi_korelasi(
        tahun= nil_imp.objects.get(post_id=id).tahun[0],
        hasil_regresi_a= a,
        hasil_regresi_b= b,
        hasil_korelasi= kor
    )
    reg_a.save()

    return HttpResponseRedirect('')










