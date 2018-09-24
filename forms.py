from django import forms
from .models import *


class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=22,widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Full-name',
                'id': 'name',

            }
        )
    )
    age = forms.CharField(max_length=2, min_length=1, widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter your age',
                'id': 'name',
            }
        )
    )
    state_of_origin = forms.CharField(max_length=44, widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'what is your state of origin',
                'id': 'name',

            }
        )
    )
    choice_of_candidate = forms.CharField(max_length=None, min_length=None, widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'choice of candidate',
                'id': 'name',

            }
        )
    )
    review = forms.CharField(widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Reason for choice',
                'id': 'message',

            }
        )
    )

    class Meta:
        model = UserModel
        fields = ['name', 'age', 'state_of_origin', 'choice_of_candidate', 'review']
