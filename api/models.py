from django.db import models

class CabinetClickLog(models.Model):
    login = models.CharField(max_length=150)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.login} - {self.action} at {self.timestamp}"

