from django.db import models

class Report(models.Model):
    """ reportes unidad"""

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255,
                                blank=True,
                                null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Attachment(models.Model):
    report = models.ForeignKey(Report, related_name='attachment',
                               on_delete=models.CASCADE)
    
    file = models.FieldFile(upload_to='uploads/')