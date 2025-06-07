# Anonymous Question Platform (NGL Clone)

A Django-based anonymous question platform similar to NGL (Not Gonna Lie) where users can submit questions anonymously or with their names.

## Features

- 🔒 **Anonymous Questions**: Users can submit questions completely anonymously
- 👤 **Optional Identity**: Users can choose to include their name
- 📱 **Responsive Design**: Works perfectly on mobile and desktop
- 🌐 **IP Tracking**: Tracks IP addresses for moderation purposes
- 📊 **Admin Dashboard**: View all questions with filtering options
- 🚀 **Easy Deployment**: Simple Django setup

## Installation

1. **Clone or download the project files**

2. **Create a virtual environment**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   \`\`\`

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run migrations**
   \`\`\`bash
   python manage.py makemigrations
   python manage.py migrate
   \`\`\`

5. **Create a superuser (optional)**
   \`\`\`bash
   python manage.py createsuperuser
   \`\`\`

6. **Run the development server**
   \`\`\`bash
   python manage.py runserver
   \`\`\`

## Usage

### Main Page
- Visit `http://localhost:8000/` to access the question submission form
- Users can choose between anonymous or named submissions
- Questions are stored in the database with IP addresses

### Admin Dashboard
- Visit `http://localhost:8000/questions/bdhjd/jndj/njf/` to view all submitted questions
- Filter questions by anonymous/named
- View IP addresses and submission timestamps

### Django Admin (Optional)
- Visit `http://localhost:8000/admin/` to access Django's admin interface
- Login with your superuser credentials to manage questions

## Project Structure

\`\`\`
ngl_project/
├── manage.py
├── requirements.txt
├── README.md
├── ngl_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── questions/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── templates/
    └── questions/
        ├── index.html
        └── view_questions.html
\`\`\`

## Configuration

### Security Settings
Before deploying to production:

1. Change the `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS` with your domain
4. Configure a production database (PostgreSQL recommended)

### Environment Variables
For production, consider using environment variables:
- `SECRET_KEY`
- `DEBUG`
- `DATABASE_URL`
- `ALLOWED_HOSTS`

## Deployment

### Vercel Deployment
1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in the project directory
3. Follow the prompts to deploy

### Traditional Hosting
1. Set up a production server (Ubuntu/CentOS)
2. Install Python, pip, and a web server (nginx/Apache)
3. Configure a WSGI server (gunicorn/uWSGI)
4. Set up a production database (PostgreSQL/MySQL)

## Features Explanation

### Anonymous Submissions
- Users can submit questions without providing any personal information
- Only IP address is stored for moderation purposes
- Questions are marked as anonymous in the database

### Named Submissions
- Users can optionally provide their name
- Name is stored along with the question and IP address
- Useful for non-anonymous feedback

### IP Tracking
- All submissions include IP address tracking
- Helps with moderation and spam prevention
- No restrictions on multiple questions from same IP

### Responsive Design
- Mobile-first design approach
- Works seamlessly on all device sizes
- Touch-friendly interface for mobile users

## Customization

### Styling
- Edit the CSS in the HTML templates to match your brand
- Modify colors, fonts, and layout as needed
- All styles are embedded in the templates for easy customization

### Functionality
- Modify `models.py` to add new fields
- Update `views.py` to change business logic
- Customize templates for different layouts

## Support

For issues or questions:
1. Check the Django documentation
2. Review the code comments
3. Test in a development environment first

## License

This project is open source and available under the MIT License.
