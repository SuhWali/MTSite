# MTSites CSS Integration

This project uses SCSS partials to organize and compile all CSS styles. The previous `MTSites.css` has been integrated into a modular SCSS structure.

## Structure

- `static/scss/main.scss` - Contains Bootstrap imports and basic variables
- `static/scss/main-compiled.scss` - The main file that imports all partials for compilation
- `static/scss/partials/` - Contains individual component partial files:
  - `_menus.scss` - Menu and navigation styles
  - `_translation-selector.scss` - Translation selector styling
  - `_carousel.scss` - Carousel components and animations
  - `_section.scss` - Section layouts and headers
  - `_buttons.scss` - Custom button styles
  - `_utilities.scss` - Helper classes and utilities
- `static/js/menu.js` - JavaScript for handling menu interactions on touch devices

## How to Compile CSS

1. Make sure you have Node.js and npm installed
2. Run `npm install` to install dependencies
3. Run one of the following commands:
   - `npm run scss` - Compile SCSS to CSS once
   - `npm run scss:watch` - Watch for changes and compile automatically
   - `npm run build` - Build for production

## Modifying Styles

1. Edit the appropriate SCSS partial based on what you're changing
2. If adding new component styles, create a new partial in `partials/` and import it in `main-compiled.scss`
3. Use Bootstrap variables (like `var(--bs-primary)`) for consistent theming

## Adding New Components

To add a new component:
1. Create a new partial file in the `partials/` directory with a leading underscore (e.g., `_new-component.scss`)
2. Add your styling inside using SCSS syntax
3. Import the partial in `main-compiled.scss`

## Menu System

The navigation system includes:
1. **Responsive menus** that work on desktop, tablet, and mobile
2. **Multi-level submenus** with proper positioning
3. **Touch device compatibility** through the menu.js script
4. **RTL language support** for Arabic and other right-to-left languages

To use the menu system:
- Include menu.js in your template before the closing body tag
- Use the proper HTML structure with `.menu-item`, `.menu-link`, and `.sub-menu` classes
- Add the `.has-children` class to parent menu items with submenus

## Theme Customization

To change theme colors:
1. Edit the color variables in `main.scss`
2. Recompile CSS using one of the commands above

## Bootstrap Integration

This project extends Bootstrap 5. All Bootstrap components and utilities are available. 