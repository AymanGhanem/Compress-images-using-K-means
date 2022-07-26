from django import forms

from compresser.models import Compressor


class CompressorForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Compressor
        fields = ('image',)
