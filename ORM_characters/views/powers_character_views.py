from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ORM_characters.forms.power_from import Powers_characterForm, PowersForm
from ORM_characters.models import Powers_character , Powers


def view_database(request):
    porwers_list = Powers_character.objects.all()
    return render(request, 'powers_characters/view_powers.html', {'powers_list': porwers_list})

@login_required
def create(request):
    form = Powers_characterForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, 'powers_characters/save_power.html', context)

@login_required
def create_powers(request):
    formP = PowersForm(request.POST or None)
    if formP.is_valid():
        formP.save()
        return redirect('create_powers_character')
    context = {
        'formP': formP,
    }
    return render(request, 'powers/create_power.html', context)

@login_required
def delete(request, id):
    power = Powers_character.objects.get(id=id)
    if request.method == 'POST':
        power.delete()
        return redirect('view_powers')
    return render(request, {'power': power})


def filter_character_by_power(request):
    name_power = request.POST.get('search', False)
    filter = Powers_character.objects.filter(powers__name__startswith=name_power)
    return render(request, 'powers_characters/filter_character_power.html', {'filter': filter})


def update_pw_ch(request, id):
    power_ch = Powers_character.objects.get(id=id)
    pw_ch_form = Powers_characterForm(request.POST or None, instance=power_ch)
    if pw_ch_form.is_valid():
        pw_ch_form.save()
        return redirect('view_powers')
    context = {
        'pw_ch_form': pw_ch_form
    }
    return render(request, 'powers_characters/update_power_character.html', context)
