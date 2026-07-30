import streamlit as st
import requests

base_url = "https://course-management-system-1-fg9s.onrender.com"
# Custom CSS for background and styling
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #667eea, #764ba2);
    }

    /* Title styling */
    h1 {
        color: white;
        text-align: center;
        font-size: 45px;
        font-weight: bold;
    }

    /* Subheader styling */
    h2, h3 {
        color: #ffffff;
        font-weight: bold;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #141E30, #243B55);
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Text styling */
    p {
        color: white;
        font-size: 18px;
    }

    /* Input boxes */
    input {
        background-color: white !important;
        color: black !important;
        border-radius: 10px;
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(90deg, #ff9966, #ff5e62);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 25px;
        border: none;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
    }

    /* JSON box */
    div[data-testid="stJson"] {
        background-color: rgba(255,255,255,0.9);
        border-radius: 15px;
        padding: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.title("Course Management System")

menu = st.sidebar.selectbox(
    "Choose",
    ["Home", "Courses", "Add Courses", "Update Courses", "Delete Courses"]
)

if menu == "Home":
    st.subheader("Welcome to Course Management System")
    st.write("This is a simple course management system.")
    st.write("Use the sidebar to navigate.")

    response = requests.get(f"{base_url}/courses")

    st.json(response.json())

elif menu=="Courses":
    st.subheader("Courses")
    response = requests.get(f"{base_url}/courses")
    st.json(response.json())

elif menu=="Add Courses":
    st.subheader("Add Courses")
    course_name = st.text_input("Enter Course name")
    st.write("Click the button to add the course")
    if st.button("Add Course"):
        response = requests.post(f"{base_url}/addcourses/{course_name}")
        st.write(response.text)
    else:
        st.write("Please enter a course name and click the button to add the course.")

elif menu=="Update Courses":
    st.subheader("Update Courses")
    old_course_name = st.text_input("Enter Old Course name")
    new_course_name = st.text_input("Enter New Course name")
    st.write("Click the button to update the course")
    if st.button("Update Course"):
        response = requests.put(f"{base_url}/updatecourse/{old_course_name}/{new_course_name}")
        st.write(response.text)
    else:
        st.write("Please enter both old and new course names and click the button to update the course.")

else:
    st.subheader("Delete Courses")

    course_name = st.text_input("Enter Course name")

    if st.button("Delete Course"):

        if course_name:

            response = requests.delete(
                f"{base_url}/deletecourse/{course_name}"
            )

            if response.status_code == 200:
                st.success(response.text)
            else:
                st.error(f"Error: {response.status_code}")

        else:
            st.warning("Please enter course name")