from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pip._vendor.chardet.enums import CharacterCategory
from ORM_characters.forms.character_form import CharacterForm
from ORM_characters.models import Character, Universe, Powers_character


# yes
def view_database(request):
    characters_list = Character.objects.all()
    return render(request, 'characters/view_characters.html', {'characters':characters_list})


@login_required
def create(request):
    form = CharacterForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "characters/save_characters.html", context)


@login_required
def delete(request, id):
    character = Character.objects.get(id=id)
    if request.method == 'POST':
        character.delete()
        return redirect('view_characters')
    return render(request, {'character': character})


def filter_oneCharacter(request):
    name_search = request.POST.get('name_character', False)
    filter_name = Character.objects.filter(name=name_search)
    return render(request, 'characters/filter_characters.html', {'filter_name': filter_name})


def filter__by_universe(request, id):
     oneUniverse = Character.objects.select_related('universe')
     characters_uni = Character.objects.filter(universe__id=id)
     return render(request, 'characters/characters_by_universe.html', {'characters_uni': characters_uni})


@login_required
def update_character(request, id):
    character = Character.objects.get(id=id)
    character_form = CharacterForm(request.POST or None, instance=character)
    if character_form.is_valid():
        character_form.save()
        return redirect('/characters/detail/'+id)
    context = {
        'character_form': character_form
    }
    return render(request, 'characters/update_character.html', context)


# yes
def detail_character(request, id):
    data = Character.objects.get(id=id)
    data_power = Powers_character.objects.all().filter(characters_id=id)

    return render(request, 'characters/detail_character.html', {'data': data, 'data_power': data_power})
