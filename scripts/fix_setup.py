#!/usr/bin/env python
"""
Fix setup issues and create necessary directories and migrations.
"""

from django.core.management import execute_from_command_line
import os
import sys
import django

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ngl_project.settings')
django.setup()


def fix_setup():
    """Fix setup issues and create migrations"""

    # Create static directory
    static_dir = os.path.join(project_dir, 'static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
        print(f"Created static directory: {static_dir}")

    # Create templates directory if it doesn't exist
    templates_dir = os.path.join(project_dir, 'templates')
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)
        print(f"Created templates directory: {templates_dir}")

    # Create questions templates directory
    questions_templates_dir = os.path.join(templates_dir, 'questions')
    if not os.path.exists(questions_templates_dir):
        os.makedirs(questions_templates_dir)
        print(
            f"Created questions templates directory: {questions_templates_dir}")

    print("\nCreating migrations for questions app...")
    execute_from_command_line(['manage.py', 'makemigrations', 'questions'])

    print("\nApplying migrations...")
    execute_from_command_line(['manage.py', 'migrate'])

    print("\n✅ Setup complete!")
    print("\nNext steps:")
    print("1. Run: python manage.py runserver")
    print("2. Visit: http://localhost:8000/")
    print("3. Admin dashboard: http://localhost:8000/questions/bdhjd/jndj/njf/")

    print("\nOptional: Create a superuser")
    print("Run: python manage.py createsuperuser")


if __name__ == '__main__':
    fix_setup()
