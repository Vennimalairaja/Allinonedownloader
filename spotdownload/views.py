from django.shortcuts import render
from .forms import URLForm,YoutubeURLForm
from django.http import HttpResponse
from .spot import spot_download
from .move import move_file
from django.templatetags.static import static
from .tube import yt_download
# Create your views here.
def Homepage(request):
    form=URLForm()
    youtube=YoutubeURLForm()
    if request.method=='POST':
        submitted=request.POST.get('form_submit')
        form=None
        if submitted=='spotify':
            form=URLForm(request.POST)
        elif submitted=='Youtube':
            form=YoutubeURLForm(request.POST)
        if form.is_valid()and submitted=='spotify':
            url=form.cleaned_data['spotify_url']
            file=spot_download(url)
            if file:
                success_failure=move_file(file)
                file=f'/Music/{file}'
                link=static(file)
                return render(request,'download.html',{'link':link})
            else:
                return HttpResponse('<h1>Failure</h1>')
        elif submitted=='Youtube':
            if form.is_valid():
                url=form.cleaned_data['Youtube_url']
                category=form.cleaned_data['category']
                file=yt_download(url=url,category=category)
                if file:
                    success_failure=move_file(file)
                    file=f'/Music/{file}'
                    link=static(file)
                    return render(request,'download.html',{'link':link})
                else:
                    return HttpResponse(f'<h1>Youtube link:{url} and category:{category} is failure</h1>')
            #file=yt_download
    context={'form':form,'youtube':youtube}
    return render(request,'index.html',context)
def download_page(request):
    return render(request,'download.html')