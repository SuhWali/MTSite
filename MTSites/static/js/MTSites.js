// Menu functionality for mobile devices
document.addEventListener('DOMContentLoaded', function() {
    // Initialize mobile menu functionality
    initMobileMenu();
    
    // Listen for window resize events
    window.addEventListener('resize', handleResize);
});

// Initialize mobile menu
function initMobileMenu() {
    // Get all menu items with children
    const menuItemsWithChildren = document.querySelectorAll('.menu-item.has-children');
    
    // Add click event listener to each menu item with children
    menuItemsWithChildren.forEach(function(menuItem) {
        const menuLink = menuItem.querySelector('.menu-link');
        
        if (menuLink) {
            menuLink.addEventListener('click', function(e) {
                // Only intercept clicks on mobile
                if (window.innerWidth <= 992) {
                    e.preventDefault();
                    
                    // Toggle the submenu visibility
                    menuItem.classList.toggle('show-submenu');
                    
                    // Close other open submenus at the same level
                    const siblings = Array.from(menuItem.parentNode.children);
                    siblings.forEach(function(sibling) {
                        if (sibling !== menuItem && sibling.classList.contains('show-submenu')) {
                            sibling.classList.remove('show-submenu');
                        }
                    });
                }
            });
        }
    });
}

// Handle window resize events
function handleResize() {
    // If we're on desktop, remove any show-submenu classes that may have been applied on mobile
    if (window.innerWidth > 992) {
        document.querySelectorAll('.menu-item.show-submenu').forEach(function(item) {
            item.classList.remove('show-submenu');
        });
    }
}
