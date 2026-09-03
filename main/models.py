from django.db import models
from django.contrib.auth.models import User

class Employer (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='employer')
    company_name = models.CharField(verbose_name='Название компании',max_length=150,blank=True)
    descriptions = models.TextField(verbose_name='Описание', blank=True)
    city = models.CharField(max_length=100,verbose_name='Город',blank=True)

    class Meta:
        verbose_name = 'Работадатель'
        verbose_name_plural = 'Работадатели'

    def __str__(self):
        return self.company_name

class Category (models.Model):
    name = models.CharField(verbose_name='Категории работы',max_length=150)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        related_name='vacancies',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='vacancies',
    )

    title = models.CharField(max_length=200,verbose_name='Работа')
    description = models.TextField(verbose_name='Описание')
    city = models.CharField(max_length=100,)
    salary_from = models.PositiveIntegerField(verbose_name='Минимальная зарплата',blank=True,null=True)
    salary_to = models.PositiveIntegerField(verbose_name='Максимальная зарплата',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ваканции'
        verbose_name_plural = 'Ваканции'

    def __str__(self):
        return self.title

class Applicant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='applicant')
    phone = models.CharField(max_length=30,blank=True,verbose_name='Телефон')
    city = models.CharField(max_length=100,verbose_name='Город',blank=True)
    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'

    def __str__(self):
        return self.user.username


class Resume(models.Model):
    applicant = models.OneToOneField(
        Applicant,
        on_delete=models.CASCADE,
        related_name='resume',
        verbose_name='Резюме'
    )

    profession = models.CharField(max_length=150,verbose_name='Професия')
    skills = models.TextField(verbose_name='Навыки')
    experience = models.TextField(verbose_name='Опыт по работе')
    expected_salary = models.PositiveIntegerField(verbose_name='Желаемое зарплата')

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return self.profession

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'vacancy'],
                name='unique_user_vacancy'
            )
        ]

    def __str__(self):
        return f'{self.user} → {self.vacancy}'

class Application(models.Model):
    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.CASCADE
    )

    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )