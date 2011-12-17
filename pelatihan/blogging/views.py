# Create your views here.
import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from blogging.models import Artikel
from blogging.form import FormArtikel

def sekarang(request):
    waktu = datetime.datetime.now()
    return HttpResponse(waktu)

def home(request):
    artikel = Artikel.objects.all()
    return render_to_response('home.html',{
               'artikels': artikel
           })
def baca(request,id_artikel):
    artikel = Artikel.objects.get(id=id_artikel)
    return render_to_response('baca.html',{
               'artikel' : artikel
           })
def sunting(request):
    if request.method == "POST" :
        form = FormArtikel(request.POST)
        if form.is_valid() :
            form.save()
    return render_to_response('sunting.html',{
               'form' : FormArtikel()
           },RequestContext(request))
