from django.db import models

class SearchHistory(models.Model):
    """Model to store search history"""
    city_name = models.CharField(max_length=100)
    temperature = models.FloatField(null=True, blank=True)
    weather_description = models.CharField(max_length=100, null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    country = models.CharField(max_length=10, null=True, blank=True)
    date_searched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city_name} - {self.date_searched.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-date_searched']
        verbose_name_plural = 'Search Histories'
