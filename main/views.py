from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .permissions import IsEmployerOrReadOnly,IsApplicantOrReadOnly
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import (
    Vacancy,
    Employer,
    Category,
    Applicant,
    Resume,
    Favorite,
    Application,
)
from .serializers import (
    Register,
    LoginSerialiser,
    ApplicantSerialisers,
    ResumeSerialisers,
    VacancySerialisers,
    EmployerSerialisers,
    FavoriteSerializer,
    CategorySerializer,
    ApplicationSerializers
)

class VacancyListCreateView(ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerialisers
    permission_classes = [IsEmployerOrReadOnly]
    django_filter = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['title','city']
    search_filter = ['title','description']
    ordering_fields = ['salary_to', 'created_at']
class VacancyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerialisers
    permission_classes = [IsEmployerOrReadOnly]

class EmployerListCreateView(ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerialisers
    django_filter = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = ['user','city']
    search_filter = ['user','description']
    ordering_fields = ['company_name', 'user']
class EmployerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerialisers

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    django_filter = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    ordering_fields = ['name']
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ApplicantListCreateView(ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerialisers
    django_filter = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = ['user','city']
    search_filter = ['user','phone']
    ordering_fields = ['user', 'city']
class ApplicantRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerialisers

class ResumeListCreateView(ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerialisers
    permission_classes = [IsApplicantOrReadOnly]
    django_filter = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = ['profession','skills']
    search_filter = ['profession','experience']
    ordering_fields = ['experience', 'expected_salary']
class ResumeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerialisers
    permission_classes = [IsApplicantOrReadOnly]

class FavoriteListCreateView(ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class FavoriteUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    
class ApplicationListCreateView(ListCreateAPIView):
    serializer_class = ApplicationSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(
            applicant=self.request.user.applicant
        )

    def perform_create(self, serializer):
        serializer.save(
            applicant=self.request.user.applicant
        )
class ApplicationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(
            applicant=self.request.user.applicant
        )
    
@api_view(['POST'])
def register (request):

    serializers = Register(data = request.data)
    if serializers.is_valid():
        user = serializers.save()

        return Response(
                {
                    'Answer':'Successfull',
                    'username':user.username
                },
                status= status.HTTP_201_CREATED
            )
    return Response(
        serializers.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
def login(request):
    serializers = LoginSerialiser(
        data = request.data
    )
    if serializers.is_valid():
        user = serializers.validated_data['user']

        token, created = Token.objects.get_or_create(
            user = user 
        )
        return Response({
            'massages':'Login Successfull',
            'token':token.key
        })
    return Response(
        serializers.errors,
        status=400
    )

@api_view(['POST'])
def logout (request):
    if request.user.is_authenticated:
        Token.objects.filter(
            user=request.user
        ).delete()
        return Response({
            'massages':'Logout successfull'
        })
    return Response({
        'massages':'Не был авторизован!'
    })


