from django.forms import ModelForm
from .models import ModelPost

class PostForm(ModelForm):
    class Meta:
        model = ModelPost
        fields = "__all__"
