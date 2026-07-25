from django.db import models


class Prediction(models.Model):

    image = models.ImageField(upload_to="uploads/")

    prediction = models.CharField(max_length=20)

    confidence = models.FloatField()

    ai_report = models.TextField(blank=True)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction} ({self.confidence:.2f}%)"