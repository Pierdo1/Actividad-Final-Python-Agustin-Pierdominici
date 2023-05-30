from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    # path("about/", views.about, name="About"), 
    path("tracker/", views.tracker, name="Tracker"),
    path("products/<int:myid>", views.productview, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("search/", views.search, name="Search"),
    path("contact/", views.contact, name="Contact"),
    
]