from django.urls import path
from profiles_api import views

urlpatterns = [
    # note -> rendering api view here is calling the relevant function
    path('test-view/', views.TestApiView.as_view())
]
