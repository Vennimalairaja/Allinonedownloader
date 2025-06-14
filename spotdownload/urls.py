from django.urls import path
from .views import Homepage,download_page
urlpatterns=[
    path('',Homepage),
    path('download/',download_page)
]