from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>', views.finches_detail, name='detail'),
    path('finches/create', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/assoc_trinket/<int:trinket_id>/', views.assoc_trinket, name='assoc_trinket'),
    path('finches/<int:finch_id>/remove_trinket/<int:trinket_id>/', views.remove_trinket, name='remove_trinket'),
    path('trinkets/', views.TrinketList.as_view(), name='trinkets_index'),
    path('trinkets/<int:pk>/', views.TrinketDetail.as_view(), name='trinkets_detail'),
    path('trinkets/create/', views.TrinketCreate.as_view(), name='trinkets_create'),
    path('trinkets/<int:pk>/update/', views.TrinketUpdate.as_view(), name='trinkets_update'),
    path('trinkets/<int:pk>/delete/', views.TrinketDelete.as_view(), name='trinkets_delete'),
    path('accounts/signup/', views.signup, name='signup'),

]


