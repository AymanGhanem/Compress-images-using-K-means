from django.shortcuts import render, redirect

from .compress import compress
from .forms import CompressorForm

from .models import Compressor


def upload(request):
    if request.method == "POST":
        form = CompressorForm(request.POST, request.FILES)
        if form.is_valid():
            compresser = form.save()
            compressed_image = compress(compresser.image)
            print(compressed_image)
            ctx = {"compressed_image": compressed_image }
            return render(request, 'main/results.html', ctx)
        return redirect("compressor:upload")
    form = CompressorForm()
    images = Compressor.objects.all()
    return render(request=request, template_name="main/upload.html", context={'form': form, 'images': images})
