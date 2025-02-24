# E-commerce Application Documentation 🛍️

This repository contains both the backend and frontend components of an e-commerce application. The backend is built with Django REST Framework, while the frontend utilizes Vue.js with TypeScript.

## Table of Contents
- [Backend Architecture](#backend-architecture)
- [Frontend Architecture](#frontend-architecture)
- [State Management](#state-management)
- [User Interface](#user-interface)
- [Development Guidelines](#development-guidelines)

## Backend Architecture

### Technology Stack 🔧
- Django
- MySQL (default database)

### Data Models 📝

#### Product Model
```python
class Product:
    name: str                   # max 40 characters
    price: int                  # positive integer
    description: str            # text field with default
    quantity_in_stock: int      # positive integer, default 0
    rating: int                 # 1-5 scale
    image: str                  # image URL/data
    slug: str                   # auto-generated from name
```

### Key Features ⭐
- Automatic slug generation for SEO-friendly URLs
- Built-in data validation
- JSON serialization support
- RESTful API endpoints

## Frontend Architecture

### Technology Stack 🔧
- Vue.js 3
- TypeScript
- Vue Router
- Pinia (State Management)
- SCSS

### Project Structure 📁
```
src/
├── assets/         # Static assets
├── components/     # Reusable Vue components
├── router/         # Route definitions
├── state/         # Pinia stores
└── views/         # Page components
```

## State Management 🔄

### Products Store
```typescript
// State
userCart: CartItem[]    // Stores cart items
name: string           // User name

// Actions
addProductToCart()     // Add/update cart items
clearCart()           // Reset cart state

// Getters
cartTotal             // Calculate total cart value
```

### Data Flow
1. User interactions trigger actions
2. Actions modify state
3. Components react to state changes
4. UI updates automatically

## User Interface 🎨

### Navigation
- Responsive header with logo
- Main navigation menu
- Dynamic routing system

### Key Components
- Product listings
- Shopping cart
- Product details
- Responsive footer

### Design Features
- Mobile-first approach
- Flexbox layout system
- Bootstrap utility classes
- Custom SCSS styling

## Development Guidelines 📚

### Environment Configuration 🔐

1. Backend Environment Setup
Create a `.env` file in the root directory of the backend project:
```env
# Django Settings
DEBUG=True
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (if using custom database)
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173

# Static Files
STATIC_URL=/static/
MEDIA_URL=/media/
```

2. Frontend Environment Setup
Create a `.env` file in the root directory of the frontend project:
```env
# API Configuration
VITE_API_BASE_URL=http://localhost:8000/api
VITE_APP_TITLE=E-commerce Store

# Development Settings
VITE_DEV_SERVER_PORT=5173
```

⚠️ Important Notes:
- Never commit `.env` files to version control
- Keep your secret keys secure
- Use different environment configurations for development and production
- Make sure to add `.env` to your `.gitignore` file

### Setting Up Development Environment

1. Backend Setup
```bash
# Create virtual environment
python -m venv env
source env/bin/activate  # Linux/Mac
.\env\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

2. Frontend Setup
```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

### Best Practices 🎯

#### Backend
- Use model validators for data integrity
- Follow Django's REST framework conventions
- Write docstrings for complex functions
- Use appropriate HTTP methods for API endpoints

#### Frontend
- Use TypeScript for type safety
- Implement component-based architecture
- Follow Vue.js composition API patterns
- Maintain centralized state management

### Code Style 📝
- Use consistent indentation
- Follow naming conventions
- Write clear comments
- Keep components focused and reusable

## API Integration 🔌

### Available Endpoints
- GET /api/v1/products/ - List all products
- - GET /api/v1/products/{id}/ - Get single product by the id
- GET /api/v1/products/{slug}/ - Get single product (wasn't completely implemented)


## Contributing 🤝
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License 📄
[MIT License](LICENSE)
