import streamlit as st
import pickle
import numpy as np
from sklearn.datasets import load_iris

# Load the trained model
model_path = pickle.load("logistic_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

target_names = load_iris().target_names

# Dummy users
users = {
    "vivek": "pass123",
    "admin": "1234"
}

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Main app function
def main_app():
    st.sidebar.success(f"Logged in as: {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = ""
        return

    st.title("🌸 Iris Flower Prediction App")

    sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0, 5.1)
    sepal_width = st.number_input("Sepal Width (cm)", 0.0, 10.0, 3.5)
    petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0, 1.4)
    petal_width = st.number_input("Petal Width (cm)", 0.0, 10.0, 0.2)

    if st.button("Predict"):
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Class: **{target_names[prediction]}**")


# Login form
def login_form():
    st.title("🔐 Login to Iris Predictor")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        if username in users and users[username] == password:
            st.session_state.authenticated = True
            st.session_state.username = username
        else:
            st.error("❌ Invalid username or password")


# Controller
if st.session_state.authenticated:
    main_app()
else:
    login_form()
