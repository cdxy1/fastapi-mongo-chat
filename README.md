# FastAPI MongoDB Chat

A real-time messaging web application built with FastAPI, MongoDB, and Redis.

## 🚀 Features

- **User Authentication** (registration, login, token refresh, logout)
- **Direct Messages (P2P Chat)** via WebSocket
- **Message Storage** in MongoDB
- **Session Management** via Redis
- **RESTful API** for user management

## 📋 Requirements

- Python >= 3.12
- Docker and Docker Compose
- UV (Python package manager)

## 🛠 Tech Stack

- **FastAPI** - Web framework
- **MongoDB** - Database for storing users, messages, and rooms
- **Redis** - Caching refresh tokens
- **Beanie** - ODM for MongoDB
- **WebSocket** - Real-time chat
- **JWT** - Authentication
- **bcrypt** - Password hashing

## 📁 Project Structure

```
.
├── src/
│   ├── api/              # API routers
│   │   ├── v1/
│   │   │   ├── auth.py   # Authentication
│   │   │   ├── room.py   # WebSocket chat
│   │   │   └── user.py   # Users
│   ├── core/             # Core logic
│   │   ├── auth.py       # JWT tokens
│   │   ├── config.py     # Configuration
│   │   ├── exceptions.py # Exceptions
│   │   └── websocket_manager.py
│   ├── infrastructure/   # Infrastructure
│   │   ├── database.py   # MongoDB
│   │   └── redis.py      # Redis
│   ├── model/            # Data models
│   ├── repository/       # Repositories
│   ├── schema/           # Pydantic schemas
│   ├── service/          # Business logic
│   ├── usecase/          # Use cases
│   └── utils/            # Utilities
├── compose-dev.yml       # Docker Compose for development
├── compose-local.yml     # Docker Compose for local development
├── Makefile              # Management commands
├── pyproject.toml        # Project dependencies
└── README.md
```

## 🔧 Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd fastapi-mongo-chat
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Environment configuration

Create a `.env.dev` file in the project root:

```env
# MongoDB
DATABASE_USER=admin
DATABASE_PASSWORD=1234
DATABASE_HOST=mongo
DATABASE_PORT=27017
DATABASE_NAME=chat_db

# Redis
REDIS_HOST=redis
REDIS_PORT=6379

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
```

### 4. Run with Docker Compose

```bash
# Run in development mode
make up-dev

# Or manually
docker compose -f compose-dev.yml up -d
```

This will start:
- FastAPI application on port `8000`
- MongoDB on port `27017`
- Redis on port `6379`
- Mongo Express on port `8081` (web interface for MongoDB)

### 5. Run without Docker

```bash
# Start MongoDB and Redis locally
make up

# Run the application
make run

# Or manually
uvicorn src.main:app --reload
```

## 📚 API Documentation

After starting the application, documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔐 API Endpoints

### Authentication

- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login to the system
- `POST /api/v1/auth/refresh` - Refresh access token
- `DELETE /api/v1/auth/logout` - Logout from the system

### Users

- `GET /api/v1/users/` - Get list of all users (requires authentication)

### Chat

- `WebSocket /api/v1/chat/ws?token=<access_token>` - WebSocket connection for chat

## 💬 WebSocket Usage

### Connection

```javascript
const token = "your-access-token";
const ws = new WebSocket(`ws://localhost:8000/api/v1/chat/ws?token=${token}`);
```

### Sending a message

```json
{
  "receiver": "username",
  "message": "Hello!"
}
```

### Receiving messages

Messages are received in the format:
```json
{
  "message": "Message text"
}
```

## 🏗 Architecture

The project follows Clean Architecture principles:

- **Usecase** - Application business logic
- **Service** - Service layer
- **Repository** - Data access layer
- **Model** - Data models (Beanie)
- **Schema** - Pydantic schemas for validation

## 🧪 Development

### Code formatting

```bash
make fmt
```

This will run:
- `ruff format` - Code formatting
- `ruff check --fix` - Code checking and auto-fixing

### Stopping containers

```bash
# Stop dev environment
make down-dev

# Stop local environment
make down
```

## 📝 Request Examples

### User Registration

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "first_name": "John",
    "last_name": "Doe",
    "password": "secure_password"
  }'
```

### Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john_doe&password=secure_password"
```

### Get Users List

```bash
curl -X GET "http://localhost:8000/api/v1/users/" \
  -H "Authorization: Bearer <access_token>"
```

## 🔒 Security

- Passwords are hashed using bcrypt
- JWT tokens for authentication
- Refresh tokens stored in Redis
- CORS configured for all origins (change for production)

## 📦 Dependencies

Main dependencies are specified in `pyproject.toml`. To install:

```bash
uv sync
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Artem Minkin
