from django.shortcuts import render, redirect, get_object_or_404
from .forms import SigninForm, SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.urls.base import reverse
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from .forms import PDSForm, MDSForm
from .models import PJT, MR, EQT, PDS, MDS
from django.contrib import messages

class PJTList(ListView):
    model = PJT
    paginate_by = 10

    def pjt_list(request):
        pjt_counts = PJT.objects.all().count()
        context = {
            'pjt_counts': pjt_counts
        }
        return render(request, 'mds02/pjt_list.html', context=context)

class PJTDetail(DetailView):
    model = PJT

#def pjt_list(request):
    #pjts = PJT.objects.all()
    #context = {'pjts':pjts}
    #messages.add_message(request, messages.INFO, ' 로그인 되었습니다.')
    #return render(request, 'mds02/pjt_list.html', context)

#class PJTDetailView(DetailView):
#    model = PJT
#    def PJT_detail_view(request, P_Name):
#        pjt = get_object_or_404(PJT,P_Name = P_Name)
#        return render(request,'mds02/pjt_detail.html',context=)



class MRList(ListView):
    model = MR
    paginate_by = 10

    def mr_list(request):
        pjt_counts = PJT.objects.all().count()
        context = {
            'pjt_counts': pjt_counts
        }
        return render(request, 'mds02/pjt_list.html', context=context)


class MRDetail(DetailView):
    model = MR
     #def get_queryset(self):
     #   return MR.objects.all()

     #def mr_list(request, P_No):
     #   mrs = MR.objects.all()
     #  context = {'mrs': mrs, 'P_No': P_No}
     #  return render(request, 'mds02/mr_list.html', context)

class EQTList(ListView):
    model = EQT
    paginate_by = 10

class MyEQTList(LoginRequiredMixin, View):
    model = EQT
    paginate_by = 10

    def get_queryset(self):
        return EQT.objects.filter(E_user=self.request.User)


class EQTDetail(DetailView):
    model = EQT

#def eqt_list(request, P_No, M_No):
#    eqts = EQT.objects.all()
#    context = {'eqts':eqts, 'P_No':P_No, 'M_No': M_No}
#    return render(request, 'mds02/eqt_list.html', context)

def eqt_pds(request, P_No, M_No, E_No):
    pds = PDS.objects.all()
    context = {'pds':pds, 'P_No':P_No, 'M_No': M_No, 'E_No':E_No}
    return render(request, 'mds02/eqt_pds.html', context)

def eqt_mds(request, P_No, M_No, E_No):
    mds = MDS.objects.all()
    context = {'mds':mds, 'P_No':P_No, 'M_No': M_No, 'E_No':E_No}
    return render(request, 'mds02/eqt_mds.html', context)


class PJTCreate(CreateView):
    model = PJT
    fields =  '__all__'

class PJTUpdate(UpdateView):
    model = PJT
    fields =  '__all__'

class PJTDelete(DeleteView):
    model = PJT
    success_url = reverse_lazy('pjt_list')

class MRCreate(CreateView):
    model = MR
    fields =  '__all__'

class MRUpdate(UpdateView):
    model = MR
    fields =  '__all__'

class MRDelete(DeleteView):
    model = MR
    success_url = reverse_lazy('mr_list')

class EQTCreate(CreateView):
    model = EQT
    fields =  '__all__'

class EQTUpdate(UpdateView):
    model = EQT
    fields =  '__all__'

class EQTDelete(DeleteView):
    model = EQT
    success_url = reverse_lazy('eqt_list')




def eqt_mds_form(request):
    if request.method == "POST":
        form = MDSForm(request.POST)
        if form.is_valid():
            mds = form.save(commit=False)
            mds.save()
            return redirect('eqt_mds', pk=mds.pk)
        else:
            form = MDSForm()
        return render(request, 'mds02/eqt_mds_edit.html', {'form': form})


# 회원가입 기능
def signup(request):
    if request.method == "GET":
        return render(request, 'mds02/signup.html',{'f':SignupForm()})
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
                new_user.save()

                return HttpResponseRedirect(reverse('mds02:signin'))
            else:
                return render(request, 'mds02/signup.html',{'f':form, 'error':'비밀번호와 비밀번호 확인이 다릅니다.'})
        else:
            return render(request, 'mds02/signup.html',{'f':form})

# 로그인 기능
def signin(request):
    if request.method == "GET":
        return render(request, 'mds02/signin.html',{'f':SigninForm()})
    elif request.method == "POST":
        form = SigninForm(request.POST)
        id = request.POST['username']
        pw = request.POST['password']
        u = authenticate(username=id, password=pw)

        if u:
            login(request, user=u)
            return HttpResponseRedirect(reverse('mds02:pjt_list'))
        else:
            return render(request, 'mds02/signin.html',{'f':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})

# 로그아웃 기능
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mds02:signin'))

