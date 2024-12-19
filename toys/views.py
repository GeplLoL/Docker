from django.shortcuts import render, get_object_or_404, redirect
from .models import Toy
from .forms import ToyForm

def toy_list(request):
    toys = Toy.objects.all()
    return render(request, 'toys/toy_list.html', {'toys': toys})

def toy_detail(request, pk):
    toy = get_object_or_404(Toy, pk=pk)
    return render(request, 'toys/toy_detail.html', {'toy': toy})

def toy_create(request):
    if request.method == "POST":
        form = ToyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('toy_list')
    else:
        form = ToyForm()
    return render(request, 'toys/toy_form.html', {'form': form})

def toy_edit(request, pk):
    toy = get_object_or_404(Toy, pk=pk)
    if request.method == "POST":
        form = ToyForm(request.POST, instance=toy)
        if form.is_valid():
            form.save()
            return redirect('toy_list')
    else:
        form = ToyForm(instance=toy)
    return render(request, 'toys/toy_form.html', {'form': form})

def toy_delete(request, pk):
    toy = get_object_or_404(Toy, pk=pk)
    if request.method == "POST":
        toy.delete()
        return redirect('toy_list')
    return render(request, 'toys/toy_confirm_delete.html', {'toy': toy})

