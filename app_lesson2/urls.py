from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clients/create/', views.create_client_view, name='create_client'),
    path('clients/', views.all_clients_view, name='all_clients'),
    path('clients/<int:client_id>/update/', views.update_client_view, name='update_client'),
    path('clients/<int:client_id>/delete/', views.delete_client_view, name='delete_client'),
    path('clients/<int:client_id>/ordered_products/<int:days>/', views.client_ordered_products, name='client_ordered_products'),

]



