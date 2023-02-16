from django import forms
from .models import Entrada, Gasto

class CadastroEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()

class CadastroGasto(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()