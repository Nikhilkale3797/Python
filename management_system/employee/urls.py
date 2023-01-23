
from django.urls import path
from . import views
'''
urlpatterns = [
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('',views.register_view),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home',views.home,name='home'),
    path('add-emp',views.add_employ),
    path('delete<int:Empid>',views.delete_),
    path('update<int:Empid>',views.update_),
    path('do_update<int:Empid>',views.do_update_),
]
'''

urlpatterns = [
    path('',views.add_employ),
    path('add-emp',views.add_employ),
    path('login',views.login_view,name='login'),
    path('register',views.register_view),
    path('home',views.home,name='home'),

]
