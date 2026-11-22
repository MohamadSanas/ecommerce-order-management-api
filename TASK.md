# 📋 Project Roadmap & Internship Preparation Tracker

> **Project:** E-Commerce Order Management API  
> **Target Role:** Backend Intern @ SimHealth (Starting Monday 23 Nov)  
> **Core Tech Stack:** Python 3.11+, FastAPI, Pydantic v2, SQLAlchemy 2.0 (Async), Alembic, PostgreSQL, Redis, pytest, Docker, Microservices  
> **Status:** 🟡 In Active Development

---

## 🎯 Purpose & Internship Alignment

This project is built to directly prepare for the **SimHealth Backend Internship** requirements outlined by the engineering lead. It follows modern backend engineering patterns (Modular Monolith transitioning to Microservices, async-first architecture, strict typing, automated testing, and containerization).

### SimHealth Learning Syllabus Mapping

| SimHealth Internship Week | Focus Area | Corresponding Project Phases in this Tracker |
| :--- | :--- | :--- |
| **Week 1 – Python Fundamentals** | Python 3.11+, async/await, asyncio, virtual environments, project structure | **Phase 1, Phase 2** |
| **Week 2 – APIs with FastAPI** | REST, routes, path/query params, dependency injection, Pydantic, JWT/OAuth2, RBAC | **Phase 1, Phase 4, Phase 5, Phase 6** |
| **Week 3 – Databases** | SQL, PostgreSQL, SQLAlchemy 2.0 ORM (async sessions, relationships), Alembic migrations | **Phase 2, Phase 3, Phase 4, Phase 7** |
| **Week 4 – Testing & Quality** | pytest, fixtures, parametrize, mocking, TestClient/httpx, ruff/black linting | **Phase 10, Phase 11** |
| **Week 5 – Architecture** | Microservices vs Monolith, Redis caching, structured logging, secrets, LLM readiness | **Phase 8, Phase 9, Phase 12** |
| **Day 1 Readiness** | Git branching, Docker Desktop, GitHub repository & mini-project link | **Phase 1, Phase 11, Phase 12** |

---

## 📊 Overall Progress Dashboard

- **Total Tasks:** 36
- **Completed Tasks:** 10
- **In Progress:** 1
- **Remaining:** 25
- **Progress:** `[██████░░░░░░░░░░░░░░] 28%`

---

## 🗺️ Detailed Phase Breakdown

---

### Phase 1: Environment & Project Foundation (SimHealth Week 1 & Day 1 Must-Haves)
**Objective:** Set up a clean, scalable project structure with modern Python 3.11+, virtual environment, configuration management, and a running FastAPI foundation.

- [x] **Task 1.1: Virtual Environment & Dependency Management**
  - *What to do:* Initialize a clean Python virtual environment (`venv`) and specify dependencies in `requirements.txt`.
  - *How to do it:* Run `python -m venv venv` and configure dependencies: FastAPI, Uvicorn, Pydantic, SQLAlchemy 2.0, asyncpg, Alembic, Redis, PyJWT, Pwdlib, pytest, and Ruff.
  - *Internship Value:* Understanding virtual isolation and dependency pinning prevents "works on my machine" issues in team workflows.
- [x] **Task 1.2: Environment Configuration & Secrets Management**
  - *What to do:* Set up `.env.example` and `.env` using `pydantic-settings` for type-safe environment variable parsing.
  - *How to do it:* Create `app/core/config.py` using `BaseSettings` with default values, validation, and `.env` loading. Ensure `.env` is ignored by `.gitignore` (never commit secrets!).
  - *Internship Value:* SimHealth lead explicitly highlighted: *"never commit secrets!"*. Pydantic Settings provides zero-cost validation of critical variables on boot.
