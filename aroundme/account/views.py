from django.shortcuts import render,redirect
from django.urls import reverse_lazy
#Reverse_lazy is, as the name implies, a lazy implementation of the reverse URL resolver. 
# Unlike the traditional reverse function, reverse_lazy won't execute until the value is needed. 
# It is useful because it prevent Reverse Not Found exceptions when working with URLs that may not be immediately known.
from django.http import HttpResponse
from django.views.generic import View,TemplateView,CreateView,FormView
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail




# Create your views here.
#class Home(View):
#   def get(self,req,*arg,**kwargs):
#        return render(req,"home.html")

class Home(TemplateView):
        template_name="home.html"  
    


#class RegView(View):
#    def get(self,req,*arg,**kwargs):
#        f=RegistrationForm()
#        return render(req,"registration.html",{"form":f})
 #   def post(self,req,*arg,**kwargs):
  #      form_data=RegistrationForm(data=req.POST)
   #     if form_data.is_valid():
    #        form_data.save()
     #       messages.success(req,"user registered succefully")
      #      return redirect("h")
       # else:
        #    messages.error(req,"failed!!!")
         #   return render(req,"registration.html",{"forms":form_data})

class RegView(CreateView):
    form_class=RegistrationForm
    template_name="registration.html"
    model=User
    success_url=reverse_lazy("h")
    def form_valid(self,form):
        mail=form.cleaned_data.get("email")
        send_mail(
            "Aroundme registration",#subject
            "hii user thank you for registering aroundme",#message
            "thanimadev@gmail.com",
            [mail]
        )
        messages.success(self.request,"registration succefull")
        self.object=form.save()
        return super().form_valid(form)


class LogView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,req,*arg,**kwargs):
        form=LogForm(data=req.POST,files=req.FILES)
        if form.is_valid():
            un=form.cleaned_data.get("username")
            pw=form.cleaned_data.get("password")
            user=authenticate(req,username=un,password=pw)
            if user:
                login(req,user)
                messages.success(req,"login successfull")
                return redirect("uh")
            else:
                messages.error(req,"failed!!!")
                return render(req,"log")
        else:
            return render(req,"log.html",{"form":form})
        
class LogOut(View):
    def get(self,req):
        logout(req)
        messages.error(req," user logged out")
        return redirect("log")
    



#class LogView(View):
 #   def get(self,req,*arg,**kwargs):
  #      f1=LogForm
   #     return render(req,"log.html",{"form1":f1})
    #def post(self,req,*arg,**kwargs):
     #   form_data=LogForm(data=req.POST)
      #  if form_data.is_valid():
       #     un=form_data.cleaned_data.get("username")
        #    pw=form_data.cleaned_data.get("password")
         #   user=authenticate(req,username=un,password=pw)
          #  if user:
           #     print(user.first_name,user.last_name)
            #    login(req,user)
             #   messages.success(req,"login successfull")
              #  return redirect("uh")
         #   else:
          #      messages.error(req,"failed!!!")
           #     return redirect(req,"log")
    #    else:
     #      
      #      return render(req,"log.html",{"form":form_data})