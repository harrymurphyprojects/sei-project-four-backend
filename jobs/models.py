from django.db import models

class Job(models.Model):
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    company_image = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=30)
    salary = models.PositiveIntegerField(blank=True)
    reference_number = models.PositiveIntegerField(unique=True)
    description = models.TextField(max_length=800)
    date_posted = models.DateField()

    def __str__(self):
        return f'{self.position} - {self.company}'

class Application(models.Model):
    ''' Application Model '''
    name = models.CharField(max_length=30)
    contact_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(
      Job,
      related_name='applications',
      on_delete=models.DO_NOTHING
    )
    owner = models.ForeignKey(
      'jwt_auth.User',
      related_name='applications_posted',
      on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Application {self.id} on Job {self.job}'
