from flask import Flask, render_template, request, redirect, url_for, flash
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Sample project data (could be from a database in a real app)
projects = [
    {
        'title': 'Project 1',
        'description': 'A web application for task management.',
        'image': 'project1.jpg',
        'link': 'https://example.com/project1'
    },
    {
        'title': 'Project 2',
        'description': 'E-commerce platform with payment integration.',
        'image': 'project2.jpg',
        'link': 'https://example.com/project2'
    },
    {
        'title': 'Project 3',
        'description': 'Portfolio website with Flask and Jinja.',
        'image': 'project3.jpg',
        'link': 'https://example.com/project3'
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Validation
        if not all([name, email, subject, message]):
            flash('All fields are required!')
            return redirect(url_for('contact'))
        
        if '@' not in email or '.' not in email:
            flash('Invalid email format!')
            return redirect(url_for('contact'))
        
        if len(message) > 500:
            flash('Message must be 500 characters or less!')
            return redirect(url_for('contact'))

        # Log form details to terminal
        logger.info("New Contact Form Submission:")
        logger.info(f"Name: {name}")
        logger.info(f"Email: {email}")
        logger.info(f"Subject: {subject}")
        logger.info(f"Message: {message}")
        logger.info("-" * 50)  # Separator for readability

        return render_template('success.html', name=name, email=email, subject=subject, message=message)
    
    return render_template('contact.html')

@app.route('/success')
def success():
    return redirect(url_for('contact'))  # Direct access to success redirects to contact

if __name__ == '__main__':
    app.run(debug=True)