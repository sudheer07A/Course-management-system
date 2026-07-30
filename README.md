# 🎓 Course Management System

A simple **Course Management System** built using **FastAPI** and **Streamlit**. This project demonstrates CRUD operations through REST APIs with a user-friendly web interface.

## 🚀 Features

* 📋 View all courses
* ➕ Add a new course
* ✏️ Update an existing course
* 🗑️ Delete a course
* 🌐 REST API with FastAPI
* 🎨 Interactive frontend with Streamlit

## 🛠️ Tech Stack

* Python
* FastAPI
* Streamlit
* Requests
* Git & GitHub
* Render (Deployment)

## 📂 Project Structure

```text
├── work.py              # FastAPI Backend
├── streamlit_app.py     # Streamlit Frontend
├── requirements.txt
└── README.md
```

## ▶️ Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the FastAPI server:

```bash
uvicorn work:app --reload
```

3. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

## 🌐 Live Demo
**Frontend (Streamlit):**
course-management-system ∙ main ∙ app.py

**Backend API:**
https://course-management-system-1-fg9s.onrender.com

**API Documentation:**
https://course-management-system-1-fg9s.onrender.com/docs

## 📌 API Endpoints

| Method | Endpoint                                          |
| ------ | ------------------------------------------------- |
| GET    | `/courses`                                        |
| POST   | `/addcourses/{course_name}`                       |
| PUT    | `/updatecourse/{oldcourse_name}/{newcourse_name}` |
| DELETE | `/deletecourse/{course_name}`                     |

## 👨‍💻 Author

**Sudheer**

If you found this project useful, consider giving it a ⭐ on GitHub.
