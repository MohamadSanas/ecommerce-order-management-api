# 🛒 E-Commerce Order Management API

A RESTful backend API for managing an e-commerce platform, including customers, products, inventory, shopping carts, orders, and payments.

Built with **Python, FastAPI, PostgreSQL, and SQLAlchemy 2.0**, following modern backend engineering practices.

> 🚧 **Project Status:** Under Development

## 📌 Project Overview

The E-Commerce Order Management API is a backend application designed to handle the core operations of an online shopping platform.

The system provides APIs for managing users, products, inventory, shopping carts, orders, and payment records. It also implements authentication, authorization, database management, and automated testing.

## 🎯 Project Objectives

- Develop RESTful APIs using FastAPI.
- Implement secure authentication and role-based authorization.
- Design and manage relational databases using PostgreSQL.
- Work with SQLAlchemy 2.0 and Alembic migrations.
- Understand asynchronous programming in Python.
- Implement automated testing using Pytest.
- Use Redis for caching.
- Containerize the application using Docker.

## 🧰 Technology Stack

| Technology     | Purpose                           |
| -------------- | --------------------------------- |
| Python 3.11+   | Backend programming language      |
| FastAPI        | REST API framework                |
| Pydantic       | Data validation and serialization |
| PostgreSQL     | Relational database               |
| SQLAlchemy 2.0 | Object-relational mapping         |
| Alembic        | Database migrations               |
| Redis          | Caching                           |
| Pytest         | Automated testing                 |
| Docker         | Application containerization      |
| Git & GitHub   | Version control                   |

## ✨ Core Features

### 1. Authentication & Authorization

- User registration and login.
- JWT-based authentication.
- Password hashing.
- Role-based access control.

### 2. Product Management

- Create, retrieve, update, and delete products.
- Manage product categories.
- Product search and filtering.
- Manage product pricing and availability.

### 3. Inventory Management

- Track available stock.
- Update inventory quantities.
- Prevent orders exceeding available stock.
- Identify low-stock products.

### 4. Shopping Cart

- Add products to cart.
- Update product quantities.
- Remove cart items.
- Calculate cart totals.

### 5. Order Management

- Create customer orders.
- Track order status.
- Calculate order totals.
- Manage order cancellations.
- Maintain order history.

### 6. Payment Management

- Simulate payment processing.
- Record payment transactions.
- Track payment statuses.
- Associate payments with orders.

## 🏗️ Architecture

The application will initially follow a **Modular Monolith Architecture**.

This approach separates application responsibilities into independent modules while maintaining a single deployable application.

Planned high-level structure:

```text
Client
  |
  v
FastAPI Application
  |
  +-- Authentication
  +-- Product Management
  +-- Inventory Management
  +-- Shopping Cart
  +-- Order Management
  +-- Payment Management
  |
  +-- PostgreSQL
  +-- Redis
```

## 📂 Project Structure

The project will gradually evolve into the following structure:

```text
ecommerce-order-management-api/
│
├── app/
│   ├── main.py
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── api/
│   ├── services/
│   └── repositories/
│
├── alembic/
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── docker-compose.yml
└── README.md
```

## ⚙️ Getting Started

### Prerequisites

Make sure you have installed:

- Python 3.11 or higher
- Git
- PostgreSQL
- Docker Desktop (for containerized development)

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-order-management-api.git

cd ecommerce-order-management-api
```

### Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

> Note: Application dependencies and startup instructions will be updated as development progresses.

## 🧪 Testing

The project will use Pytest for automated testing.

```bash
pytest
```

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

Once the application is running:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

## 🔐 Security

- Passwords will be stored using secure password hashing.
- JWT tokens will be used for authentication.
- Environment variables will be used for sensitive configuration.
- Secrets and credentials must never be committed to Git.
- Only synthetic data will be used during development.

## 🗺️ Development Roadmap

- [ ] Repository and Python environment setup
- [ ] FastAPI application configuration
- [ ] Database integration with PostgreSQL
- [ ] SQLAlchemy models and relationships
- [ ] Alembic database migrations
- [ ] Authentication and authorization
- [ ] Product and category management
- [ ] Inventory management
- [ ] Shopping cart functionality
- [ ] Order management
- [ ] Payment simulation
- [ ] Redis integration
- [ ] Automated testing with Pytest
- [ ] Docker configuration
- [ ] API documentation and deployment

## 👨‍💻 Author

**Mohamad Sanas**

Computer Engineering Undergraduate
University of Jaffna, Sri Lanka

GitHub: [YOUR_GITHUB_USERNAME](https://github.com/YOUR_GITHUB_USERNAME)

---

⭐ If you find this project interesting, feel free to explore the repository.

**Built as a practical backend engineering learning project.**
