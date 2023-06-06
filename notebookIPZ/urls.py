from django.contrib import admin
from django.urls import path
from todo import views as todo_views
from authentication import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page
    path('', authentication_views.home, name='home'),

    # Authentication
    path('signup/', authentication_views.signup_user, name='signup'),
    path('login/', authentication_views.login_user, name='login'),
    path('logout/', authentication_views.logout_user, name='logout'),

    # Todos
    # ---- Work with Weeks
    path('week_list/', todo_views.week_list, name='week_list'),
    path('week_list_archive/', todo_views.week_list_archive, name='week_list_archive'),
    path('week/<int:week_pk>', todo_views.week_show, name='week_show'),
    path('week/week_create', todo_views.week_create, name='week_create'),
    path('week/<int:week_pk>/week_delete', todo_views.week_delete, name='week_delete'),
    path('week/<int:week_pk>/week_edit', todo_views.week_edit, name='week_edit'),
    path('week/<int:week_pk>/week_archive', todo_views.week_archive, name='week_archive'),
    path('week/<int:week_pk>/week_unarchive', todo_views.week_unarchive, name='week_unarchive'),
    # ---- Work with Todos
    path('week/<int:week_pk>/todo_create', todo_views.todo_create, name='todo_create'),
    path('week/<int:week_pk>/todo_edit/<int:todo_pk>', todo_views.todo_edit, name='todo_edit'),
    path('week/<int:week_pk>/todo_delete/<int:todo_pk>', todo_views.todo_delete, name='todo_delete'),
]
