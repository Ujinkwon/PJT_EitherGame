from dataclasses import field, fields
from django import forms
from .models import Either, Comment

class EitherForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.Textarea(
            attrs={
                'class': 'my-title form-control',
                'rows': 1,
                'cols': 100,
            }
        )
    )
    issue_a = forms.CharField(
        label='Option A',
        widget=forms.Textarea(
            attrs={
                'class': 'my-title form-control',
                'rows': 1,
                'cols': 100,
            }
        )
    )
    issue_b = forms.CharField(
        label='Option B',
        widget=forms.Textarea(
            attrs={
                'class': 'my-title form-control',
                'rows': 1,
                'cols': 100,
            }
        )
    )
    class Meta:
        model = Either
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('either', )