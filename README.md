# Products Application

This is a Django-based web application that manages online products, users, orders, and blog posts. It comprises four primary applications: **Users**, **Products**, **Orders**, and **Blog**. This README provides an overview of the project, installation instructions, usage, and more.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Management**: 
  - User registration, login, and profile management.
  
- **Product Catalog**: 
  - Add, edit, and delete products.
  - Categorize products and manage inventory.
  
- **Order Processing**: 
  - Create and manage customer orders.
  - Integrate payment processing (if applicable).
  
- **Blog**: 
  - Create, read, update, and delete blog posts.
  - Comment on blog posts and manage discussions.

## Technologies Used

- [Django](https://www.djangoproject.com/) - The PHP framework used for building the web application.
- [Django Rest Framework](https://www.django-rest-framework.org/) - Used for building the REST API.
- [SQLite](https://www.sqlite.org/index.html) - Default database for development.
- [Bootstrap](https://getbootstrap.com/) - For responsive front-end design.
 
## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package manager)
- virtualenv (recommended)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/cwalton133/ProductOrder_with_Blog.git
   cd products_application


### Create a Virtual Environment

   python -m venv venv

   # Activate the virtual environment:

venv\Scripts\activate

   # macOS/Linux:

source venv/bin/activate

   # Install the dependencies

   pip install -r requirements.txt

# Apply migrations:

python manage.py migrate


# Create a superuser (optional but recommended for admin access):


python manage.py createsuperuser

# Run the development server:

python manage.py runserver

Your application should now be running on http://127.0.0.1:8000/.


Usage
Access the application in your web browser using the following URLs:

Home Page: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/ (Use the superuser credentials to log in)
API Documentation: If using Django Rest Framework, ensure you have included the Swagger or similar API documentation.

API Endpoints
Here are some of the main API endpoints:


User

POST /api/users/ - Register a new user.
POST /api/auth/login/ - Log in a user.
Products

GET /api/products/ - List all products.
POST /api/products/ - Create a new product.
Orders

GET /api/orders/ - View all orders.
POST /api/orders/ - Create a new order.
Blog

GET /api/blog/ - List all blog posts.
POST /api/blog/ - Create a new blog post.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License.

Contact
For any questions or feedback, please contact:

Charles Walton - cwalton1335@gmail.com
GitHub: cwalton133
Thank you for checking out the Products Application!


:

