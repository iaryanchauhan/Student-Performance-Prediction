
import streamlit as st
import pandas as pd
import joblib

# --------------------------------
# 1. Load trained machine learning model
# --------------------------------

model = joblib.load("src/student_performance_model.pkl")

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# --------------------------------
# 2. Application heading
# --------------------------------

st.title("🎓 Student Performance Prediction")

st.write(
    "Enter the student's information below "
    "to predict their final academic grade."
)

st.info("The predicted grade will be between 0 and 20.")

# --------------------------------
# 3. Student information
# --------------------------------

st.header("Student Information")

age = st.number_input(
    "Age",
    min_value=15,
    max_value=22,
    value=17
)

school = st.selectbox(
    "School",
    ["GP", "MS"],
    format_func=lambda x: {
        "GP": "Gabriel Pereira",
        "MS": "Mousinho da Silveira"
    }[x]
)

sex = st.selectbox(
    "Gender",
    ["F", "M"],
    format_func=lambda x: {
        "F": "Female",
        "M": "Male"
    }[x]
)

address = st.selectbox(
    "Home Address",
    ["U", "R"],
    format_func=lambda x: {
        "U": "Urban",
        "R": "Rural"
    }[x]
)

# --------------------------------
# 4. Family information
# --------------------------------

st.header("Family Information")

famsize = st.selectbox(
    "Family Size",
    ["GT3", "LE3"],
    format_func=lambda x: {
        "GT3": "More than 3 members",
        "LE3": "3 or fewer members"
    }[x]
)

Pstatus = st.selectbox(
    "Parents' Status",
    ["T", "A"],
    format_func=lambda x: {
        "T": "Living together",
        "A": "Living apart"
    }[x]
)

education_options = {
    0: "No formal education",
    1: "Primary education",
    2: "5th–9th grade",
    3: "Secondary education",
    4: "Higher education"
}

Medu = st.selectbox(
    "Mother's Education",
    [0, 1, 2, 3, 4],
    format_func=lambda x: education_options[x]
)

Fedu = st.selectbox(
    "Father's Education",
    [0, 1, 2, 3, 4],
    format_func=lambda x: education_options[x]
)

Mjob = st.selectbox(
    "Mother's Job",
    ["at_home", "health", "other", "services", "teacher"],
    format_func=lambda x: x.replace("_", " ").title()
)

Fjob = st.selectbox(
    "Father's Job",
    ["teacher", "health", "services", "at_home", "other"],
    format_func=lambda x: x.replace("_", " ").title()
)

guardian = st.selectbox(
    "Student's Guardian",
    ["mother", "father", "other"],
    format_func=lambda x: x.title()
)

reason = st.selectbox(
    "Reason for Choosing School",
    ["home", "reputation", "course", "other"],
    format_func=lambda x: {
        "home": "Close to home",
        "reputation": "School reputation",
        "course": "Preferred course",
        "other": "Other reasons"
    }[x]
)

# --------------------------------
# 5. Study and lifestyle information
# --------------------------------

st.header("Study and Lifestyle Information")

traveltime = st.selectbox(
    "Travel Time to School",
    [1, 2, 3, 4],
    format_func=lambda x: {
        1: "Less than 15 minutes",
        2: "15–30 minutes",
        3: "30 minutes–1 hour",
        4: "More than 1 hour"
    }[x]
)

studytime = st.selectbox(
    "Weekly Study Time",
    [1, 2, 3, 4],
    format_func=lambda x: {
        1: "Less than 2 hours",
        2: "2–5 hours",
        3: "5–10 hours",
        4: "More than 10 hours"
    }[x]
)

failures = st.selectbox(
    "Past Class Failures",
    [0, 1, 2, 3]
)

famrel = st.selectbox(
    "Family Relationship",
    [1, 2, 3, 4, 5],
    format_func=lambda x: {
        1: "Very Bad",
        2: "Bad",
        3: "Average",
        4: "Good",
        5: "Excellent"
    }[x]
)

scale_options = {
    1: "1 - Very Low",
    2: "2 - Low",
    3: "3 - Average",
    4: "4 - High",
    5: "5 - Very High"
}

freetime = st.selectbox(
    "Free Time After School",
    [1, 2, 3, 4, 5],
    format_func=lambda x: scale_options[x]
)

