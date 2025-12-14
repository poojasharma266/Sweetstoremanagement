# Sweet Shop Management System – Backend

This repository contains the **backend implementation** of the Sweet Shop Management System, built using **FastAPI** and developed following **strict Test-Driven Development (TDD)** principles.

The backend is responsible for authentication, sweet management, inventory operations, and role-based authorization.

This project was developed as part of an **AI-assisted TDD kata**, with a strong focus on clean architecture, test coverage, and professional Git workflows.

---

## 🎯 Objectives

The backend is designed to demonstrate:

* Test-Driven Development (Red → Green → Refactor)
* Clean and modular backend architecture
* Secure authentication using JWT
* Role-based authorization (USER / ADMIN)
* Inventory and business rule enforcement
* Transparent and responsible AI usage

---

## 🚀 Tech Stack

### Backend

* Python 3.10+
* FastAPI
* SQLAlchemy ORM
* SQLite (local development)
* JWT Authentication (`python-jose`)
* Pytest for testing

## Why FastAPI?

FastAPI was chosen for its:
- High performance and async support
- Built-in request validation using Pydantic
- Automatic Swagger/OpenAPI documentation
- Clean dependency injection system

These features make it well-suited for building testable and maintainable APIs.


### Tooling

* Git & GitHub
* AI-assisted development (documented below)

---

## 🧠 Core Features

### 🔐 Authentication & Authorization

* User registration
* User login with JWT token
* Users are assigned the USER role by default on registration
* Role-based access control (USER / ADMIN)
* Protected routes using JWT
> Note: Admin users can be seeded directly in the database for testing purposes.

### 🍬 Sweet Management

* Add new sweets
* View all sweets
* Automatic ID generation
* Quantity tracking per sweet

### 📦 Inventory Management

* Purchase sweets (quantity decreases by 1)
* Purchase blocked when stock is zero
* All inventory operations are validated at the service layer to ensure data consistency
* Restock sweets (ADMIN only)
* Quantity can never go negative

---

## 🧪 Test-Driven Development (TDD)

This backend strictly follows **Test-Driven Development**:

1. Write a failing test
2. Implement minimal logic to pass the test
3. Refactor while keeping tests green

The Git commit history clearly reflects this approach with:

* `test:` commits before `feat:` commits
* Small, meaningful changes per commit

---

## 📂 Project Structure

```
backend/
├── app/
│   ├── api/        # API routes
│   ├── core/       # Security & configuration
│   ├── db/         # Database models & sessions
│   ├── services/   # Business logic layer
│   ├── schemas/    # Request/response schemas
│   └── tests/      # Test cases (TDD)
|
├── requirements.txt
├── pytest.ini
└── README.md
```
---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/poojasharma266/Sweetstoremanagement.git
cd sweet-shop-management-system/backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Backend Server

```bash
uvicorn app.main:app --reload
```

Backend will be available at:

```
http://127.0.0.1:8000
```

---

## 📘 API Documentation (Swagger)

FastAPI provides interactive API documentation using Swagger UI.

Access it at:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Running Tests

All backend tests are written using **Pytest**.

```bash
pytest
```

The test suite covers:

* Authentication flows
* Authorization rules
* Inventory edge cases
* Business logic constraints

---

## 🔗 API Endpoints Overview

### Authentication

* `POST /api/auth/register`
* `POST /api/auth/login`

### Sweets

* `POST /api/sweets`
* `GET /api/sweets`

### Inventory

* `POST /api/sweets/{id}/purchase`
* `POST /api/sweets/{id}/restock` (ADMIN only)

---

## 🔐 Authorization Rules

| Endpoint       | Access             |
| -------------- | ------------------ |
| Create Sweet   | Authenticated User |
| Purchase Sweet | Authenticated User |
| Restock Sweet  | ADMIN only         |
| View Sweets    | Authenticated User |

---

## 🤖 My AI Usage

AI tools were used responsibly to **assist**, not replace, development.

### AI Tool Used

* ChatGPT

### How AI Was Used

* Designing the FastAPI project structure
* Brainstorming TDD test cases
* Refactoring service-layer logic
* Improving documentation clarity

### Reflection

AI helped improve development speed and validate design decisions.
All AI-generated suggestions were reviewed, modified, and fully understood before implementation.
Final architecture, business rules, and code were owned and implemented by the developer.

---

## 🧪 Test Report Summary

* All tests executed successfully using Pytest
* Critical business logic is fully covered
* No skipped or ignored tests

---

## 📌 Notes

* The backend follows clean code and SOLID principles
* Commit history narrates the complete TDD journey
* AI usage has been transparently disclosed as required

---

## ✨ Future Enhancements

* Sweet search and filtering
* Pagination support
* Production database configuration
* Dockerization
