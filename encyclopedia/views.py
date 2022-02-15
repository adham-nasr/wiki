from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import util
from random import randrange

import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_page(request,page_name):
    if util.get_entry(page_name) == None:
        return redirect("/error/Page_not_found")
    else:
        html = markdown2.markdown(util.get_entry(page_name))
        return render(request,"encyclopedia/article.html", {
            "page_name": page_name , "html" : html    
        })

def random(request):
    lst = util.list_entries()
    n=len(lst)
    i = randrange(0,n)
    return redirect(f"/wiki/{lst[i]}")

def search(request):
    key = request.GET["q"]
    if util.get_entry(key) != None:
        return redirect(f"/wiki/{key}")
    else:
        lst = util.list_entries()
        slst = []
        for el in lst:
            if key.lower() in el.lower():
                slst.append(el)
        return render(request,"encyclopedia/search.html" , {
            "entries" : slst
        })

def create(request):
    if request.method == "GET":
        return render(request,"encyclopedia/new.html")
    else:
        title = request.POST["title"]
        if util.get_entry(title) != None:
            return redirect("/error/Entry_already_exists")
        else:
            util.save_entry(title,request.POST["content"])
            return redirect(f"/wiki/{title}")


def error(request,error_message):
    error_message = error_message.replace("_"," ")
    return render(request,"encyclopedia/error.html" , {
        "str":error_message
    })

def edit(request,title):
    if request.method == "GET":
       return render(request,"encyclopedia/edit.html", {
            "title" : title , "content" : util.get_entry(title) 
        })
    else:
        title = request.POST["title"]
        util.save_entry(title,request.POST["content"])
        return redirect(f"/wiki/{title}")




        



