from django.shortcuts import render, redirect
from characters.forms.universe_form import Universe_form
from characters.models import Universe


def save_form(request):
    return render(request, 'characters\\save_universe_form.html')


def list(request):
    lista = Universe.objects.all()
    return render(request, 'universes\\show_universes.html', {'universes': lista})


def create(request):
    form = Universe_form(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'universes\\create_universe.html', context)


def edit(request, id):
    universe = Universe.objects.filter(id=id).first()
    form = Universe_form(request.POST or None, instance=universe)
    return render(request, 'universes\\edit_universe.html', {'form': form, 'universe': universe})


def update(request, id):
    universe = Universe.objects.get(pk=id)
    form = Universe_form(request.POST, instance=universe)
    if form.is_valid():
        form.save()
        return redirect('universes')
    context = {
        'form': form
    }
    return render(request, 'universes\\edit_universe.html', context)


def delete(request, id):
    universe = Universe.objects.get(pk=id)
    universe.delete()
    lista = Universe.objects.all()
    return render(request, 'universes\\show_universes.html', {'universes': lista})

