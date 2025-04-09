document.addEventListener('DOMContentLoaded', function() {
    // Touch swipe support for carousel
    const carousel = document.getElementById('homeCarousel');
    if (carousel) {
        let touchStartX = 0;
        let touchEndX = 0;

        carousel.addEventListener('touchstart', function(e) {
            touchStartX = e.changedTouches[0].screenX;
        }, false);

        carousel.addEventListener('touchend', function(e) {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        }, false);

        function handleSwipe() {
            const swipeThreshold = 50; // Minimum distance to be considered a swipe
            if (touchEndX < touchStartX - swipeThreshold) {
                // Swipe left - go to next slide
                const nextButton = carousel.querySelector('.carousel-control-next');
                nextButton.click();
            }
            if (touchEndX > touchStartX + swipeThreshold) {
                // Swipe right - go to previous slide
                const prevButton = carousel.querySelector('.carousel-control-prev');
                prevButton.click();
            }
        }

        // Reset animation when slide changes
        carousel.addEventListener('slide.bs.carousel', function() {
            const activeItem = carousel.querySelector('.carousel-item.active');
            const activeImage = activeItem.querySelector('img') || activeItem.querySelector('.bg-light');

            if (activeImage) {
                // Reset the animation
                activeImage.style.animation = 'none';
                activeImage.offsetHeight; // Trigger reflow
                activeImage.style.animation = null;
            }
        });
    }
}); 