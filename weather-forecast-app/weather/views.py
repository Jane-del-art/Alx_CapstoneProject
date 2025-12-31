from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import SearchHistory
from .forms import WeatherSearchForm
from .services import get_weather_data

def home(request):
    """
    Homepage view - displays search form
    """
    form = WeatherSearchForm()
    searches_count = SearchHistory.objects.count()
    
    context = {
        'form': form,
        'searches_count': searches_count,
    }
    return render(request, 'weather/home.html', context)

def get_weather(request):
    """
    Handle weather search and display results
    """
    if request.method == 'POST':
        form = WeatherSearchForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            
            try:
                # Get weather data from API
                weather_data = get_weather_data(city_name)
                
                # Save search to database
                search_record = SearchHistory.objects.create(
                    city_name=weather_data['city_name'],
                    temperature=weather_data['temperature'],
                    weather_description=weather_data['weather_description'],
                    humidity=weather_data['humidity'],
                    wind_speed=weather_data['wind_speed'],
                    country=weather_data['country'],
                )
                
                # Display results
                context = {
                    'weather': weather_data,
                    'search_record': search_record,
                }
                return render(request, 'weather/result.html', context)
                
            except Exception as e:
                # Handle errors
                context = {
                    'error_message': str(e),
                    'city_name': city_name,
                }
                return render(request, 'weather/error.html', context)
    
    # If not POST or form invalid, redirect to home
    return redirect('home')

def search_history(request):
    """
    Display all search history
    """
    searches = SearchHistory.objects.all().order_by('-date_searched')
    context = {'searches': searches}
    return render(request, 'weather/history.html', context)

def clear_history(request):
    """
    Clear all search history - DEBUG VERSION
    """
    print("\n" + "="*60)
    print(" CLEAR HISTORY FUNCTION CALLED ")
    print(f" Request Method: {request.method}")
    print(f" Request Path: {request.path}")
    print(f" User: {request.user}")
    print(f" POST data: {request.POST}")
    
    if request.method == 'POST':
        print(" POST request received!")
        
        # Check CSRF token
        if not request.POST.get('csrfmiddlewaretoken'):
            print(" ERROR: CSRF token missing!")
        else:
            print(" CSRF token present")
        
        try:
            # Get count before deletion
            count = SearchHistory.objects.count()
            print(f" Records before: {count}")
            
            if count > 0:
                # Delete all history
                deleted_count = SearchHistory.objects.all().delete()
                print(f"  Deleted: {deleted_count}")
                
                # Verify deletion
                count_after = SearchHistory.objects.count()
                print(f" Records after: {count_after}")
                
                # Add success message
                msg = f'Successfully cleared {count} search records.'
                messages.success(request, msg)
                print(f" Success message: {msg}")
            else:
                print(" No records to delete")
                messages.info(request, 'No search history to clear.')
                
        except Exception as e:
            # Add error message
            error_msg = f'Error clearing history: {str(e)}'
            messages.error(request, error_msg)
            print(f" ERROR: {error_msg}")
            import traceback
            traceback.print_exc()
    
    else:
        print(f"  Not a POST request (method: {request.method})")
        messages.error(request, 'Invalid request method.')
    
    print(f" Redirecting to history page")
    print("="*60 + "\n")
    return redirect('history')
