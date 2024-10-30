import streamlit as st
import openai
import pandas as pd
import numpy as np

# Set your OpenAI API key
openai.api_key = "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"

# Define the main function
def main():
    st.title("Chronic Care Management App")

    # Patient Input Data
    st.header("Patient Input Data")
    patient_data = {
        'Name': st.text_input("Enter patient's name"),
        'Age': st.number_input("Enter patient's age", min_value=0),
        'Gender': st.selectbox("Select gender", ["Male", "Female", "Other"]),
        'Cardiovascular Disease Risk': st.slider("Cardiovascular Disease Risk (0-100)", 0, 100),
        'Hypertension Risk': st.slider("Hypertension Risk (0-100)", 0, 100),
        'Diabetes Risk': st.slider("Diabetes Risk (0-100)", 0, 100),
        'COPD Risk': st.slider("COPD Risk (0-100)", 0, 100),
        'Asthma Risk': st.slider("Asthma Risk (0-100)", 0, 100)
    }
    
    # Collect the patient data
    if st.button("Submit"):
        st.write("Patient Data Submitted:")
        st.json(patient_data)
        risk_level = assess_risk(patient_data)
        care_plan = create_care_plan(risk_level)
        st.write("Risk Level: ", risk_level)
        st.write("Personalized Care Plan: ")
        st.write(care_plan)
        self_management_support = generate_self_management_support(risk_level)
        st.write("Self-Management Support: ")
        st.write(self_management_support)

        # AI Q&A Section
        st.header("AI Q&A Section")
        user_question = st.text_input("Ask a health-related question:")
        if st.button("Ask"):
            answer = get_ai_response(user_question)
            st.write("AI Response: ", answer)

# Function for AI-driven risk stratification
def assess_risk(patient_data):
    # Basic logic to determine risk level based on inputs
    risk_score = (patient_data['Cardiovascular Disease Risk'] +
                  patient_data['Hypertension Risk'] +
                  patient_data['Diabetes Risk'] +
                  patient_data['COPD Risk'] +
                  patient_data['Asthma Risk']) / 5
    
    if risk_score < 30:
        return "Low Risk"
    elif 30 <= risk_score < 70:
        return "Moderate Risk"
    else:
        return "High Risk"

# Function for creating personalized care plans
def create_care_plan(risk_level):
    plans = {
        "Low Risk": "Maintain a healthy lifestyle, regular check-ups, and monitor blood pressure and cholesterol levels.",
        "Moderate Risk": "Adopt a balanced diet, increase physical activity, and consider regular screenings.",
        "High Risk": "Follow a tailored medical plan, engage in regular monitoring, and possibly start medication as prescribed."
    }
    return plans.get(risk_level, "No care plan available.")

# Function for self-management support
def generate_self_management_support(risk_level):
    supports = {
        "Low Risk": "Stay active, eat well, and schedule annual health check-ups.",
        "Moderate Risk": "Focus on balanced nutrition, exercise 150 minutes a week, and monitor health indicators regularly.",
        "High Risk": "Follow the care plan closely, attend all medical appointments, and communicate regularly with your healthcare provider."
    }
    return supports.get(risk_level, "No self-management support available.")

# Function for getting AI response to user questions
def get_ai_response(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with your desired model
            messages=[
                {"role": "user", "content": question}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

# Run the app
if __name__ == "__main__":
    main()
