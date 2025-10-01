# QuickBite - Full-Stack Food Ordering Web App 🍔

![QuickBite Demo](./demo.gif)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.1-green.svg)](https://www.djangoproject.com/)

QuickBite is an interactive web application designed for a seamless food ordering experience. Built with Python and Django, it provides a user-friendly interface for browsing a restaurant's menu, adding items to a cart, and managing orders. This project showcases a full-stack development workflow, from backend logic and database management to a responsive frontend.

---

## ✨ Key Features

* **Secure User Authentication:** Users can sign up, log in, and log out with persistent sessions.
* **Dynamic Menu Display:** Browse all menu items, complete with images, descriptions, and prices.
* **Interactive Category Filtering:** Instantly filter the menu by food category (e.g., Appetizers, Main Course).
* **Shopping Cart:** Add items to a shopping cart that is tied to the user's session.
* **Admin Panel:** Full administrative control over menu items, categories, and user orders via the built-in Django admin interface.
* **User Feedback:** Interactive messages confirm user actions, such as adding an item to the cart.
* **Responsive Design:** A clean, mobile-friendly UI built with Bootstrap that works on all screen sizes.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **Key Libraries:** Pillow (for image handling)

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.10+
* Git

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/rajnish-chaube/quickbite-django.git](https://github.com/rajnish-chaube/quickbite-django.git)
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd quickbite-django
    ```
3.  **Create and activate a virtual environment:**
    ```sh
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
5.  **Apply the database migrations:**
    ```sh
    python manage.py migrate
    ```
6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

---

## ⚙️ Usage

To populate the menu, you need to use the admin panel.

1.  **Create a superuser account:**
    ```sh
    python manage.py createsuperuser
    ```
2.  **Access the Admin Panel:** Navigate to `http://127.0.0.1:8000/admin/` and log in.

3.  **Add Content:**
    * First, add a few `Categories` (e.g., "Appetizers," "Main Course").
    * Then, add several `Menu Items`, assigning each to a category and uploading an image.

Once you've added content, it will appear on the main site.

---

## 👤 Contact

Rajnish Chaube

* [GitHub](https://github.com/rajnish-chaube)
* [LinkedIn](https://www.linkedin.com/in/rajnish290/)
