from django.urls import path
from .views import index, signup, logOut
from django.contrib.auth import views as log_views


from .forms import LoginForm
app_name = 'main_app'
urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', log_views.LoginView.as_view(template_name='main_app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/',logOut, name='logout')
    
]
