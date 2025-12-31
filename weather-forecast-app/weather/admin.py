from django.contrib import admin
from .models import SearchHistory

@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'temperature', 'weather_description', 'country', 'date_searched')
    list_filter = ('country', 'date_searched')
    search_fields = ('city_name', 'country')
    readonly_fields = ('date_searched',)
    ordering = ('-date_searched',)
