from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView,ListView
from django.contrib.auth.models import User
from django.forms.models import BaseModelForm
from django.contrib.auth import authenticate,login,logout
from  user.forms import Registration,Studentprofile
from django.urls import reverse_lazy
from app.models import student,job,applications
from django.utils.decorators import method_decorator
# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


class Register(CreateView):
    template_name="user/register.html"
    form_class=Registration
    model=User
    success_url=reverse_lazy("reg")

#class Signin(View):
   #def get(self,request,*args,**kwargs):
        #form=Loginform()
        #return render(request,"user/login.html",{"form":form})
    
    #def post(self,request,*args,**kwargs):
        #form=Loginform(request.POST)
        #if form.is_valid():
            #u_name=form.cleaned_data.get("username")
            #pwd=form.cleaned_data.get("password")
            #user_obj=authenticate(request,username=u_name,password=pwd)
            #if user_obj:
                #login(request,user_obj)
               # print("user logged in")
            #else:
                #print("False credentials")
           # return redirect("reg")

class Student_home(ListView):
    template_name="user/index.html"
    model=job
    context_object_name="job"

class user_profile(CreateView):
    template_name="user/profile.html"
    form_class=Studentprofile
    model=student
    success_url=reverse_lazy('reg')

    # def post(self,request,*args,**kwargs):
    #     form=Studentprofile(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         return redirect("userindex")
    #     else:
    #         print("getout")
    #     return redirect("reg")
    
    def form_valid(self,form:BaseModelForm):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class Profileview(DetailView):
    template_name="user/p_view.html"
    context_object_name="data"
    model=student
    success_url=reverse_lazy('userview')
    #def get(self,request,*args,**kwargs):
        #id=kwargs.get("pk")
        #data=student.objects.filter(id=id)
        #return render(request,self.template_name,{'data':data})
    
class update_profile(UpdateView):
    template_name="user/p_edit.html"
    model=student
    form_class=Studentprofile
    success_url=reverse_lazy('userindex')

class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    
class jobdetailsview(DetailView):
    template_name="user/jobdetail.html"
    model=job
    context_object_name="data"


@method_decorator(signin_required,name="dispatch")
class Applyviewjob(View):
    
     def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        job_obj=job.objects.get(id=id)
        user=request.user
        applications.objects.create(jobs=job_obj,student=user)
        return redirect("userindex")

class Appliedjob(View):
    def get(self,request,*args,**kwargs):
        data=applications.objects.filter(student=request.user)

        return render(request,"user/appliedjob.html",{"data":data})

class deljob(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        applications.objects.get(id=id).delete()
        return render("deljob")
        