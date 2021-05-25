from django.contrib import admin
from django.urls import path
from characters.views import character_views
from characters.views import universe_views
from characters.views import user_views
from characters.views import home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home
    path('home/', home_views.show, name='home'),

    # characters' urls.
    path('characters/', character_views.list, name="characters"),
    path('characters/save/', character_views.save, name="save_character"),
    path('characters/edit/<int:id>/', character_views.edit, name="edit_character"),
    path('characters/update/<int:id>/', character_views.update, name="update_character"),
    path('characters/delete/<int:id>/', character_views.delete, name="delete_character"),

    # universes' urls.
    path('universes/', universe_views.list, name='universes'),
    path('universes/create/', universe_views.create, name="save_universe"),
    path('universes/edit/<int:id>/', universe_views.edit, name="edit_universe"),
    path('universes/update/<int:id>/', universe_views.update, name="update_universe"),
    path('universes/delete/<int:id>/', universe_views.delete, name="delete_universe"),

    # user's views
    path('login/', user_views.login_view, name="login"),
    path('users/logout/', user_views.logout_view, name='logout'),
]
