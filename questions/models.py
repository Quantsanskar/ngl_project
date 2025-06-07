from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.TextField()
    ip_address = models.GenericIPAddressField()
    name = models.CharField(max_length=100, blank=True, null=True)
    is_anonymous = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        if self.is_anonymous:
            return f"Anonymous: {self.question_text[:50]}..."
        else:
            return f"{self.name}: {self.question_text[:50]}..."
