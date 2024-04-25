from django.urls import path
from .views import register_user, user_login, user_logout, list_users, SatisfactionSurveyViewSet, RecognitionViewSet, KaizenViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'surveys', SatisfactionSurveyViewSet)
router.register(r'recognitions', RecognitionViewSet)
router.register(r'kaizens', KaizenViewSet)

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('users/', list_users, name='list_users'),
    path('surveys/', SatisfactionSurveyViewSet.as_view({'get': 'list', 'post': 'create'}), name='survey-list'),
    path('surveys/<int:pk>/', SatisfactionSurveyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='survey-detail'),
    path('recognitions/', RecognitionViewSet.as_view({'get': 'list', 'post': 'create'}), name='recognition-list'),
    path('recognitions/<int:pk>/', RecognitionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='recognition-detail'),
    path('kaizens/', KaizenViewSet.as_view({'get': 'list', 'post': 'create'}), name='kaizen-list'),
    path('kaizens/<int:pk>/', KaizenViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='kaizen-detail'),
]