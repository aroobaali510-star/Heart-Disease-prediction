
import streamlit as st
import pandas as pd
import joblib

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("heart_disease_pipeline.pkl")

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ---------- Main background ---------- */

.stApp {
    background:
        radial-gradient(circle at 15% 20%, rgba(0, 180, 255, 0.08), transparent 30%),
        radial-gradient(circle at 85% 80%, rgba(255, 0, 100, 0.07), transparent 30%),
        #050505;
    color: #f5f5f5;
}

/* ---------- Hide Streamlit branding ---------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* ---------- Main container ---------- */

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ---------- Hero section ---------- */

.hero {
    text-align: center;
    padding: 35px 20px 25px;
    animation: fadeDown 1s ease;
}

.hero-icon {
    font-size: 58px;
    animation: heartbeat 1.6s infinite;
    display: inline-block;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    letter-spacing: -1px;
    margin: 10px 0 8px;
    background: linear-gradient(90deg, #ffffff, #8bdcff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #9ca3af;
    font-size: 17px;
    margin: 0 auto;
}

/* ---------- Cards ---------- */

.card {
    background: rgba(17, 17, 17, 0.82);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 22px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
    backdrop-filter: blur(12px);
    animation: fadeUp 0.8s ease;
}

.card-title {
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 18px;
    color: #ffffff;
}

.card-subtitle {
    color: #8d96a5;
    font-size: 14px;
    margin-bottom: 18px;
}

/* ---------- Input styling ---------- */

label {
    color: #d1d5db !important;
    font-weight: 600 !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background-color: #111111 !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 10px !important;
    color: white !important;
    transition: all 0.25s ease;
}

div[data-baseweb="input"] > div:hover,
div[data-baseweb="select"] > div:hover {
    border-color: #4cc9f0 !important;
    box-shadow: 0 0 12px rgba(76,201,240,0.12);
}

input {
    color: white !important;
}

/* ---------- Selectbox text ---------- */

iv[data-baseweb="select"] {
    background-color: #111111 !important;
    color: #ffffff !important;
}

div[data-baseweb="select"] > div {
    background-color: #111111 !important;
    border: 1px solid #2a2a2a !important;
}

div[data-baseweb="select"] span {
    color: #ffffff !important;
}

div[data-baseweb="select"] input {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

/* ---------- Button ---------- */

.stButton > button {
    width: 100%;
    height: 55px;
    border: none;
    border-radius: 12px;
    background: linear-gradient(90deg, #087ea4, #0ea5e9);
    color: white;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 0.3px;
    transition: all 0.3s ease;
    box-shadow: 0 8px 25px rgba(14,165,233,0.22);
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 35px rgba(14,165,233,0.35);
}

.stButton > button:active {
    transform: scale(0.98);
}

/* ---------- Result ---------- */

.result-card {
    text-align: center;
    padding: 28px;
    border-radius: 18px;
    margin-top: 25px;
    animation: resultPop 0.6s ease;
}

.result-danger {
    background: rgba(127, 29, 29, 0.22);
    border: 1px solid rgba(248,113,113,0.35);
}

.result-safe {
    background: rgba(6, 78, 59, 0.22);
    border: 1px solid rgba(52,211,153,0.35);
}

.result-icon {
    font-size: 42px;
    margin-bottom: 8px;
}

.result-title {
    font-size: 25px;
    font-weight: 800;
}

.result-text {
    color: #aeb6c2;
    margin-top: 8px;
}

/* ---------- Info strip ---------- */

.info-strip {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin: 12px 0 30px;
}

.badge {
    background: #111111;
    border: 1px solid #252525;
    border-radius: 30px;
    padding: 8px 15px;
    color: #aeb6c2;
    font-size: 13px;
}

/* ---------- Footer ---------- */

.app-footer {
    text-align: center;
    color: #6b7280;
    font-size: 13px;
    padding: 30px 0 10px;
}

/* ---------- Animations ---------- */

@keyframes heartbeat {
    0%, 100% {
        transform: scale(1);
    }
    14% {
        transform: scale(1.18);
    }
    28% {
        transform: scale(1);
    }
    42% {
        transform: scale(1.12);
    }
    70% {
        transform: scale(1);
    }
}

@keyframes fadeDown {
    from {
        opacity: 0;
        transform: translateY(-25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes resultPop {
    0% {
        opacity: 0;
        transform: scale(0.92);
    }
    100% {
        opacity: 1;
        transform: scale(1);
    }
}

/* ---------- Mobile ---------- */

@media (max-width: 700px) {

    .hero h1 {
        font-size: 34px;
    }

    .hero-icon {
        font-size: 45px;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">
    <div class="heart">❤️</div>
    <h1>Heart Disease Prediction</h1>
    <p>Machine Learning powered heart disease prediction system</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# INPUT SECTION
# ============================================================

st.markdown("""
<div class="card">
<div class="card-title">Patient Information</div>
<div class="card-subtitle">
Enter the patient's clinical information below.
</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=50
    )

    sex = st.selectbox(
        "Sex",
        [0, 1],
        format_func=lambda x: "Female" if x == 0 else "Male"
    )

    cp = st.selectbox(
        "Chest Pain Type",
        [0, 1, 2, 3]
    )

    trestbps = st.number_input(
        "Resting Blood Pressure",
        min_value=50,
        max_value=250,
        value=120
    )

with col2:

    chol = st.number_input(
        "Cholesterol",
        min_value=50,
        max_value=700,
        value=200
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    restecg = st.selectbox(
        "Resting ECG Results",
        [0, 1, 2]
    )

    thalach = st.number_input(
        "Maximum Heart Rate",
        min_value=50,
        max_value=250,
        value=150
    )

with col3:

    exang = st.selectbox(
        "Exercise Induced Angina",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    oldpeak = st.number_input(
        "Oldpeak",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

    slope = st.selectbox(
        "Slope",
        [0, 1, 2]
    )

    ca = st.selectbox(
        "Major Vessels (ca)",
        [0, 1, 2, 3, 4]
    )

thal = st.selectbox(
    "Thal",
    [0, 1, 2, 3]
)

st.write("")

# ============================================================
# PREDICTION
# ============================================================

# Prediction button

if st.button("Analyze Patient"):

    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "cp": [cp],
        "trestbps": [trestbps],
        "chol": [chol],
        "fbs": [fbs],
        "restecg": [restecg],
        "thalach": [thalach],
        "exang": [exang],
        "oldpeak": [oldpeak],
        "slope": [slope],
        "ca": [ca],
        "thal": [thal]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:

        st.error("Higher Likelihood of Heart Disease")

    else:

        st.success("Lower Likelihood of Heart Disease")
# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="app-footer">
    Built with Python · Pandas · Scikit-learn · Streamlit
    <br><br>
    This application is for educational purposes only and is not a medical diagnosis.
</div>
""", unsafe_allow_html=True)

