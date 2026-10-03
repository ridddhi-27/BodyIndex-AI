
import streamlit as st
import numpy as np
import joblib
import time

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="BodyIndex AI",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ---------------------------------------------------------
   GLOBAL
--------------------------------------------------------- */

html, body, [class*="css"] {
    font-family: "Inter", "Segoe UI", sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255, 92, 0, 0.10), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(255, 120, 0, 0.08), transparent 25%),
        radial-gradient(circle at 50% 100%, rgba(255, 70, 0, 0.07), transparent 30%),
        #050505;
    color: #ffffff;
}

/* Remove default padding */

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* ---------------------------------------------------------
   HIDE STREAMLIT DEFAULT
--------------------------------------------------------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ---------------------------------------------------------
   ANIMATED BACKGROUND
--------------------------------------------------------- */

.stApp::before {
    content: "";
    position: fixed;
    width: 500px;
    height: 500px;
    border-radius: 50%;
    background: rgba(255, 76, 0, 0.05);
    filter: blur(100px);
    top: 15%;
    left: -150px;
    z-index: -1;
    animation: floatGlow 7s ease-in-out infinite alternate;
}

.stApp::after {
    content: "";
    position: fixed;
    width: 450px;
    height: 450px;
    border-radius: 50%;
    background: rgba(255, 130, 0, 0.04);
    filter: blur(100px);
    right: -150px;
    bottom: 10%;
    z-index: -1;
    animation: floatGlow2 8s ease-in-out infinite alternate;
}

@keyframes floatGlow {
    from {
        transform: translateY(0px);
    }
    to {
        transform: translateY(80px);
    }
}

@keyframes floatGlow2 {
    from {
        transform: translateY(0px);
    }
    to {
        transform: translateY(-80px);
    }
}

/* ---------------------------------------------------------
   NAVBAR
--------------------------------------------------------- */

