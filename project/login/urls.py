from django.urls import path
from .views import user_login, signup, submit, home, voting, hasil, about


urlpatterns = [
    path('', user_login, name='login'),
    path('signup/', signup, name='signup'),
    path('submit/', submit, name='submit'),
    path('home/', home, name='home'),
    path('voting/', voting, name='voting'),
    path('hasil/', hasil, name='hasil'),
    path('about/', about, name='about'),
]