- [x] **Task 1.3: Scalable Directory Structure**
  - *What to do:* Create modular architecture directories: `app/` (`core`, `database`, `models`, `schemas`, `api`, `services`, `repositories`) and `tests/`.
  - *How to do it:* Initialize package files (`__init__.py`) across all modules to ensure clean import paths and avoid circular imports.
  - *Internship Value:* Prepares the code for easy extraction into microservices later.
- [x] **Task 1.4: Structured Logging & Global Error Handling**
  - *What to do:* Configure Python standard logging with formatted output and global exception handlers.
  - *How to do it:* Implement `app/core/logging.py` and attach custom exception handlers in `app/main.py` for consistent JSON error responses (`{"detail": "...", "code": "..."}`).
  - *Internship Value:* SimHealth Week 5 topic: structured logging and standard error response schemas are vital for microservice observability.
- [x] **Task 1.5: Initial FastAPI App & Health Check Endpoint**
  - *What to do:* Create `app/main.py` and register `/api/v1/health` endpoint with Swagger documentation (`/docs`).
  - *How to do it:* Instantiate `FastAPI` with metadata (title, version, docs_url) and include API v1 router.
  - *Internship Value:* SimHealth Week 2 basics: REST HTTP GET, JSON responses, and FastAPI interactive docs.

---

### Phase 2: Database Layer & Async SQLAlchemy 2.0 (SimHealth Week 3)
**Objective:** Establish asynchronous database connectivity with PostgreSQL using modern SQLAlchemy 2.0 syntax, connection pooling, and FastAPI dependency injection.

- [x] **Task 2.1: Async Database Engine & Session Factory**
  - *What to do:* Create `create_async_engine` and `async_sessionmaker` in `app/database/session.py`.
  - *How to do it:* Connect using `postgresql+asyncpg://...`, configure pool size, recycle timeout, and `echo` flag for SQL query logging in development.
  - *Internship Value:* SimHealth requires async/await throughout. Async database drivers (`asyncpg`) prevent event-loop blocking under high concurrent loads.
- [x] **Task 2.2: Declarative Base & Reusable Mixins**
  - *What to do:* Set up SQLAlchemy 2.0 `DeclarativeBase` with timestamp mixins (`created_at`, `updated_at`, `id`).
  - *How to do it:* Create `app/database/base.py` using `Mapped` and `mapped_column` type annotations (SQLAlchemy 2.0 standard).
  - *Internship Value:* Type hints in ORM models catch schema discrepancies at development time rather than runtime.
- [x] **Task 2.3: Database Session Dependency Injection (`get_db`)**
  - *What to do:* Implement an `async def get_db()` generator yielding an `AsyncSession` with proper context management.
  - *How to do it:* Define dependency in `app/api/deps.py` with `try ... finally await session.close()`.
  - *Internship Value:* SimHealth Week 2 & 3 core topic: FastAPI Dependency Injection ensures sessions are properly released back to the pool, preventing connection leaks.

---

### Phase 3: Database Migrations with Alembic (SimHealth Week 3)
**Objective:** Manage relational database schema evolution through version-controlled Alembic migrations.

- [x] **Task 3.1: Alembic Async Setup**
  - *What to do:* Initialize Alembic with async template (`alembic init -t async alembic`).
  - *How to do it:* Modify `alembic/env.py` to import `Base.metadata` from `app.database.base` and dynamically inject `DATABASE_URL` from `app.core.config.settings`.
  - *Internship Value:* Understand how Alembic inspects metadata to compare against live database state.
- [ ] **Task 3.2: Initial Migration Generation & Validation**
  - *What to do:* Generate and test the initial migration script (`alembic revision --autogenerate -m "initial_schema"`).
  - *How to do it:* Verify the generated migration file for clean `upgrade()` and `downgrade()` logic.
  - *Internship Value:* Lead requirement: create, upgrade, and downgrade migrations safely in CI/CD and local environments.

---

### Phase 4: Core Domain Models & Schemas (SimHealth Week 1, 2 & 3)
**Objective:** Model relational e-commerce entities in SQLAlchemy 2.0 and validate inputs/outputs with Pydantic v2.

