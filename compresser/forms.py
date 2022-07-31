from django import forms

from compresser.models import Compressor


class CompressorForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Compressor
        fields = ('image',)
