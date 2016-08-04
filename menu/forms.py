from django import forms
from .models import Cupcake,Comment


class CupcakeForm(forms.ModelForm):

    class Meta:
        model = Cupcake
        fields = ('name','rating','price','image')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