- [x] **Task 4.1: User Model & Schemas**
  - *What to do:* Create `User` model (`id`, `email`, `hashed_password`, `full_name`, `role`, `is_active`) and schemas (`UserCreate`, `UserUpdate`, `UserOut`).
  - *How to do it:* Use `EmailStr` from Pydantic, define user roles enum (`customer`, `admin`), and configure `from_attributes = True`.
  - *Internship Value:* Pydantic v2 data validation, email formatting, and sensitive field masking (`hashed_password` never returned in output).
- [ ] **Task 4.2: Category & Product Models & Schemas**
  - *What to do:* Create `Category` and `Product` models with foreign key relationships (`category_id`), title, description, price (Decimal), and stock quantity.
  - *How to do it:* Define `relationship("Product", back_populates="category")` in SQLAlchemy and corresponding Pydantic schemas with price validation (`gt=0`).
  - *Internship Value:* Relational modeling: One-to-Many relationships, database indexes on slug and category foreign keys.
- [ ] **Task 4.3: Cart & CartItem Models & Schemas**
  - *What to do:* Create `Cart` (associated with `User`) and `CartItem` (holding `product_id`, `quantity`).
  - *How to do it:* Implement unique constraint on `(cart_id, product_id)` to prevent duplicate item entries.
  - *Internship Value:* Relational integrity and database constraints.
