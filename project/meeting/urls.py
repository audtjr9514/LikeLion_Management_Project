from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name="new"),
    path('detail/', views.detail, name="detail"),
    path('<int:blog>', views.detail, name="detail")
]
