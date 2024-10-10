from django.urls import path
from . import views


urlpatterns = [
    path('', views.GeeksCreate.as_view(), name='create'),
    path('list/', views.GeeksList.as_view(), name='list'),
    path('detail/<pk>/', views.GeeksDetailView.as_view(), name='detail'),
    path('update/<pk>/', views.GeeksUpdateView.as_view(), name='update'),
    path('delete/pk/', views.GeeksDeleteView.as_view()),
    path('form/', views.GeeksFormView.as_view(), name='form'),
]



