from django.forms import ModelForm
from .models import investimentos

class investimentofrm(ModelForm):
    class Meta:
        model = investimentos
        fields = '__all__'