.navbar {
    height: 72px;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(12,12,12,0.75);
    backdrop-filter: blur(20px);
    border-radius: 18px;
    padding: 0 24px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    box-shadow:
        0 10px 50px rgba(0,0,0,0.35),
        inset 0 1px rgba(255,255,255,0.03);
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo-icon {
    width: 40px;
    height: 40px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 12px;

    background: linear-gradient(
        135deg,
        #ff5a00,
        #ff8a3d
    );

    color: white;
    font-size: 21px;
    font-weight: 900;

    box-shadow:
        0 0 25px rgba(255, 90, 0, 0.35);
}

.logo-text {
    font-size: 20px;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.logo-text span {
    color: #ff641f;
}

.nav-right {
    display: flex;
    gap: 10px;
    align-items: center;
}

.nav-pill {
    padding: 8px 15px;
    border-radius: 30px;

    border: 1px solid rgba(255,255,255,0.08);

    color: #aaa;
    font-size: 13px;

    background: rgba(255,255,255,0.025);
}

.ai-pill {
    color: #ff7a38;

    border-color:
        rgba(255,100,30,0.25);

    background:
        rgba(255,80,0,0.07);
}

/* ---------------------------------------------------------
   HERO
--------------------------------------------------------- */

.hero {
    padding: 75px 0 45px 0;
}

.eyebrow {
    display: inline-block;

    padding: 8px 14px;

    border-radius: 30px;

    border: 1px solid rgba(255,100,30,0.25);

    background:
        rgba(255,80,0,0.07);

    color: #ff7840;

    font-size: 12px;
    font-weight: 700;

    letter-spacing: 1.5px;

    text-transform: uppercase;
}

.hero-title {
    margin-top: 22px;

    font-size: clamp(45px, 6vw, 78px);

    font-weight: 900;

    line-height: 0.98;

    letter-spacing: -4px;
}

.hero-title .gradient {
    background:
        linear-gradient(
            90deg,
            #ff5410,
            #ff914d,
            #ff5410
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    background-size: 200% auto;

    animation: gradientMove 4s linear infinite;
}

@keyframes gradientMove {
    to {
        background-position: 200% center;
    }
}

.hero-description {
    margin-top: 25px;

    max-width: 650px;

    color: #8d8d8d;

    font-size: 17px;

    line-height: 1.7;
}

/* ---------------------------------------------------------
   MAIN CARD
--------------------------------------------------------- */

.glass-card {
    background:
        linear-gradient(
            145deg,
            rgba(25,25,25,0.92),
            rgba(10,10,10,0.92)
        );

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 26px;

    padding: 30px;

    box-shadow:
        0 25px 70px rgba(0,0,0,0.45),
        inset 0 1px rgba(255,255,255,0.035);

    position: relative;

    overflow: hidden;
}

.glass-card::before {
    content: "";

    position: absolute;

    top: 0;
    left: 10%;

    width: 80%;
    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,100,30,0.6),
            transparent
        );
}

.card-title {
    font-size: 24px;
    font-weight: 800;
}

.card-subtitle {
    color: #777;
    margin-top: 5px;
    font-size: 13px;
}

/* ---------------------------------------------------------
   INPUT LABELS
--------------------------------------------------------- */

.input-label {
    color: #aaa;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 6px;
}

/* ---------------------------------------------------------
   STREAMLIT INPUTS
--------------------------------------------------------- */

div[data-baseweb="input"] {
    background: #111 !important;

    border:
        1px solid
        rgba(255,255,255,0.08) !important;

    border-radius: 12px !important;
}

div[data-baseweb="input"]:focus-within {
    border:
        1px solid
        rgba(255,100,30,0.65) !important;

    box-shadow:
        0 0 0 3px
        rgba(255,90,0,0.08) !important;
}

input {
    color: white !important;
}

div[data-baseweb="select"] > div {
    background: #111 !important;

    border:
        1px solid
        rgba(255,255,255,0.08) !important;

    border-radius: 12px !important;

    color: white !important;
}

/* ---------------------------------------------------------
   BUTTON
--------------------------------------------------------- */

.stButton > button {

    width: 100%;

    height: 52px;

    border-radius: 13px;

    border: none;

    color: white;

    font-weight: 800;

    font-size: 15px;

    background:
        linear-gradient(
            135deg,
            #ff5100,
            #ff7b32
        );

    box-shadow:
        0 10px 35px
        rgba(255,80,0,0.22);

    transition:
        all 0.25s ease;
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 15px 45px
        rgba(255,80,0,0.38);

    background:
        linear-gradient(
            135deg,
            #ff641f,
            #ff914d
        );
}

/* ---------------------------------------------------------
   RESULT CARD
--------------------------------------------------------- */

.result-card {

    margin-top: 20px;

    border-radius: 22px;

    padding: 30px;

    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(255,80,0,0.14),
            transparent 55%
        ),
        #0d0d0d;

    border:
        1px solid
        rgba(255,100,30,0.22);

    text-align: center;

    box-shadow:
        0 20px 60px
        rgba(255,70,0,0.08);
}

.result-small {
    color: #777;

    font-size: 12px;

    text-transform: uppercase;

    letter-spacing: 2px;
}

