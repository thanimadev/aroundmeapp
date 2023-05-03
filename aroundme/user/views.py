
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View,TemplateView,CreateView,UpdateView,FormView,DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from .models import*
from .forms import*
from django.contrib.auth.models import User




# Create your views here.
class Uhome(CreateView):
    template_name="uhome.html"
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("uh")
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"post added!")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Posts.objects.all().order_by('-datetime')
        context["cform"]=CommentForm()
        context["comments"]=Comments.objects.all()
        return context

def addcomment(request,*args,**kwargs):
    if request.method=="POST":
        pid=kwargs.get("pid")
        post=Posts.objects.get(id=pid)
        user=request.user
        comment=request.POST.get("comment")
        Comments.objects.create(comment=comment,user=user,post=post)
        return redirect("uh")
    
#class Uhome(CreateView):
#    template_name="uhome.html"
#    form_class=PostForm
#    model=Posts
#    success_url=reverse_lazy("uh")
#    def form_valid(self, form):
#        form.instance.user=self.request.user
#        self.object=form.save()
#        messages.success(self.request,"post added!")
#        return super().form_valid(form)
#    def get_context_data(self, **kwargs):
#        context=super().get_context_data(**kwargs)
#        context["data"]=Posts.objects.all().order_by('-datetime')
#        context["cform"]=CommentForm()
#        return context

def addlike(request,*args,**kwargs):
    pid=kwargs.get("pid")
    post=Posts.objects.get(id=pid)
    user=request.user
    post.likes.add(user)
    post.save()
    return redirect("uh")

    
class Myblog(TemplateView):
    template_name="myblog.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Posts.objects.filter(user=self.request.user) 
        return context

class Dblog(DeleteView):
    model=Posts
    template_name="deleteblog.html"
    success_url=reverse_lazy("mb")
    pk_url_kwargs="pk"


    
class Eblog(UpdateView):
    model=Posts
    form_class=PostForm
    
    template_name="eblog.html"
    success_url=reverse_lazy("mb")
    pk_url_kwargs="pk"




#def get(self,req,*arg,**kwargs):
        #return render(req,"uhome.html")
class Profile(View):
    def get(self,req,*args,**kwargs):
        return render(req,"profile.html")

class Addbio(CreateView):
    form_class=BioForm
    template_name="addbio.html"
    model=Bio
    success_url=reverse_lazy("pro")
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"bio added!")
        return super().form_valid(form)


class Editbio(UpdateView):
    model=Bio
    form_class=BioForm
    template_name="editbio.html"
    success_url=reverse_lazy("pro")
    pk_url_kwargs="pk"

#    def get(self,req,*arg,**kwargs):
#        id=kwargs.get("pk")
#        bio=Bio.objects.get(id=id)
#        f=BioForm(instance=bio)
 #       return render(req,"editbio.html",{"form":f})
  #  def post(self,request,*args,**kwargs):
   #     id=kwargs.get("pk")
    #    bio=Bio.objects.get(id=id)
     #   form_data=BioForm(data=request.DATA,files=request.FILES)
      #  if form_data.is_valid():
       #     form_data.save()
        #    messages.success(request,"bio updated")

class Cpassword(FormView):
    template_name="cpassword.html"
    form_class=PForm
    def post(self,request,*arg,**kwargs):
        form_data=PForm(data=request.POST)
        if form_data.is_valid():
            old=form_data.cleaned_data.get("old_password")
            new=form_data.cleaned_data.get("new_password")
            confirm=form_data.cleaned_data.get("confirm_new_password")
            user=authenticate(request,username=request.user.username,password=old)
            if user:
                if new==confirm:
                    user.set_password(new)
                    user.save()
                    messages.success(request,"password updated")
                    logout(request)
                    return redirect("log")
                else:
                    messages.error(request,"password mismatches!!!")
                    return render(request,"cpassword.html",{"form":form_data})
        
            else:
              messages.error(request,"incorrect password!!!")
              return render(request,"cpassword.html",{"form":form_data})
        
        else:
            return render(request,"cpassword.html",{"form":form_data})
        
    
    


    


    
    