from django.shortcuts import render, redirect
from .forms import OyaForm
from .models import Oya
 
def index(request):
    oyas = Oya.objects.all()
    return render(request,  'index.html', {'oyas': oyas})
 
def form(request):
    form = OyaForm()
    return render(request, 'form.html', {'form': form})
 
def post(request):
    if request.method != 'POST':
        return redirect(to="/form")
    form = OyaForm(request.POST)
    if form.is_valid():
        oya = Oya.objects.create(
            name = request.POST['name'],
            addr = request.POST['addr']
        )
        oya.save()
        return redirect(to='/')
    else:
        return redirect(to="/form")