from django import forms
from django.core import validators
from django.core.validators import validate_unicode_slug

from . import models

def must_be_caps(value):
    if not value.isupper():
        raise forms.ValidationError("Not all upper case")
    # Always return the cleaned data
    return value

def must_be_bob(value):
    if not value.startswith("BOB"):
        raise forms.ValidationError("Must start with BOB")
    # Always return the cleaned data
    return value


class SuggestionForm(forms.Form):
    suggestion_field = forms.CharField(
        label='Suggestion',
        max_length=240,
        # validators=[validate_unicode_slug, must_be_caps, must_be_bob]
        )

    def save(self, request):
        suggestion_instance = models.SuggestionModel()
        suggestion_instance.suggestion = self.cleaned_data["suggestion_field"]
        suggestion_instance.author = request.user
        suggestion_instance.save()
        return suggestion_instance
