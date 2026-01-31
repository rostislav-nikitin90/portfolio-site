# Overview

This portfolio application is a **Django-based web project** designed to showcase my work in web development and graphic design. It demonstrates how Django views, templates, and static files integrate to create a responsive, interactive portfolio site. The app includes three main sections:

- **Home Page** – introduces me and highlights my latest project.  
- **Projects Page** – displays a gallery of projects with filtering by category (Web Development or Graphic Design). Each project includes a modal with detailed information.  
- **Contact Page** – provides a contact form where visitors can send a message, with a thank‑you confirmation displayed upon submission.  

The site uses Django’s template inheritance (`base.html`) for consistent layout, dynamic data passed through `views.py`, and custom CSS for styling and responsiveness.

# Requirements

Before running the application, make sure you have the following installed:

- **Python 3.10+**  
- **pip** (Python package manager)  
- **Git** (for cloning the repository)  
- **Virtual environment support** (`venv` comes bundled with Python 3.3+)  

All required Python libraries are listed in the `requirements.txt` file. The most important dependency is **Django**.

To install dependencies manually:
   ```bash
   pip install -r requirements.txt
   ```

# Running the Test Server

Follow these steps to run the portfolio application locally on your computer:

1. **Clone the repository from GitHub**  
   ```bash
   git clone https://github.com/rostislav-nikitin90/portfolio-site.git
   cd portfolio-site
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
3. **Install dependencies from requirements.txt**
   ```bash
   pip install -r requirements.txt
4. **Apply database migrations (required by Django even if you don’t use a database yet)**
   ```bash
   python manage.py migrate
5. **Start the Django development server**
   ```bash
   python manage.py runserver
6. **Open the application in your browser** 
   ```bash
   http://127.0.0.1:8000/
   ```
   This will display the **Home Page** of the portfolio app.
7. **Deactivate the virtual environment when finished**
   ```bash
   deactivate
   ```

# Purpose

I built this portfolio application as part of my journey to grow as a software engineer. My goals are:

- **Practice Django fundamentals** such as views, templates, and context data.  
- **Apply responsive design principles** and improve my front‑end skills with HTML and CSS.  
- **Showcase my projects** in a professional way that demonstrates both technical and creative abilities.  
- **Gain experience in structuring real applications**, preparing me for larger projects and future career opportunities.  

# Web Pages

This portfolio application consists of several interconnected web pages. Each page extends the base layout (`base.html`) to ensure a consistent design, while Django views and context data dynamically generate content.

## Home Page (`home.html`)
- **Purpose:** Introduces me and highlights my latest project.
- **Dynamic Content:**  
  - My name and surname are passed from `views.py` and displayed using template variables.  
  - The latest project’s title, description, and tools are dynamically inserted from the context dictionary.  
- **Transition:** Visitors can navigate to the **Projects** page or **Contact** page using the navigation menu.

## Projects Page (`projects.html`)
- **Purpose:** Displays a gallery of all projects with filtering options.
- **Dynamic Content:**  
  - A list of projects is passed from `views.py`. Each project includes a title, short description, long description, tools, image, category, and external link.  
  - The filter form allows users to select a category (Web Development or Graphic Design). The view filters projects accordingly and re-renders the page.  
  - Clicking on a project opens a modal window with detailed information, dynamically populated from the project dictionary.  
- **Transition:** Users can return to the **Home** page or go to the **Contact** page via the navigation menu.

## Contact Page (`contact.html`)
- **Purpose:** Provides a form for visitors to send a message.
- **Dynamic Content:**  
  - If the form is submitted, the view captures the visitor’s name, email, and message, and displays a thank‑you confirmation message dynamically.  
  - If not submitted, the page shows the contact form with CSRF protection.  
- **Transition:** Users can navigate back to the **Home** or **Projects** page using the navigation menu.

## Base Layout (`base.html`)
- **Purpose:** Defines the common structure for all pages, including the header, navigation menu, footer, and placeholders for page‑specific content.  
- **Dynamic Content:**  
  - The page title and heading are overridden by child templates.  
  - Navigation links highlight the active page dynamically using Django’s `request.resolver_match.url_name`.

### Page Transitions
- The navigation bar at the top of every page allows smooth transitions between **Home**, **Projects**, and **Contact**.  
- Each page inherits the same layout, so the user experience remains consistent.  
- Dynamic data ensures that content changes depending on the page context, while the overall design stays uniform.

# Development Environment

## Tools Used
This portfolio application was developed using the following tools:

- **Django Framework** – for building the web application, handling views, templates, and routing.  
- **Python Virtual Environment (`venv`)** – to isolate dependencies and ensure reproducibility across different systems.  
- **Git & GitHub** – for version control and publishing the project repository.  
- **Visual Studio Code (VS Code)** – as the primary code editor.  
- **Browser Developer Tools** – for testing responsiveness, debugging CSS, and verifying cross‑browser compatibility.  

## Programming Language and Libraries
- **Programming Language:**  
  - **Python 3.10+** – used for Django views, and managing the application structure.  

- **Libraries and Dependencies (from `requirements.txt`):**  
  - **Django** – the main web framework powering the app.  
  - **asgiref** – provides asynchronous support for Django.  
  - **sqlparse** – used internally by Django for SQL parsing.  
  - **tzdata** – ensures proper timezone handling.  

- **Front‑End Technologies:**  
  - **HTML5** – for structuring the web pages.  
  - **CSS3** – for styling, layout, and responsive design.  

# Useful Websites

* [Django Official Documentation](https://docs.djangoproject.com/en/stable/) – The primary reference for Django, covering models, views, templates, and deployment.  
* [Python Official Documentation](https://docs.python.org/3/) – Comprehensive guide to Python syntax, libraries, and best practices.  
* [MDN Web Docs – HTML & CSS](https://developer.mozilla.org/en-US/docs/Learn) – Beginner‑friendly tutorials on HTML and CSS, essential for front‑end styling.  
* [Django Girls Tutorial](https://tutorial.djangogirls.org/) – A step‑by‑step introduction to building a Django project, perfect for beginners.  
* [Real Python – Django Tutorials](https://realpython.com/tutorials/django/) – In‑depth articles and video tutorials on Django and Python development.  
* [Programming with Mosh YouTube Channel](https://www.youtube.com/watch?v=rHux0gMZ3Eg) – Django Tutorial for Beginners.  

# Future Work

There are several improvements and additions planned for this portfolio application to make it more robust and professional:

- **Enhance Contact Form Functionality**  
  Add backend email integration so that submitted messages are sent directly to my inbox, rather than just displaying a thank‑you message.

- **Add User Authentication**  
  Implement login/logout functionality to allow secure access to an admin dashboard for managing projects and content.

- **Expand Project Showcase**  
  Include more detailed case studies, screenshots, and links to GitHub repositories for each project.


