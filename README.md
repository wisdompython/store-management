# 🛒 Simple E-commerce API

Welcome to the **Simple E-commerce API** project! This API serves as an inventory management system for a basic e-commerce platform, allowing users to register, authenticate, manage products, and place orders.

## 🚀 Project Overview

This project demonstrates my proficiency in building scalable backend systems using Django and Django REST Framework. It showcases key functionalities including user authentication, product management, and order processing, all integrated with a PostgreSQL database and deployed on a cloud server.

### Key Technologies & Tools:
- **Django & Django REST Framework**: Backend framework
- **PostgreSQL**: Database for data management
- **JWT Authentication**: Secure user authentication


---

## 📋 Features

### 1. **User Management**
- **User Registration**: New users can register and create an account.
- **User Login**: Registered users can log in with JWT authentication.
  
### 2. **Product Management**
- **Category & Product Models**: Create and manage categories and products.
- **CRUD Operations**: Create, retrieve, update, and delete products.
  
### 3. **Order Management**
- **Order Creation**: Users can place orders with multiple products.
- **Order History**: Retrieve past orders for authenticated users.

### 4. **Other Features**
- **Search**: Search for products based on name and category.
- **Pagination**: Paginate product listings for efficient browsing.

---


## 🔐 Endpoints

### **Authentication**
- **POST** `/api/register/` - Register a new user
- **POST** `/api/login/` - Login and obtain a JWT token

### **Products**
- **GET** `/api/products/` - List all products (supports search and pagination)
- **POST** `/api/products/` - Create a new product (Admin only)
- **PUT** `/api/products/<id>/` - Update product details (Admin only)
- **DELETE** `/api/products/<id>/` - Delete a product (Admin only)

### **Orders**
- **POST** `/api/orders/` - Place a new order
- **GET** `/api/orders/history/` - Get order history for the authenticated user

---

## 🧪 Testing

To run the test suite:

```bash
python manage.py test
```

This includes unit tests for all critical endpoints to ensure system reliability.
