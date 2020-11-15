from django.shortcuts import render
from django.http import HttpResponse
import random

import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wikiPage(request, page):
    
    title = page
    page = util.get_entry(page)

    if(page == None):
        return render(request, "encyclopedia/error404.html")
    
    page = markdown2.markdown(page)

    return render(request, "encyclopedia/wikiPage.html", {
        "title": title,
        "page": page
    })

def search(request):

    if request.method == "POST":

        toSearch = request.POST.get('q', None).upper()  
        list_entries = util.list_entries()

        if toSearch.capitalize() in list_entries:
            return wikiPage(request, toSearch)

        list_search = []

        for entry in list_entries:
            if toSearch in entry.upper():
                list_search.append(entry)
        
        return render(request, "encyclopedia/search.html", {
            "entries": list_search
        })
        
def create(request):

    if request.method == "GET":
        return render(request, "encyclopedia/create.html")

    title = request.POST.get('title', None).capitalize()
    content = request.POST.get('textArea', None)

    list_entries = util.list_entries()

    if title in list_entries :
        return render(request, "encyclopedia/errorCreate.html")
    
    fileMD = open(f"entries/{title}.md", "w")

    fileMD.write(content)

    fileMD.close()

    return wikiPage(request, title)

def editPage(request, page):

    if request.method == "GET":

        fileMD = open(f"entries/{page}.md", "r")

        content = fileMD.read()

        fileMD.close()

        if request.method == "GET":
            return render(request, "encyclopedia/editPage.html", {
                "title": page,
                "content": content
            })

    content = request.POST.get('textArea', None)
    
    fileMD = open(f"entries/{page}.md", "w")

    fileMD.write(content)

    fileMD.close()

    return wikiPage(request, page)

def randomPage(request):

    list_entries = util.list_entries()

    sizeList = len(list_entries)

    randomNumber = random.randrange(0, sizeList - 1)

    page = list_entries[randomNumber]

    return wikiPage(request, page)
