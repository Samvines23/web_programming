from django.shortcuts import render
from . import util
from markdown2 import Markdown

def index(request):
    #entries = util.list_entries()
    #title = entries
    #print(entries)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        #"title":title        
    })

def entry(request, title):
    entry1 = util.get_entry(title)
    #test = str(entry1)
    #test1 = test.replace("/wiki/","/")
   # print(test1)
    #print("test is " + test)
    if entry1 == None:
        return render(request, "encyclopedia/error.html")
    else:
        markdowner = Markdown()
        page = markdowner.convert(entry1)
        #entries = util.list_entries()
      #  print("entry1 is " + entry1)
       # print(page)
       # print(title1)
        return render(request, "encyclopedia/entry.html",{
            "page": page, 
            "title": title
        })
    
def search(request):
    input = request.get("q")
    print(input)