goout = st.selectbox(
    "Going Out With Friends",
    [1, 2, 3, 4, 5],
    format_func=lambda x: scale_options[x]
)

Dalc = st.selectbox(
    "Workday Alcohol Consumption",
    [1, 2, 3, 4, 5],
    format_func=lambda x: scale_options[x]
)

Walc = st.selectbox(
    "Weekend Alcohol Consumption",
    [1, 2, 3, 4, 5],
    format_func=lambda x: scale_options[x]
)

health = st.selectbox(
    "Health Status",
    [1, 2, 3, 4, 5],
    format_func=lambda x: {
        1: "Very Bad",
        2: "Bad",
        3: "Average",
        4: "Good",
        5: "Very Good"
    }[x]
)

absences = st.number_input(
    "Number of School Absences",
    min_value=0,
    max_value=100,
    value=0
)

# --------------------------------
# 6. Additional student information
# --------------------------------

st.header("Additional Information")

schoolsup = st.selectbox(
    "Extra Educational Support",
    ["yes", "no"]
)

famsup = st.selectbox(
    "Family Educational Support",
    ["yes", "no"]
)

paid = st.selectbox(
    "Extra Paid Classes",
    ["yes", "no"]
)

activities = st.selectbox(
    "Extra Activities",
    ["yes", "no"]
)

nursery = st.selectbox(
    "Attended Nursery School",
    ["yes", "no"]
)

higher = st.selectbox(
    "Wants Higher Education",
    ["yes", "no"]
)

internet = st.selectbox(
    "Internet Access at Home",
    ["yes", "no"]
)

romantic = st.selectbox(
    "In a Romantic Relationship",
    ["yes", "no"]
)

# --------------------------------
# 7. Prediction
# --------------------------------

if st.button("Predict Final Grade", use_container_width=True):

    input_data = {
        "age": age,
        "Medu": Medu,
        "Fedu": Fedu,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences,
        "school": school,
        "sex": sex,
        "address": address,
        "famsize": famsize,
        "Pstatus": Pstatus,
        "Mjob": Mjob,
        "Fjob": Fjob,
        "reason": reason,
        "guardian": guardian,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "nursery": nursery,
        "higher": higher,
        "internet": internet,
        "romantic": romantic
    }

    # Convert user input into a DataFrame
   
    # Create a dictionary with all model features initialized to 0
    row = {col: 0 for col in model.feature_names_in_}

    # Numerical features
    numerical_features = {
        "age": age,
        "Medu": Medu,
        "Fedu": Fedu,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences
    }

    row.update(numerical_features)

    # Categorical features: match the training columns
    categorical_features = {
        "school_MS": school == "MS",
        "sex_M": sex == "M",
        "address_U": address == "U",
        "famsize_LE3": famsize == "LE3",
        "Pstatus_T": Pstatus == "T",

        "Mjob_health": Mjob == "health",
        "Mjob_other": Mjob == "other",
        "Mjob_services": Mjob == "services",
        "Mjob_teacher": Mjob == "teacher",

        "Fjob_health": Fjob == "health",
        "Fjob_other": Fjob == "other",
        "Fjob_services": Fjob == "services",
        "Fjob_teacher": Fjob == "teacher",

        "reason_home": reason == "home",
        "reason_other": reason == "other",
        "reason_reputation": reason == "reputation",

        "guardian_mother": guardian == "mother",
        "guardian_other": guardian == "other",

        "schoolsup_yes": schoolsup == "yes",
        "famsup_yes": famsup == "yes",
        "paid_yes": paid == "yes",
        "activities_yes": activities == "yes",
        "nursery_yes": nursery == "yes",
        "higher_yes": higher == "yes",
        "internet_yes": internet == "yes",
        "romantic_yes": romantic == "yes"
    }

    row.update(categorical_features)

    # Create DataFrame in the exact training feature order
    input_df = pd.DataFrame(
        [row],
        columns=model.feature_names_in_
    )

    # Make prediction
    st.write("Input features:")
    st.write(input_df.T)
    prediction = model.predict(input_df)[0]

    # Display result
    st.success(
        f"Predicted Final Grade: {prediction:.2f} / 20"
    )

    if prediction >= 10:
        st.write("The predicted grade is at or above 10.")
    else:
        st.warning("The predicted grade is below 10.")

    st.caption(
        "This is an estimated grade generated by a "
        "machine learning model, not a guaranteed result."
    )
