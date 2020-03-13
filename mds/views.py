from django.shortcuts import render

from .models import Project, MR, EQT

def pjt(request):
    pjts = Pjt.objects.all()
    context = {'pjts':pjts}
    return render(request, 'mds/pjt_list.html', context)

def mr(request, PJT_No):
    pjts = Pjt.objects.all()
    mrs = Mr.objects.all()
    context = {'projcets' : projects, 'MRs': MRs}
    return render(request, 'mds/mr_list.html', context)

def eqt(request, MR_No):
    pjts = Pjt.objects.all()
    mrs = Mr.objects.all()
    eqts = Eqt.objects.all()
    context = {'projcets' : projects, 'MRs': MRs, 'EQTs':EQTs}
    return render(request, 'mds/eqt_list.html', context)