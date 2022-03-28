from django.urls import path
from . import views
from .views import ComidaListView, ComidaCreateView, ComidaDeleteView, ComidaUpdateView

urlpatterns = [
    path('', ComidaListView.as_view(), name='testApp-home'),
    path('comida/new', ComidaCreateView.as_view(), name='testApp-create'),
    path('comida/<int:pk>/delete/', ComidaDeleteView.as_view(), name='testApp-delete'),
    path('comida/<int:pk>/update/', ComidaUpdateView.as_view(), name='testApp-update'),
    path('about/', views.about, name='testApp-about'),
]
