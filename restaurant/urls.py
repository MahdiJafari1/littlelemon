from django.urls import path
from . import views

urlpatterns = [
    path("menus/", views.MenuItemsView.as_view()),
    path("menus/<int:pk>", views.SingleMenuItemView.as_view()),
]
