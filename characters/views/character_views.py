from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.template import RequestContext

from characters.forms.character_form import Character_form
from characters.models import Character


def save(request):
    form = Character_form(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'characters/create_character.html', context)


@login_required
def list(request):
    lista = Character.objects.all()
    return render(request, 'characters\\show_characters.html', {'characters': lista})


def edit(request, id):

    character = Character.objects.filter(id=id).first()
    form = Character_form(request.POST or None, instance=character)

    return render(request, 'characters/edit_character.html', {'form': form, 'characters': character})


def update(request, id):

    character = Character.objects.get(pk=id)
    form = Character_form(request.POST, instance=character)
    if form.is_valid():
        form.save()
        return redirect('characters')
    context = {
        'form': form
    }
    return render(request, 'characters/edit_character.html', context)


def delete(request, id):
    character = Character.objects.get(pk=id)
    character.delete()
    lista = Character.objects.all()
    return render(request, 'characters\\show_characters.html', {'characters': lista})

