from django.shortcuts import render
from .forms import URLForm
from django.http import HttpResponse
from .spot import spot_download
from .move import move_file
from django.templatetags.static import static
# Create your views here.
def Homepage(request):
    form=URLForm()
    if request.method=='POST':
        form=URLForm(request.POST)
        if form.is_valid():
            url=form.cleaned_data['url']
            file=spot_download(url)
            if file:
                success_failure=move_file(file)
                file=f'/Music/{file}'
                link=static(file)
                return render(request,'download.html',{'link':link})
            else:
                return HttpResponse('<h1>Failure</h1>')
    context={'form':form}
    return render(request,'index.html',context)
def download_page(request):
    return render(request,'download.html')