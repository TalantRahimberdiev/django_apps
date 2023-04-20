from django.urls import path
from .views import *
urlpatterns=[
    path('list/', StudiesList.as_view(), name='studies-list'),
    path('list/create/',StudiesCreate.as_view(),name='create'),
    path('list/update/<int:pk>/',StudiesUpdate.as_view(),name='study-update'),
    path('list/delete/<int:pk>/',StudiesDelete.as_view(),name='study-delete'),
    path('list/detail/<int:pk>/',StudiesDetail.as_view(),name='detail'),
]