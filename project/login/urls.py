from django.urls import path
from .views import login, signup, submit, home, voting, hasil, about, BerhasilVoting


urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('submit/', submit, name='submit'),
    path('login/', login, name='login'),
    path('voting/', voting, name='voting'),
    path('hasil/', hasil, name='hasil'),
    path('about/', about, name='about'),
    path('BerhasilVoting/', BerhasilVoting, name='BerhasilVoting'),
]
