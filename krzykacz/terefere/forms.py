from django import forms


class AddTweetForm(forms.Form):
    content = forms.CharField(max_length=140,
                              label="Treść Tweet-a",
                              help_text="Maksymalnie 140 znaków")