.result-number {

    font-size: 85px;

    line-height: 1;

    font-weight: 900;

    margin: 12px 0;

    background:
        linear-gradient(
            135deg,
            #ffffff,
            #ff7040
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.result-category {

    display: inline-block;

    padding: 9px 18px;

    border-radius: 30px;

    color: #ff8b55;

    border:
        1px solid
        rgba(255,100,30,0.25);

    background:
        rgba(255,80,0,0.08);

    font-weight: 700;

    font-size: 13px;
}

/* ---------------------------------------------------------
   METRICS
--------------------------------------------------------- */

.metric-card {

    background:
        rgba(255,255,255,0.025);

    border:
        1px solid
        rgba(255,255,255,0.07);

    border-radius: 18px;

    padding: 22px;

    transition:
        transform .25s ease,
        border .25s ease;
}

.metric-card:hover {

    transform: translateY(-4px);

    border:
        1px solid
        rgba(255,100,30,0.3);
}

.metric-icon {
    font-size: 25px;
}

.metric-value {

    font-size: 25px;

    font-weight: 800;

    margin-top: 10px;
}

.metric-label {

    color: #777;

    font-size: 12px;

    margin-top: 4px;
}

/* ---------------------------------------------------------
   INFO SECTION
--------------------------------------------------------- */

.section-heading {

    font-size: 28px;

    font-weight: 800;

    letter-spacing: -1px;

    margin-top: 45px;
}

.section-description {

    color: #777;

    font-size: 14px;

    margin-top: 5px;
}

.info-card {

    margin-top: 20px;

    background:
        rgba(255,255,255,0.025);

    border:
        1px solid
        rgba(255,255,255,0.07);

    border-radius: 20px;

    padding: 25px;

    min-height: 150px;
}

.info-number {

    color: #ff641f;

    font-size: 13px;

    font-weight: 800;

    letter-spacing: 1px;
}

.info-title {

    font-size: 18px;

    font-weight: 750;

    margin-top: 12px;
}

.info-text {

    color: #777;

    font-size: 13px;

    line-height: 1.6;

    margin-top: 7px;
}

/* ---------------------------------------------------------
   FOOTER
--------------------------------------------------------- */

.footer {

    text-align: center;

    margin-top: 70px;

    padding-top: 25px;

    border-top:
        1px solid
        rgba(255,255,255,0.06);

    color: #555;

    font-size: 12px;
}

.footer span {
    color: #ff641f;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVBAR
# ============================================================

st.markdown("""
<div class="navbar">

    <div class="logo">

        <div class="logo-icon">
            ◈
        </div>

        <div class="logo-text">
            BodyIndex<span>AI</span>
        </div>

    </div>

    <div class="nav-right">

        <div class="nav-pill">
            ML CLASSIFIER
        </div>

        <div class="nav-pill ai-pill">
            ● AI ACTIVE
        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

    <div class="eyebrow">
        ✦ Intelligent Body Analysis
    </div>

    <div class="hero-title">
        Understand your body.<br>
        <span class="gradient">Know your index.</span>
    </div>

    <div class="hero-description">
        A machine-learning powered prediction system that
        analyzes your gender, height and weight to determine
        your predicted body index category.
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MAIN COLUMNS
# ============================================================

left, right = st.columns(
    [1, 1],
    gap="large"
)


# ============================================================
# INPUT PANEL
# ============================================================

with left:

    st.markdown("""
    <div class="glass-card">

        <div class="card-title">
            ◉ Prediction Engine
        </div>

        <div class="card-subtitle">
            Enter your physical parameters
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    height = st.number_input(
        "Height (cm)",
        min_value=50.0,
        max_value=250.0,
        value=170.0,
        step=1.0
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=20.0,
        max_value=250.0,
        value=65.0,
        step=1.0
    )

    st.write("")

    predict_button = st.button(
        "⚡ ANALYZE MY INDEX"
    )


# ============================================================
# RESULT PANEL
# ============================================================

with right:

    if predict_button:

        gender_value = 1 if gender == "Male" else 0

        input_data = np.array([
            [gender_value, height, weight]
        ])

        input_scaled = scaler.transform(
            input_data
        )

        prediction = model.predict(
            input_scaled
        )

        index = int(prediction[0])

        categories = {
            0: "Extremely Weak",
            1: "Weak",
            2: "Normal",
            3: "Overweight",
            4: "Obesity",
            5: "Extreme Obesity"
        }

        category = categories.get(
            index,
            "Unknown"
        )

        st.markdown(f"""
        <div class="result-card">

            <div class="result-small">
                AI PREDICTION
            </div>

            <div class="result-number">
                {index}
            </div>

            <div class="result-category">
                {category}
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        # Metrics
        m1, m2, m3 = st.columns(3)

        with m1:
            st.markdown(f"""
            <div class="metric-card">

                <div class="metric-icon">
                    ♀♂
                </div>

                <div class="metric-value">
                    {gender}
                </div>

                <div class="metric-label">
                    GENDER
                </div>

            </div>
            """, unsafe_allow_html=True)

        with m2:
            st.markdown(f"""
            <div class="metric-card">

                <div class="metric-icon">
                    ↕
                </div>

                <div class="metric-value">
                    {height:.0f}
                </div>

                <div class="metric-label">
                    HEIGHT / CM
                </div>

            </div>
            """, unsafe_allow_html=True)

        with m3:
            st.markdown(f"""
            <div class="metric-card">

                <div class="metric-icon">
                    ◉
                </div>

                <div class="metric-value">
                    {weight:.0f}
                </div>

                <div class="metric-label">
                    WEIGHT / KG
                </div>

            </div>
            """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="result-card" style="min-height:330px;
             display:flex;
             flex-direction:column;
             justify-content:center;
             align-items:center;">

            <div style="
                font-size:65px;
                margin-bottom:15px;
            ">
                ◈
            </div>

            <div style="
                font-size:20px;
                font-weight:800;
            ">
                Awaiting Analysis
            </div>

            <div style="
                color:#666;
                margin-top:8px;
                font-size:13px;
            ">
                Enter your details and launch the AI engine.
            </div>

            <div style="
                margin-top:25px;
                color:#ff641f;
                font-size:11px;
                letter-spacing:2px;
            ">
                READY TO ANALYZE
            </div>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# HOW IT WORKS
# ============================================================

st.markdown("""
<div class="section-heading">
    How the intelligence works
</div>

<div class="section-description">
    Three simple stages from your data to the prediction.
</div>
""", unsafe_allow_html=True)


c1, c2, c3 = st.columns(3)


with c1:

    st.markdown("""
    <div class="info-card">

        <div class="info-number">
            01 / INPUT
        </div>

        <div class="info-title">
            Capture Parameters
        </div>

        <div class="info-text">
            Gender, height and weight are collected
            through the interactive prediction interface.
        </div>

    </div>
    """, unsafe_allow_html=True)


with c2:

    st.markdown("""
    <div class="info-card">

        <div class="info-number">
            02 / PROCESS
        </div>

        <div class="info-title">
            Machine Learning
        </div>

        <div class="info-text">
            Your trained classifier processes the
            standardized input and identifies the
            corresponding index class.
        </div>

    </div>
    """, unsafe_allow_html=True)


with c3:

    st.markdown("""
    <div class="info-card">

        <div class="info-number">
            03 / OUTPUT
        </div>

        <div class="info-title">
            Generate Result
        </div>

        <div class="info-text">
            The predicted index and corresponding
            category are displayed instantly.
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# MODEL STATUS
# ============================================================

st.markdown("""
<div class="section-heading">
    Model status
</div>

<div class="section-description">
    Your local machine-learning pipeline.
</div>
""", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)


with s1:
    st.markdown("""
    <div class="metric-card">

        <div class="metric-icon">◈</div>

        <div class="metric-value">
            ACTIVE
        </div>

        <div class="metric-label">
            MODEL STATUS
        </div>

    </div>
    """, unsafe_allow_html=True)


with s2:
    st.markdown("""
    <div class="metric-card">

        <div class="metric-icon">⚙</div>

        <div class="metric-value">
            ML
        </div>

        <div class="metric-label">
            PREDICTION ENGINE
        </div>

    </div>
    """, unsafe_allow_html=True)


with s3:
    st.markdown("""
    <div class="metric-card">

        <div class="metric-icon">↔</div>

        <div class="metric-value">
            3
        </div>

        <div class="metric-label">
            INPUT FEATURES
        </div>

    </div>
    """, unsafe_allow_html=True)


with s4:
    st.markdown("""
    <div class="metric-card">

        <div class="metric-icon">✓</div>

        <div class="metric-value">
            READY
        </div>

        <div class="metric-label">
            SYSTEM STATUS
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <span>◈ BodyIndex AI</span>
    &nbsp; • &nbsp;
    Machine Learning Classification System
    &nbsp; • &nbsp;
    Built with Python + Scikit-learn + Streamlit

</div>
""", unsafe_allow_html=True)

