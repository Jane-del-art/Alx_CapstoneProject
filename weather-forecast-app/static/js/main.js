document.addEventListener('DOMContentLoaded', function() {
    console.log('WeatherCast JS loaded');
    
    // ONLY handle weather search forms (not clear history)
    const searchForms = document.querySelectorAll('form[action*="weather"]');
    searchForms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitButton = this.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Loading...';
                submitButton.disabled = true;
            }
        });
    });
    
    // Fade in effect for weather cards
    const weatherCards = document.querySelectorAll('.weather-card');
    weatherCards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
});