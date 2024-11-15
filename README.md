# 🛒 Simple E-commerce API

Hey there! Welcome to my **Simple E-commerce API** project. This is an inventory management system I built for a basic e-commerce platform, where users can register, log in, manage products, and place orders.

## 🚀 Project Overview

This project was a great opportunity for me to dive deeper into Django and Django REST Framework. It's designed to handle core functionalities like user authentication, product management, and order processing, all backed by a PostgreSQL database and deployed on a cloud server for reliability.

### Key Technologies & Tools:
- **Django & Django REST Framework**: For the backend logic and API handling.
- **PostgreSQL**: For storing data efficiently.
- **JWT Authentication**: To keep user data secure and authenticated.

---

## 📋 Features

### 1. **User Management**
- **User Registration**: New users can sign up and create an account.
- **User Login**: Existing users can log in using JWT for secure authentication.
  
### 2. **Product Management**
- **Categories & Products**: Manage categories and products seamlessly.
- **CRUD Operations**: Easily add, view, update, or delete products.
  
### 3. **Order Management**
- **Placing Orders**: Users can place orders with multiple products in their cart.
- **Order History**: Users can view their past orders at any time.

### 4. **Other Cool Features**
- **Search**: Quickly find products by name or category.
- **Pagination**: Browse products smoothly with paginated results.

---

## 🔐 Endpoints Overview

Here's a quick look at the main endpoints:

### **Authentication**
- **POST** `/api/register/` - Sign up a new user.
- **POST** `/api/login/` - Log in and get a JWT token.

### **Products**
- **GET** `/api/products/` - List all products (supports search and pagination).
- **POST** `/api/products/` - Add a new product (Admin only).
- **PUT** `/api/products/<id>/` - Update a product.
- **DELETE** `/api/products/<id>/` - Remove a product.

### **Orders**
- **POST** `/api/orders/` - Place a new order.
- **GET** `/api/orders/history/` - View your order history (for logged-in users).

---

## 🧪 Testing

To make sure everything works smoothly, I've added unit tests for all key endpoints. You can run them using:

```bash
python manage.py test
```



