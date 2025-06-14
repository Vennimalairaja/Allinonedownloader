from django import forms

class URLForm(forms.Form):
    spotify_url=forms.URLField(max_length=200,required=False)
class YoutubeURLForm(forms.Form):
    CATEGORY_CHOICES=[
        ('video','Video'),
        ('audio','Audio')
    ]
    Youtube_url=forms.URLField(max_length=200,required=False)
    category=forms.ChoiceField(choices=CATEGORY_CHOICES,required=False)
    
