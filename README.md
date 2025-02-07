<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping Cart  with a Blog Application by Charles Walton</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        h1, h2 { color: #333; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        table, th, td { border: 1px solid #ddd; }
        th, td { padding: 10px; text-align: left; }
        th { background: #f4f4f4; }
    </style>
</head>
<body>
    <h1>Shopping Cart with a Blog Application</h1>
    
    <h2>Overview</h2>
    <p>This is a Django-based Shopping Cart application that allows login users to browse products, add items to their cart, and proceed with a checkout process.</p>
    
    <h2>Features</h2>
    <ul>
        <li>User authentication (Login/Signup)</li>
        <li>Product listing and details</li>
        <li>Add to cart functionality</li>
        <li>Update and remove items from cart</li>
        <li>Checkout process with order summary</li>
        <li>Admin panel for product management</li>
    </ul>
    
    <h2>Technologies Used</h2>
    <ul>
        <li>Django</li>
        <li>SQLite/PostgreSQL (Database)</li>
        <li>Bootstrap (Frontend)</li>
    </ul>
    
    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/cwalton133/ProductOrder_with_Blog.git
cd shopping-cart</code></pre>
        </li>
        <li>Create a virtual environment and activate it:
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
        </li>
        <li>Install dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Apply migrations:
            <pre><code>python manage.py migrate</code></pre>
        </li>
        <li>Create a superuser:
            <pre><code>python manage.py createsuperuser</code></pre>
        </li>
        <li>Run the development server:
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li>Access the application at <code>http://127.0.0.1:8000/</code></li>
    </ol>
    
    <h2>API Endpoints</h2>
    <table>
        <tr>
            <th>Endpoint</th>
            <th>Method</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>/api/products/</td>
            <td>GET</td>
            <td>List all products</td>
        </tr>
        <tr>
            <td>/api/cart/</td>
            <td>GET</td>
            <td>View cart items</td>
        </tr>
        <tr>
            <td>/api/cart/add/</td>
            <td>POST</td>
            <td>Add item to cart</td>
        </tr>
        <tr>
            <td>/api/cart/remove/</td>
            <td>DELETE</td>
            <td>Remove item from cart</td>
        </tr>
        <tr>
            <td>/api/checkout/</td>
            <td>POST</td>
            <td>Checkout process</td>
        </tr>
    </table>
    
    <h2>API End points</h2>
    <p>The above listed API Endpoints will be added soon.</p>
    
    <h2>Contributing</h2>
    <p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p>
    
    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>
</body>
</html>
