from django.urls import path, include
from products import views

urlpatterns = [
    # http://localhost:8000/api/v1/latest-products /
    path('latest-products/', views.LatestProductsView.as_view())
]

