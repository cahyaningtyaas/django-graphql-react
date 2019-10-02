from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'api/dish/', views.DishListCreate.as_view()),
    url(r'dish/', views.DishIndexView.as_view() ),#, name=dishindex),
    url(r'dish/<int:pk>/', views.DishDetailView.as_view()),#, name=dishdetail),
    url(r'dish/edit/<int:pk>/', views.dishedit),#, name=dishedit),
    url(r'dish/delete/<int:pk>/', views.dishdelete),#, name=dishdelete),
    url(r'dish/dish/',views.dishview),#, name=dishview),
    
]