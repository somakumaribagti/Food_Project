from django.urls import path
from Home_App.views import *

urlpatterns = [
    path('',HomeView,name="Home"),
    path('book_table',BookTableView,name="Book_Table"),
    path('menu',MenuView,name="Menu"),
    path('about',AboutView,name="About"),
    path('index.html',SingnUpView,name="handlesignup"),
    path('login/',SignInView,name="handlesignin"),
]
