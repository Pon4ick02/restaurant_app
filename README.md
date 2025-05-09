# MyRestaurant 🍽

A Django-based web application for an online restaurant. This pet project demonstrates core e-commerce features such as browsing a menu, managing a cart, placing orders, and leaving reviews.

## Features

- 🔐 **Custom User Authentication**  
  Users can register, log in, and manage their accounts using a custom user model.

- 📋 **Menu System**  
  View dishes with names, descriptions, prices, and images. Each dish displays its average user rating.

- 🛒 **Cart Functionality**  
  Authenticated users can add dishes to their cart with custom quantities. Dish count is shown in the UI (with a `99+` cap).

- 📦 **Order Placement**  
  Users can place orders directly from their cart. The system supports viewing past orders (including an order history section for both buyers and sellers).

- 🌟 **Review System**  
  Users can leave a star-rated review (1–5) and a comment only for dishes they've ordered.  
  - Anonymous reviews are supported.  
  - Admins can delete any review.  
  - Reviews are visible to everyone, including non-logged-in users.

- 🖼 **Admin Interface**  
  Superusers can manage all data through Django Admin: users, dishes, orders, and reviews.

- 🧠 **Role-based Access**  
  - Visitors can browse the menu and reviews.  
  - Only logged-in users can place orders and leave reviews.  
  - Sellers can view the order history filtered by their own dishes.

- 🎨 **Responsive Frontend (Bootstrap)**  
  Clean, mobile-friendly layout styled using Bootstrap with a focus on usability.

## Tech Stack

- **Backend**: Django 5.2
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (for development)


