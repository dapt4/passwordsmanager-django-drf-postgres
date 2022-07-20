from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('signin', views.signin),
    path('pass', views.list_pass),
    path('pass/new', views.new_pass),
    path('pass/<int:id>', views.get_pass),
    path('pass/del/<int:id>', views.delete_pass),
    path('pass/put/<int:id>', views.edit_pass),
]
