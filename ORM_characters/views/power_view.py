from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ORM_characters.models import Powers
from ORM_characters.forms.power_from import PowersForm


def view_database(request):
    porwers_list = Powers.objects.all()
    return render(request, 'powers/view_powers.html', {'powers_list': porwers_list})


@login_required
def delete(request, id):
    power = Powers.objects.get(id=id)
    if request.method == 'POST':
        power.delete()
        return redirect('see_powers')
    return render(request, {'power': power})

@login_required
def update_power(request, id):
    power = Powers.objects.get(id=id)
    power_form = PowersForm(request.POST or None, instance=power)
    if power_form.is_valid():
        power_form.save()
        return redirect('/power/detail/'+id)
    context = {
        'power_from': power_form
    }
    return render(request, 'powers/update_power.html', context)


def detail_power(request, id):
    context={}
    context['data'] = Powers.objects.get(id=id)
    return render(request, 'powers/detail_power.html', context)