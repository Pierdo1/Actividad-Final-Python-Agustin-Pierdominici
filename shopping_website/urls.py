from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="Home"),
    # path("about/", views.about, name="About"), 
    path("tracker/", views.tracker, name="Tracker"),
    path("products/<int:myid>", views.productview, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("search/", views.search, name="Search"),
    path("contact/", views.contact, name="Contact"),
    path('register/', views.register, name='Register'),
    path("login/", views.login, name="Login"),

]