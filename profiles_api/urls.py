from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

# note router will create urls for you, so no need to specify /
router = DefaultRouter()
router.register('test-viewset', views.TestViewSet, basename='test-viewset')
####
# if queryset provided, no need for basename
router.register('user-profile', views.UserProfileViewSet)

urlpatterns = [
    # note -> rendering api view here is calling the relevant function
    path('test-view/', views.TestApiView.as_view()),
    path('login/', views.UserLogInAPIView.as_view()),
    path('', include(router.urls))
]
