import streamlit as st
import pickle

# Title
st.title("🚢 Titanic Survival Prediction")

# Load the model
model = pickle.load(open("titanic_model.pkl", "rb"))

st.write("Fill the details below to predict survival:")

# Inputs
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0, max_value=100, value=25)
fare = st.number_input("Fare", min_value=0.0, value=50.0)
sibsp = st.number_input("Number of Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0)
parch = st.number_input("Number of Parents/Children Aboard (Parch)", min_value=0, max_value=10, value=0)

# Convert sex to numeric
sex_num = 1 if sex == "female" else 0

# Predict button
if st.button("Predict"):
    features = [[pclass, sex_num, age, sibsp, parch, fare]]
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.success("✅ The passenger is likely to SURVIVE.")
    else:
        st.error("❌ The passenger is likely to NOT survive.")
