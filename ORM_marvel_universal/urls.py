from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from ORM_characters.views import character_views
from ORM_characters.views import universe_views
from ORM_characters.views import user_view
from ORM_characters.views import index_view
from ORM_characters.views import powers_character_views
from ORM_characters.views import power_view

urlpatterns = [
    path('comics/', index_view.views, name='comics'),
    path('login/', user_view.login_view, name='login'),
    path('logout/', user_view.logout_v, name='logout'),
    path('admin/', admin.site.urls),

    # url of characters
    path('characters/', character_views.view_database, name='view_characters'),
    path('character/save/', character_views.create, name='save_character'),
    url(r'^character/delete_data(?P<id>\d+)/$', character_views.delete, name='delete_character'),
    path('character/filter/', character_views.filter_oneCharacter, name='filter_character'),

    # url of universes
    path('universes/', universe_views.view_database, name='view_universe'),
    path('universe/create', universe_views.create, name="save_universe"),
    url(r'^universe/delete_data(?P<id>\d+)/$', universe_views.delete, name='delete_universe'),

    # view characters by name of universe
    url(r'^charcaters/filter/name(?P<id>\d+)/$', character_views.filter__by_universe, name='character_universe'),

    # updata and datail characters
    url(r'^characters/update/(?P<id>\d+)/$', character_views.update_character, name='update_character'),
    path('characters/detail/<int:id>', character_views.detail_character, name='detail_character'),

    # powers for use table characters...
    path('powers/view/', powers_character_views.view_database, name='view_powers'),
    path('powers/create/', powers_character_views.create, name='create_powers_character'),
    path('powers/create_power/', powers_character_views.create_powers, name='create_powers'),
    url(r'^powers/delete_power_character(?P<id>\d+)/$', powers_character_views.delete, name='delete_powers_character'),
    path('powers/filter/', powers_character_views.filter_character_by_power, name='filter_power'),
    url(r'^powers/update/(?P<id>\d+)/$', powers_character_views.update_pw_ch, name='update_power_ch'),

    # powers...
    url(r'^power/delete_power(?P<id>\d+)/$', power_view.delete, name='delete_powers'),
    path('power/view/', power_view.view_database, name='see_powers'),
    path('power/detail/<int:id>', power_view.detail_power, name='detail_power'),
    url(r'^power/update/(?P<id>\d+)/$', power_view.update_power, name='update_power')

]
