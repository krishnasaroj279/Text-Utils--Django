#This project is created by- Krishna

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    
    remP = request.POST.get('rempunc','off')
    capA = request.POST.get('capfirst','off')
    spaceR = request.POST.get('spacerem','off')
    newlineR = request.POST.get('newlinerem','off')
    charC = request.POST.get('charcount','off')
    # analyzed=''
    
    if remP=='on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose':'Remove Punctuation','analyzed_text':analyzed}
        djtext = analyzed
    
    if capA == 'on':
        analyzed=''
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose':'Capitalize All', 'analyzed_text':analyzed}
        djtext = analyzed    

    if newlineR == 'on':
        analyzed=''
        for char in djtext:
            if char is not '\n' and char is not '\r':
                analyzed = analyzed + char
        param = {'purpose':'Remove New line', 'analyzed_text':analyzed}
        djtext = analyzed
          
    if spaceR == 'on':
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        param = {'purpose':'Remove Spaces', 'analyzed_text':analyzed}
        djtext = analyzed
     
                         
    if (remP!='on' and capA!='on' and newlineR!='on' and spaceR!='on'):
        return HttpResponse('''<h2>No action selected. Please try <a href="http://127.0.0.1:8000">Again!</a></h2>''')
    
    return render(request, 'analyzer.html', param)