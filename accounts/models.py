from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    ROLE_CHOICES = (
        (1, 'Admin'),
        (2, 'Usuario'),
    )
    role = models.IntegerField(choices=ROLE_CHOICES) 

    full_name = models.CharField(max_length=255) 

    def __str__(self):
        return self.username
    
class SatisfactionSurvey(models.Model):
    atmosphereRating = models.CharField(max_length=100, blank=True)
    comfortAndMotivation = models.CharField(max_length=100, blank=True)
    supportFromPeersAndSuperiors = models.CharField(max_length=100, blank=True)
    communication = models.CharField(max_length=100, blank=True)
    feelingValued = models.CharField(max_length=100, blank=True)
    constructiveFeedback = models.CharField(max_length=100, blank=True)
    growthOpportunities = models.CharField(max_length=100, blank=True)
    trainingAndDevelopment = models.CharField(max_length=100, blank=True)
    careerAdvancement = models.CharField(max_length=100, blank=True)
    workLifeBalance = models.CharField(max_length=100, blank=True)
    stressManagementSupport = models.CharField(max_length=100, blank=True)
    flexibilityInSchedule = models.BooleanField(default=False)
    overallSatisfaction = models.CharField(max_length=100, blank=True)
    aspectsToImprove = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Satisfaction Survey ({self.date})"


class Recognition(models.Model):
    selected_employee = models.CharField(max_length=100, blank=True)
    selected_recognition = models.CharField(max_length=100, blank=True)
    recognition_message = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Satisfaction Recognition ({self.date})"

class Kaizen(models.Model):
    userId = models.IntegerField()  
    fullName = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    description = models.TextField()
    department = models.CharField(max_length=100)
    area_of_improvement = models.CharField(max_length=100)
    expected_impact = models.TextField()
    required_resources = models.TextField()
    implementation_method = models.TextField()
    evaluation_plan = models.TextField()

    def __str__(self):
        return self.title
    