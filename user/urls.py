from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('product/', views.product, name='product'),  # Ensure this is present
]