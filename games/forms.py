from django import forms


class AddGameForm(forms.Form):
    name = forms.CharField(label='Name', max_length=300)
    min_players = forms.IntegerField()
    max_players = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)

