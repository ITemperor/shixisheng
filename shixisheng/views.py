#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
import datetime
from django.template.response import TemplateResponse as TR
#from django.template import RequestContext
from shixisheng.models import student,Image
def home(request):
    d={}
    all=student.objects.all()
    d['all']=all
    all_img=Image.objects.all()
    d['all_img']=all_img
    return TR(request,"index.html",d)
    #return HttpResponse("Hello world")


def hello(request,abcd):
    #return HttpResponse("Hello world"+x)
   	d={"abcd":abcd,"date":str(datetime.datetime.now())}
   	all=student.objects.all()
   	d['all']=all
   	return TR(request,"hello.html",d)
   	#return render_to_response("hello.html",d,context_instance=RequestContext(request))

def new(request):
  print request.POST
  s=student()
  s.name=request.POST['name']
  s.addrss =request.POST['addrss']
  s.content=request.POST['content']
  s.count=0
  s.save()
  return redirect("/hello/fd")

def delete(request,id):
  s=student.objects.get(id=int(id))
  s.delete()
  return redirect("/hello/fd")

def edit_view(request,id):
  s=student.objects.get(id=int(id))
  time=datetime.datetime.now()
  d={"s":s,"t":str(time)}
  return TR(request,"edit.html",d)

def edit(request,id):
  s=student.objects.get(id=int(id))
  s.name=request.POST['name']
  s.addrss=request.POST['addrss']
  s.save()
  return redirect("/hello/fd")