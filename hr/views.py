from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView,ListView,DeleteView,UpdateView,DetailView
from django.contrib.auth import authenticate,login,logout
from hr.forms import LoginForm,categoryform,jobform
from django.urls import reverse_lazy
from app.models import Category,job,applications,student
# Create your views here.

class loginview(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                if request.user.is_superuser:
                    return redirect("index")
                else:
                    return redirect("userindex")
            else:
                print("failed")
            return render(request,"login.html",{"form":form})
        
class dashboard(TemplateView):
    template_name="index.html"

class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")

class Addcategory(CreateView,ListView):
    template_name="category.html"
    form_class=categoryform
    success_url=reverse_lazy("category")
    context_object_name="data"
    model=Category

#class categoryremove(DeleteView):
    #template_name="category.html"
    #model=Category
    #success_url=reverse_lazy("category")

class categoryremove(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Category.objects.get(id=id).delete()
        return redirect("category")
    
class Addjob(CreateView):
    template_name="job_add.html"
    form_class=jobform
    model=job
    success_url=reverse_lazy("addjob")
    #context_object_name="qs"

class jobremove(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        job.objects.get(id=id).delete()
        return redirect("addjob")
    
#class jobdetail(View):
    #def get(self,request,*args,**kwargs):
        #id=kwargs.get("pk")
        #detail=job.objects.filter(id=id)
        #return render(request,"jobview.html",{"detail":detail})
    
class joblist(ListView):
    template_name="job_list.html"
    model=job
    context_object_name="jobs"

class jobupdate(UpdateView):
    template_name="jobview.html"
    form_class=jobform
    success_url=reverse_lazy("index")
    model=job

class Viewjobs(View):
    def get(self,request,*args,**kwargs):
        data=applications.objects.all()
        return render(request,"viewjob.html",{"data":data})
    
class Seeker(DetailView):
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     student.objects.get(id=id)
    #     return render(request,"userdetails.html")
    template_name="userdetails.html"
    context_object_name="data"
    model=student
    success_url=reverse_lazy('hrview')
    