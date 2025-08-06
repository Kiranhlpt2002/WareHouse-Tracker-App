# WareHouse-Tracker-App
**Warehouse Stock Tracker** is a Django + Bootstrap app to manage products, IN/OUT transactions, and stock# 📦 Warehouse Stock Tracker

A lightweight Django + Bootstrap app to manage products, IN/OUT transactions, and stock details.  
Ideal for small warehouses, inventory demos, or educational use.

---

## ✨ Features

- Add and manage products (code, name, unit, rate)
- Record IN and OUT stock transactions
- Assign stock details to transactions
- Real-time stock summary per product (IN - OUT)
- Tab-based UI: only one data table visible at a time
- Bootstrap 5 styling for clean UX
- SQLite database for easy setup

---

## 🖥️ Live Demo

🔗 [View Hosted App](https://your-live-link.render.com/)  
*(Replace with actual link once deployed)*

---

## 🛠️ Tech Stack

- **Backend**: Django 4.x
- **Frontend**: HTML, Bootstrap 5
- **Database**: SQLite
- **Deployment**: Render / PythonAnywhere

---

## 📷 UI Highlights

- **Home Page** – Central dashboard with quick access to all forms  
- **Add Forms** – Add product, IN/OUT transactions, and stock details  
- **Inventory Page** – View Products, Transactions, Stock Details, and Stock Summary using Bootstrap tabs  

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/your-username/warehouse-stock-tracker.git
cd warehouse-stock-tracker
python -m venv env
source env/bin/activate      # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
tails. It features tab-based navigation, real-time stock calculations, and a clean UI. Built on SQLite, it's ideal for small warehouses and is deployable on Render or PythonAnywhere.
