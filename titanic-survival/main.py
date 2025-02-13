import streamlit as st
import math
import pickle

# Load the model
with open("model.pkl", 'rb') as f:
    model = pickle.load(f)

# Header and title of the app
st.title("Titanic Survival Prediction")
st.markdown("### Enter passenger details below:")

# Layout with columns for better organization
col1, col2, col3 = st.columns(3)
with col1:
    Pclass = st.selectbox("Class of Passenger", ("Premiere", "Executive", "Economy"))
with col2:
    Sex = st.selectbox("Gender", ("Male", "Female"))
with col3:
    Age = st.number_input("Age of Passenger", min_value=0, value=30)

col4, col5 = st.columns(2)
with col4:
    SibSp = st.number_input("Siblings/Spouses", min_value=0, value=0)
with col5:
    Parch = st.number_input("Parents/Children", min_value=0, value=0)

col6, col7 = st.columns(2)
with col6:
    Fare = st.number_input("Fare of Journey", min_value=0.0, value=50.0)
with col7:
    Embarked = st.selectbox("Embarked Port", ("Cherbourg", "Queenstown", "Southampton"))

# Prediction button with a more prominent appearance
if st.button("Predict", key="predict_button"):
    # Encode inputs for model prediction
    pclass = 1 if Pclass == "Premiere" else (2 if Pclass == "Executive" else 3)
    gender = 0 if Sex == "Male" else 1
    age = math.ceil(Age)
    sibsp = math.ceil(SibSp)
    parch = math.ceil(Parch)
    fare = math.ceil(Fare)
    embarked = 0 if Embarked == "Southampton" else (1 if Embarked == "Cherbourg" else 2)

    # Make prediction
    result = model.predict([[pclass, gender, age, sibsp, parch, fare, embarked]])
    output_labels = {1: "The passenger will survive", 0: "The passenger will not survive"}

    # Display the result
    st.markdown(f"### {output_labels[result[0]]}")

    # Add an image or illustration for better visualization (Optional)
    if result[0] == 1:
        st.image("survive_image.jpg", caption="Survival Prediction", use_container_width=True)
    else:
        st.image("no_survive_image.jpg", caption="Non-Survival Prediction", use_container_width=True)

# Styling (optional, for a better visual experience)
st.markdown("""
    <style>
        .css-1kyxreq {
            background-color: #f5f5f5;
        }
        .css-2trq61 {
            font-size: 1.5em;
        }
    </style>
""", unsafe_allow_html=True)
