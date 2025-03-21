﻿# LibraryProject
echo "This is the initial setup of the LibraryProject using Django." >> README.md


admin_interface.md:
# Django Admin Interface for Book Model

## Registration
- The `Book` model is registered in `bookshelf/admin.py` using the `admin.site.register()` method.

## Customization
- The `BookAdmin` class is created to customize the admin display.
- `list_display`: Configures visible fields (`title`, `author`, `publication_year`).
- `search_fields`: Adds a search box for `title` and `author`.
- `list_filter`: Enables filtering by `publication_year`.

## Steps to Verify
1. Run the development server: `python manage.py runserver`.
2. Access the admin interface: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
3. Navigate to the **Bookshelf** section to manage books effectively.

