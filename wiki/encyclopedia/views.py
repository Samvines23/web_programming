from django.shortcuts import render
from . import util
from markdown2 import Markdown

def index(request):
    entries = util.list_entries
    title = entries
    print(entries)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title":title        
    })

def entry(request, title):
    title1 = util.get_entry(title)
    if title1 == None:
        return render(request, "encyclopedia/error.html")
    else:
        markdowner = Markdown()
        page = markdowner.convert(title1)
        entries = util.list_entries()
        print(entries)
        #print(page)
       # print(title1)
        return render(request, "encyclopedia/entry.html",{
            "page": page, 
            "title": title
        })