- [ ] **Task 4.4: Order, OrderItem & Payment Models & Schemas**
  - *What to do:* Create `Order` (`user_id`, `status`, `total_amount`, `shipping_address`), `OrderItem` (capturing historical unit price and quantity), and `Payment` (`order_id`, `amount`, `status`, `provider`, `transaction_id`).
  - *How to do it:* Ensure `OrderItem` preserves price-at-purchase-time (so product price changes don't alter past orders).
  - *Internship Value:* E-commerce domain modeling and financial record immutability.

---

### Phase 5: Authentication & Authorization (SimHealth Week 2)
**Objective:** Implement secure JWT-based authentication, password hashing, and role-based access control (RBAC).

- [ ] **Task 5.1: Password Hashing Utilities**
  - *What to do:* Implement secure password hashing and verification in `app/core/security.py`.
  - *How to do it:* Use `pwdlib` / `bcrypt` to generate salted hashes and verify incoming plain passwords.
  - *Internship Value:* Security hygiene: never store plaintext passwords, understand salt rounds and timing-attack protections.
- [ ] **Task 5.2: JWT Token Generation & Decoding**
  - *What to do:* Create helper functions to encode and decode access tokens with expiration times (`exp`).
  - *How to do it:* Use `pyjwt` with HMAC-SHA256 (`HS256`) and settings-based `SECRET_KEY`.
  - *Internship Value:* Stateless authentication in REST APIs and token lifetime management.
- [ ] **Task 5.3: Current User Dependency & OAuth2 Password Flow**
  - *What to do:* Build `get_current_user` and `get_current_active_user` dependencies using `OAuth2PasswordBearer`.
  - *How to do it:* Parse `Authorization: Bearer <token>` header, decode user ID, verify user in database, and raise `401 Unauthorized` if invalid.
  - *Internship Value:* FastAPI Dependency Injection chaining (`Depends(get_current_active_user)`).
- [ ] **Task 5.4: Role-Based Access Control (RBAC)**
  - *What to do:* Create a permission dependency `require_role(allowed_roles: list[str])`.
  - *How to do it:* Inspect `current_user.role`; raise `403 Forbidden` if the user lacks the required role.
  - *Internship Value:* Securing administrative routes (e.g., adding products, updating inventory) versus customer routes.
- [ ] **Task 5.5: Auth Endpoints (`/api/v1/auth`)**
  - *What to do:* Expose `/auth/register`, `/auth/login` (OAuth2 form data returning `{access_token, token_type}`), and `/auth/me`.
  - *How to do it:* Wire routes to `AuthService` handling user creation and credential verification.
  - *Internship Value:* Full auth lifecycle testable directly in Swagger UI (`/docs`).

---

### Phase 6: Product & Inventory Management (SimHealth Week 2 & 3)
**Objective:** Build high-performance REST endpoints for category, product catalog, search, and stock tracking using the repository/service pattern.

- [ ] **Task 6.1: Category CRUD Endpoints**
  - *What to do:* Create routes for listing categories, getting category by slug/ID, and admin-only creation/updating/deletion.
  - *How to do it:* Implement `CategoryRepository` and `CategoryService` with async SQLAlchemy `select` queries.
  - *Internship Value:* Separation of concerns: API routes handle HTTP, services handle business rules, repositories handle database access.
- [ ] **Task 6.2: Product Catalog & Filtering Endpoints**
  - *What to do:* Build `GET /api/v1/products` with pagination (`skip`, `limit`), category filtering, price range, and search query.
  - *How to do it:* Use dynamic SQLAlchemy 2.0 query builder (`select(Product).where(...)`) and return total count with items.
  - *Internship Value:* Query optimization, indexing, and handling user search input efficiently.
- [ ] **Task 6.3: Product Admin Management**
  - *What to do:* Build `POST`, `PUT`, `DELETE` endpoints for products restricted to `admin` role.
  - *How to do it:* Validate category existence and enforce positive stock counts before persisting.
  - *Internship Value:* RBAC in action and data integrity checks.
- [ ] **Task 6.4: Inventory Stock Management Endpoints**
  - *What to do:* Create dedicated endpoints for updating product stock levels and retrieving low-stock items (`stock <= threshold`).
  - *How to do it:* Provide `PATCH /api/v1/inventory/{product_id}/stock` and `GET /api/v1/inventory/low-stock`.
  - *Internship Value:* Dedicated inventory tracking prepares for an independent Inventory Microservice.

---

### Phase 7: Shopping Cart & Order Processing (SimHealth Week 3 & 5)
**Objective:** Implement stateful cart operations and atomic order placement with inventory reservation using database transactions.

- [ ] **Task 7.1: Shopping Cart Endpoints**
  - *What to do:* Endpoints for `GET /cart`, `POST /cart/items` (add item), `PATCH /cart/items/{item_id}` (update qty), and `DELETE /cart/items/{item_id}`.
  - *How to do it:* Calculate subtotals and grand total dynamically; verify requested quantity does not exceed available stock.
  - *Internship Value:* Complex calculations and multi-entity relationship querying in SQLAlchemy.
- [ ] **Task 7.2: Atomic Order Checkout with Stock Deduction**
  - *What to do:* Implement `POST /api/v1/orders/checkout` that converts current cart into an `Order` with `OrderItem`s.
  - *How to do it:* Execute inside an atomic transaction (`async with session.begin():`):
    1. Lock product rows or verify stock availability.
    2. Deduct product inventory.
    3. Create `Order` in `PENDING` state.
    4. Copy cart items into `OrderItem` records.
    5. Clear the user's shopping cart.
  - *Internship Value:* **Crucial Backend Concept:** ACID transactions, concurrency handling, and avoiding race conditions / overselling.
- [ ] **Task 7.3: Order Management & Status Lifecycle**
  - *What to do:* Endpoints to list customer orders, get order details by ID, cancel pending orders (with stock rollback), and admin status updates (`SHIPPED`, `DELIVERED`).
  - *How to do it:* Implement state transition rules (e.g. cannot cancel once shipped; cancelling restores inventory).
  - *Internship Value:* Finite State Machine (FSM) patterns and business rule enforcement.

---

### Phase 8: Payment Simulation & Service Layer (SimHealth Week 2 & 5)
**Objective:** Simulate an asynchronous payment gateway integration with idempotent transaction handling.

- [ ] **Task 8.1: Payment Gateway Service Simulation**
  - *What to do:* Create `PaymentService` simulating external provider interactions (e.g. Stripe/Stripe-like webhooks).
  - *How to do it:* Support test card scenarios (success, decline, insufficient funds) and generate unique `transaction_id`.
  - *Internship Value:* Simulating third-party external API integration with retry and error handling.
- [ ] **Task 8.2: Payment Execution & Webhook Processing**
  - *What to do:* Endpoints `POST /api/v1/payments/process` and `POST /api/v1/payments/webhook`.
  - *How to do it:* On successful payment, transition order status to `PAID`. Support idempotency keys to prevent duplicate charges.
  - *Internship Value:* Distributed systems concept: Idempotent API design.

---

### Phase 9: Redis Caching & Performance Optimization (SimHealth Week 5)
**Objective:** Integrate Redis for fast read caching and reduced database load on hot endpoints.

- [ ] **Task 9.1: Redis Client & Connection Management**
  - *What to do:* Configure async Redis client connection in `app/core/redis.py` with lifespan startup and shutdown hooks.
  - *How to do it:* Use `redis.asyncio` with connection pooling and graceful fallback if Redis is unavailable.
  - *Internship Value:* SimHealth Week 5: Redis caching basics and resilient external service connections.
- [ ] **Task 9.2: Cache Product Catalog & Invalidation Pattern**
  - *What to do:* Cache popular product listings and product detail lookups with TTL (Time-To-Live).
  - *How to do it:* Check Redis cache before hitting PostgreSQL; on product create/update/delete, invalidate the corresponding cache keys.
  - *Internship Value:* Cache-aside pattern and cache invalidation strategies in production APIs.

---

### Phase 10: Automated Testing Suite with Pytest (SimHealth Week 4)
**Objective:** Build a comprehensive automated test suite with fixtures, isolated test databases, and async API client testing.

- [ ] **Task 10.1: Pytest Async Configuration & Test Fixtures**
  - *What to do:* Create `tests/conftest.py` with test database setup and `httpx.AsyncClient` fixtures.
  - *How to do it:* Use `pytest-asyncio`, SQLite in-memory async or PostgreSQL test database, and automatic table creation/cleanup per test session.
  - *Internship Value:* SimHealth Week 4 core: pytest fixtures, async test runner, and dependency overrides (`app.dependency_overrides[get_db] = override_get_db`).
- [ ] **Task 10.2: Authentication & User API Tests**
  - *What to do:* Test user registration, duplicate email handling, login validation, JWT generation, and token rejection.
  - *How to do it:* Write parametrized test cases covering valid credentials, wrong passwords, and expired tokens.
  - *Internship Value:* Parametrized testing (`@pytest.mark.parametrize`) and security assertions.
- [ ] **Task 10.3: Product Catalog & Category Tests**
  - *What to do:* Test CRUD operations, permission checks (customer vs admin), search filters, and pagination.
  - *How to do it:* Assert response status codes (200, 201, 403, 404, 422) and response payload schemas.
  - *Internship Value:* Integration testing of REST contracts and RBAC.
- [ ] **Task 10.4: End-to-End Cart, Checkout & Inventory Tests**
  - *What to do:* Test the complete user journey: browse -> add to cart -> attempt checkout with insufficient stock (verify 400 error) -> successful checkout -> verify stock decremented.
  - *How to do it:* Multi-step async test simulating realistic e-commerce purchase workflows.
  - *Internship Value:* High-value integration tests that guarantee business logic correctness.
- [ ] **Task 10.5: Mocking External Services**
  - *What to do:* Mock Redis and payment gateways during unit tests using `pytest-mock` / `unittest.mock`.
  - *How to do it:* Ensure tests run fast and deterministically without requiring live external network dependencies.
  - *Internship Value:* SimHealth Week 4 requirement: mastering test mocking.

---

### Phase 11: Code Quality, Linting & Docker Containerization (SimHealth Week 4 & Must-Haves)
**Objective:** Enforce clean code standards and package the entire stack for single-command deployment.

- [ ] **Task 11.1: Linting & Code Formatting with Ruff**
  - *What to do:* Configure Ruff in `pyproject.toml` for high-speed Python linting and formatting.
  - *How to do it:* Set target Python version to 3.11+, configure rule sets (E, F, I, B), and run `ruff check` and `ruff format`.
  - *Internship Value:* SimHealth Week 4 requirement: code style consistency, type-checking, and reading tracebacks.
- [ ] **Task 11.2: Production Multi-Stage Dockerfile**
  - *What to do:* Create an optimized `Dockerfile` for the FastAPI backend.
  - *How to do it:* Use `python:3.11-slim` (or `3.13-slim`), non-root user execution for security, and minimal image footprint.
  - *Internship Value:* SimHealth "Must-have before day 1": Docker fundamentals.
- [ ] **Task 11.3: Docker Compose Stack (`api`, `postgres`, `redis`)**
  - *What to do:* Create `docker-compose.yml` orchestrating the FastAPI application, PostgreSQL database, and Redis cache.
  - *How to do it:* Configure environment variables, persistent volumes, healthchecks, and dependency order (`depends_on: {postgres: {condition: service_healthy}}`).
  - *Internship Value:* SimHealth Day 1 checklist: `docker compose up` spinning up the entire stack with zero manual configuration.

---

### Phase 12: Microservices Transition Guide & Intern Showcase (SimHealth Week 5 & Lead Mini-Project)
**Objective:** Document microservices decomposition strategies and push the completed project to GitHub for the SimHealth lead review.

- [ ] **Task 12.1: Microservices Architecture Transition Document**
  - *What to do:* Write an architectural document explaining how this modular monolith decomposes into independent microservices:
    - *Auth Service* (JWT issuer & user management)
    - *Catalog & Inventory Service* (Products, categories, stock)
    - *Order & Cart Service* (Shopping carts, checkout saga)
    - *Payment Service* (Transactions & webhooks)
    - *SimHealth AI Integration* (LLM patient simulation service calls)
  - *Internship Value:* Directly connects to SimHealth's Week 5 syllabus: *Microservices vs monolith, service-to-service calls, calling LLM APIs*.
- [ ] **Task 12.2: Git Discipline & Clean Commit History**
  - *What to do:* Structure commits using Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`).
  - *How to do it:* Work on feature branches and create meaningful commit messages.
  - *Internship Value:* Lead checklist: *Git: branch, commit, PR, merge conflicts*.
- [ ] **Task 12.3: GitHub Repository Ready & Share with Lead**
  - *What to do:* Push to GitHub with comprehensive README, setup instructions, interactive docs screenshots, and test results.
  - *How to do it:* Share the GitHub link in the SimHealth onboarding group as the recommended mini-project!
  - *Internship Value:* Fulfills the lead's recommendation: *"Build a small FastAPI CRUD API with PostgreSQL + SQLAlchemy + an Alembic migration + a few pytest tests. Push it to GitHub and share the link here 🚀"*.

---

## 🛠️ Quick Command Reference

```bash
# 1. Activate Virtual Environment
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 2. Run API in Development Mode (Live reload)
uvicorn app.main:app --reload --port 8000

# 3. Access Interactive API Docs
# Swagger UI: http://127.0.0.1:8000/docs
# ReDoc: http://127.0.0.1:8000/redoc

# 4. Run Automated Tests
pytest -v

# 5. Run Database Migrations
alembic revision --autogenerate -m "describe_migration"
alembic upgrade head

# 6. Run Code Linting & Formatting
ruff check .
ruff format .

# 7. Start Full Stack with Docker
docker compose up -d --build
```
