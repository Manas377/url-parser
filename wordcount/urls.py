from django.urls import path
from .views import frequency, result
from django.shortcuts import redirect
urlpatterns = [
    path("", frequency, name='frequency'),
    path("result/", result, name='result'),
    path("try-again/", lambda request: redirect(frequency, permanent=True), name='re-try'),
]