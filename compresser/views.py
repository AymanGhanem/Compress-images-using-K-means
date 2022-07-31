from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

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


@method_decorator(name='dispatch', decorator=csrf_exempt)
class CompressImageView(UpdateView):
    queryset = Compressor.objects.all()

    def post(self, request, *args, **kwargs):
        compresser = self.get_object()
        compressed_image = compress(compresser.image, colors=int(request.POST.get('colors', 2)))
        return JsonResponse(data={'image': compressed_image})
