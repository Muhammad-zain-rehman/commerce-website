from django.urls import path
from api import views

urlpatterns = [
    # For Categories
                  path('', views.CategoryApiViewPublic.as_view()),
                  path('add/', views.CategoryApiView.as_view()),
                  path('update/<int:pk>', views.CategoryApiView.as_view()),
                  path('partially_update/<int:pk>', views.CategoryApiView.as_view()),

    # For Products
                  path('products', views.ProductApiViewPublic.as_view()),
                  path('products-add/', views.ProductApiView.as_view()),
                  path('products-update/<int:pk>', views.ProductApiView.as_view()),
                  path('products-partially_update/<int:pk>', views.ProductApiView.as_view()),

              ]



