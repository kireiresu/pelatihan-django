from django.forms import ModelForm
from blogging.models import Artikel

class FormArtikel(ModelForm):

    class Meta:
        model = Artikel
