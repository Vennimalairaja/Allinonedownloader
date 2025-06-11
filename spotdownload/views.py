from django.shortcuts import render
from .forms import URLForm
from django.http import HttpResponse
from .spot import spot_download
# Create your views here.
def Homepage(request):
    form=URLForm()
    if request.method=='POST':
        form=URLForm(request.POST)
        if form.is_valid():
            url=form.cleaned_data['url']
            if spot_download(url):
                return HttpResponse('<h1>Success</h1>')
            else:
                return HttpResponse('<h1>Failure</h1>')
    context={'form':form}
    return render(request,'index.html',context)