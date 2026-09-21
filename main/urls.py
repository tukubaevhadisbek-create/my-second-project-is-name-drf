from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    register,
    login,
    logout,
    VacancyListCreateView,
    VacancyRetrieveUpdateDestroyAPIView,
    EmployerListCreateView,
    EmployerRetrieveUpdateDestroyAPIView,
    # CategoryListCreateView,
    # CategoryRetrieveUpdateDestroyAPIView,
    ApplicantListCreateView,
    ApplicantRetrieveUpdateDestroyAPIView,
    ResumeListCreateView,
    ResumeRetrieveUpdateDestroyAPIView,
    FavoriteUpdateDestroyAPIView,
    FavoriteListCreateView,
    ApplicationListCreateView,
    StatisticView,
    CategoryViewSet,
    EmployerApplicationListView,
    EmployerApplicationDetailView,
)
router =DefaultRouter()
router.register(r'category',CategoryViewSet)


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('vacancies/', VacancyListCreateView.as_view(), name='vacancy-list-create'),
    path('vacancies/<int:pk>/', VacancyRetrieveUpdateDestroyAPIView.as_view(), name='vacancy-detail'),

    path('employers/', EmployerListCreateView.as_view(), name='employer-list-create'),
    path('employers/<int:pk>/', EmployerRetrieveUpdateDestroyAPIView.as_view(), name='employer-detail'),

    # path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    # path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),

    path('applicants/', ApplicantListCreateView.as_view(), name='applicant-list-create'),
    path('applicants/<int:pk>/', ApplicantRetrieveUpdateDestroyAPIView.as_view(), name='applicant-detail'),

    path('resumes/', ResumeListCreateView.as_view(), name='resume-list-create'),
    path('resumes/<int:pk>/', ResumeRetrieveUpdateDestroyAPIView.as_view(), name='resume-detail'),

    path('favorites/',FavoriteListCreateView.as_view()),
    path('favorites/<int:pk>/',FavoriteUpdateDestroyAPIView.as_view()),
    path('applications/',ApplicationListCreateView.as_view(),name='application-list-create'),
    path('employer/applications/',EmployerApplicationListView.as_view(),name='employer-application-list'),
    path('employer/applications/<int:pk>/',EmployerApplicationDetailView.as_view(),name='employer-application-detail'),
    path('statistics/', StatisticView.as_view()),
    path('',include(router.urls))
]

