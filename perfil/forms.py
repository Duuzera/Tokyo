from django import forms
from home.models import Usuario

class EditPerfil(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"