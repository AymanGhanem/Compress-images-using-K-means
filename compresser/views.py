from django.shortcuts import render, redirect

from .forms import CompressorForm

from .models import Compressor


def upload(request):
    if request.method == "POST":
        form = CompressorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("compressor:upload")
    form = CompressorForm()
    images = Compressor.objects.all()
    return render(request=request, template_name="main/upload.html", context={'form': form, 'images': images})
