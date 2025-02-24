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
- Django REST Framework
- SQLite (default database)

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
- GET /api/products/ - List all products
- GET /api/products/{slug}/ - Get single product
- POST /api/cart/ - Add to cart
- GET /api/cart/ - View cart

## Contributing 🤝
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License 📄
[MIT License](LICENSE)
