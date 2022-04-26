from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ORM_characters.models import Universe
from ORM_characters.forms import UniverseForm


def view_database(request):
    universe_list = Universe.objects.all().order_by('name')
    return render(request, 'universe/view_universe.html', {'universes': universe_list})


@login_required
def create(request):
    form = UniverseForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "universe/create_universe.html", context)


def save(request):
    _name = request.POST["name"]
    _description = request.POST["description"]
    _date_foundation = request.POST["data_foundation"]
    oneUniverse = Universe.objects.create(name=_name, description=_description, date_foundation=_date_foundation)
    return redirect("character")

@login_required
def delete(request, id):
    universe = Universe.objects.get(id=id)
    if request.method == 'POST':
        universe.delete()
        return redirect('view_universe')
    return render(request, {'universe':universe})


def orderBY(request):
    universe = Universe.objects.order_by('-id')
    return render(request, 'universe/view_universe.html',{'universe':universe})
