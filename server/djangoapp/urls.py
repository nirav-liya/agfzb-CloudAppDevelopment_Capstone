from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
     path(route='', view=views.get_dealerships, name='index'),
    # path for about view
    path('about/', view=views.about, name='about'),
    # path for contact us view
     path('contact/', view=views.contact, name='contact'),
    # path for registration

    # path for login

    # path for logout
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
   

    # path for dealer reviews view
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    # path for add a review view
    path(route='dealer/<int:dealer_id>/add-review/', view=views.add_review, name="add_review")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)