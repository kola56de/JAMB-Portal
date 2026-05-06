# 🎓 JAMB Student Portal

A web-based student management system built with **Streamlit**, **SQLite**, and **Pandas** for registering, searching, updating, deleting, and displaying student records through an interactive dashboard.

🔗 **Live App:** https://k-jamb-app.streamlit.app/

---

## 📌 Project Overview

The **JAMB Student Portal** is a lightweight student information management application designed to simplify student registration and record administration.

The system provides a clean interface where users can:

- Register new students  
- Search student records  
- Update student information  
- Delete records  
- Display all registered students  

The application uses **SQLite** as the backend database and Streamlit for the user interface.

---

## 🚀 Features

### 📝 Student Registration

Register new students with:

- Registration Number  
- Full Name  
- Gender  
- State of Origin  
- Email Address  

### 🔍 Student Search

Search and retrieve student records instantly using registration number.

### ✏️ Update Records

Modify existing student information directly from the dashboard.

### 🗑️ Delete Records

Delete student records safely using registration number.

### 📊 Display All Records

View all registered students in a structured interactive table.

### 💾 SQLite Database Integration

Uses SQLite database (`students.db`) for persistent data storage.

### ⚡ Interactive Streamlit Dashboard

Simple and responsive user interface powered by Streamlit.

---

## 🖼️ App Screenshot

### Dashboard

![Dashboard](assets/Dashboard.png)

---

## 📝 Dashboard Explanation

The **JAMB Student Portal Dashboard** is an interactive student management interface built with **Streamlit** and **SQLite** for handling student records efficiently.

### 🎛️ Sidebar Navigation Menu

The left sidebar serves as the control panel for all portal operations.

Users can navigate between:

- Register → Add new student records  
- Search → Retrieve student information  
- Update → Modify existing records  
- Delete → Remove records from the database  
- Display All → View all registered students  
- Logout → Exit the session  

This menu makes the application easy to use and beginner-friendly.

---

### 🔍 Search Student Record Section

The screenshot currently shows the **Search Module**.

Users can:

1. Enter a Registration Number  
2. Click the Search button  
3. Retrieve student details instantly from the SQLite database  

If a matching record exists, the system displays:

- Registration Number  
- Full Name  
- Gender  
- State of Origin  
- Email Address  

If no record is found, the system displays a warning message.

---

### 🧠 Backend Database Operation

The application uses **SQLite** as the backend database.

When the search button is clicked:

- A SQL query is executed  
- The system checks the database for the registration number  
- Matching records are returned and displayed in table format  

Example SQL logic:

```sql
SELECT * FROM informations WHERE reg_no = ?
### ⚡ User Interface Design

The dashboard features:

- Simple and clean layout  
- Interactive sidebar controls  
- Responsive form inputs  
- Beginner-friendly navigation  

The minimalist interface makes student data management easy and efficient.

---

### 📌 Benefits of the Search Module

- Fast student record retrieval  
- Easy academic data lookup  
- Reduces manual searching  
- Demonstrates CRUD database operations  
- Useful for educational administration systems  

---

### 🧾 Summary

This dashboard acts as a mini **Student Information Management System**, allowing administrators to quickly search and manage student records through an interactive web application.

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- SQLite3  
- Pandas  

---

## 📂 Project Structure

```bash
JAMB-Portal/
│── assets/
│   └── Dashboard.png
│── Portal.py
│── requirements.txt
