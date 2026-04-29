# 🌾 KisanCart - Farmer Portal

[![GitHub](https://img.shields.io/badge/GitHub-codebydhiraj08-brightgreen)](https://github.com/codebydhiraj08/kisancart-farmer-portal)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-green)]
[![Node.js](https://img.shields.io/badge/Node.js-14+-green)]

An agricultural e-commerce platform that empowers farmers by connecting them directly with customers, eliminating middlemen and maximizing their profits.

---

## 🎯 About KisanCart

**KisanCart** is a revolutionary platform designed to transform the agricultural market. Our mission is to:
- ✅ Connect farmers **directly** with customers
- ✅ Eliminate exploitative middlemen
- ✅ Ensure **fair pricing** for farmers
- ✅ Provide **real-time order management**
- ✅ Build **verified farmer community**

---

## ⭐ Key Features

### 👨‍🌾 Farmer Portal
- **Easy Registration & Verification** - Simple onboarding process
- **Product Management** - Add, edit, and manage farm products
- **Order Dashboard** - Real-time order tracking and updates
- **Rating & Reviews** - Build trust through customer feedback
- **Farm Profile** - Showcase your farm and products
- **Payment Integration** - Secure and reliable payments
- **Analytics** - Track sales and performance metrics

### 🛒 Customer Features
- **Browse Products** - Discover fresh produce from verified farmers
- **Direct Ordering** - Place orders directly from farmers
- **Real-time Tracking** - Track your orders in real-time
- **Farmer Ratings** - See reviews and ratings before purchasing
- **Secure Checkout** - Safe and secure payment gateway

---

## 💻 Tech Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with Tailwind CSS
- **JavaScript (ES6+)** - Dynamic interactions
- **Tailwind CSS** - Utility-first CSS framework
- **FontAwesome Icons** - Professional icons
- **AOS (Animate On Scroll)** - Smooth animations

### Backend
- **Python** - Flask framework
- **Node.js** - Express.js server
- **SQLite** - Lightweight database
- **REST API** - Clean API architecture

### Database Schema
- Users Management
- Farmer Profiles
- Products Catalog
- Orders System
- Categories
- Ratings & Reviews

---

## 📁 Project Structure

```
KisanCart/
├── index.html                 # Home page
├── farmer.html               # Farmer dashboard
├── our-farmers.html          # Farmer listing page
├── icons.html                # Icons page
├── app.py                    # Flask backend
├── models.py                 # Database models
├── server.js                 # Node.js/Express server
├── package.json              # Node dependencies
├── database_schema.sql       # Database structure
├── DATABASE_README.md        # Database documentation
├── Css/
│   └── style.css            # Main stylesheet
├── Js/
│   └── script.js            # Main JavaScript
├── Assets/
│   └── images/
│       └── icons/           # Icon assets
└── models/                  # Node.js models
    ├── User.js
    ├── Farmer.js
    ├── Product.js
    └── Order.js
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- SQLite3
- npm or yarn

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/codebydhiraj08/kisancart-farmer-portal.git
cd kisancart-farmer-portal
```

2. **Install Python dependencies:**
```bash
pip install flask flask-sqlalchemy
```

3. **Install Node dependencies:**
```bash
npm install
```

4. **Database Setup:**
```bash
# Create database (runs automatically on app start)
python app.py
```

5. **Run the application:**

**Option 1 - Flask Server:**
```bash
python app.py
```

**Option 2 - Node.js Server:**
```bash
npm start
# or
node server.js
```

6. **Open in browser:**
```
http://localhost:5000  (Flask)
# or
http://localhost:3000  (Node.js)
```

---

## 📝 Database Schema

### Users Table
```sql
- id (Primary Key)
- mobile_number (Unique)
- name
- email
- address
- password_hash
- is_registered
- created_at
- updated_at
```

### Farmers Table
```sql
- id (Primary Key)
- name
- mobile_number (Unique)
- email
- farm_name
- farm_address
- is_verified
- rating (0.00-5.00)
- created_at
- updated_at
```

### Products Table
```sql
- id (Primary Key)
- farmer_id
- name
- category_id
- price
- quantity
- description
- image_url
- created_at
- updated_at
```

### Orders Table
```sql
- id (Primary Key)
- order_id (Unique)
- customer_name
- phone
- address
- total_amount
- items (JSON format)
- date
- status
```

---

## 🔐 API Endpoints

### Order Management
```
POST   /api/place-order       - Place new order
GET    /api/orders            - Get all orders
GET    /api/orders/:id        - Get specific order
PUT    /api/orders/:id        - Update order status
DELETE /api/orders/:id        - Cancel order
```

### Farmer Management
```
POST   /api/farmers           - Register farmer
GET    /api/farmers           - Get all farmers
GET    /api/farmers/:id       - Get farmer profile
PUT    /api/farmers/:id       - Update farmer info
```

### Product Management
```
POST   /api/products          - Add product
GET    /api/products          - Get all products
GET    /api/products/:id      - Get product details
PUT    /api/products/:id      - Update product
DELETE /api/products/:id      - Delete product
```

---

## 📖 Usage Guide

### For Farmers 👨‍🌾

1. **Register on Portal**
   - Go to farmer registration page
   - Enter farm details and contact info
   - Get verified

2. **Add Products**
   - Login to farmer dashboard
   - Add your products with details
   - Set prices and quantities

3. **Manage Orders**
   - View incoming orders in real-time
   - Update order status
   - Track payments

4. **Build Reputation**
   - Deliver orders on time
   - Get customer ratings
   - Build trust score

### For Customers 🛒

1. **Browse Products**
   - Visit marketplace
   - Filter by category or farmer
   - Check ratings and reviews

2. **Place Order**
   - Add items to cart
   - Enter delivery address
   - Proceed to checkout

3. **Track Order**
   - Get real-time updates
   - Rate farmer after delivery
   - Leave reviews

---

## 🎨 UI/UX Features

- **Responsive Design** - Works on all devices
- **Dark Mode Support** - Easy on the eyes
- **Glass Morphism Effects** - Modern navigation
- **Smooth Animations** - AOS scroll animations
- **Accessibility** - WCAG compliant

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📊 Future Enhancements

- [ ] Mobile app (React Native)
- [ ] Advanced analytics dashboard
- [ ] AI-based crop recommendation
- [ ] Bulk order management
- [ ] Weather forecasting integration
- [ ] Government subsidy tracker
- [ ] Supply chain transparency
- [ ] Blockchain for authenticity

---

## 👨‍💻 Author

**Dhiraj Warangane**
- GitHub: [@codebydhiraj08](https://github.com/codebydhiraj08)
- Project Link: https://codebydhiraj08.github.io/kisancart-farmer-portal/
- Email: [dhirajwarangane@gmail.com]

---

## 🙏 Acknowledgments

- Thanks to all contributors
- Inspired by the agricultural community
- Built with ❤️ for farmers

---

## 🌟 Star Us!

If you found this project helpful, please give it a ⭐ on GitHub!

---

**Made with ❤️ to empower farmers | Direct From Farm 🌾**
