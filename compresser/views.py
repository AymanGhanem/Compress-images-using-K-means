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
            ctx = {"compressed_image": compressed_image, "original_image": compresser}
            return render(request, 'partials/results.html', ctx)
    form = CompressorForm()
    # images = Compressor.objects.all()
    images = Compressor.objects.none()
    return render(request=request, template_name="main/upload.html", context={'form': form, 'images': images})
