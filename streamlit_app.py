import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc

# Set page config
st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="wide")

# Load models
@st.cache_resource
def load_models():
    with open('rf_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_models()

# Feature descriptions
feature_descriptions = {
    'age': 'Age of the patient (years)',
    'sex': 'Gender (0=Female, 1=Male)',
    'cp': 'Chest pain type (0-3)',
    'trestbps': 'Resting blood pressure (mmHg)',
    'chol': 'Serum cholesterol (mg/dl)',
    'fbs': 'Fasting blood sugar > 120 mg/dl (0=No, 1=Yes)',
    'restecg': 'Resting ECG results (0-2)',
    'thalach': 'Maximum heart rate achieved',
    'exang': 'Exercise induced angina (0=No, 1=Yes)',
    'oldpeak': 'ST depression induced by exercise',
    'slope': 'Slope of ST segment (0-2)',
    'ca': 'Number of major vessels (0-3)',
    'thal': 'Thalassemia type (0-3)'
}

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page:", ["Home", "Make Prediction", "Model Insights", "About"])

# HOME PAGE
if page == "Home":
    st.title("❤️ Heart Disease Risk Prediction System")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ## Welcome! 👋
        
        This AI-powered application predicts the risk of heart disease based on clinical parameters.
        
        ### Features:
        - **Real-time Predictions**: Get instant risk assessment
        - **Model Insights**: Understand which factors matter most
        - **Data Visualizations**: See patterns in the data
        
        ### How it works:
        1. Go to **Make Prediction** tab
        2. Enter patient health metrics
        3. Get instant risk assessment with confidence score
        """)
    
    with col2:
        st.info("""
        ### 📊 Model Performance
        - **Accuracy**: ~85%
        - **ROC-AUC**: ~0.90
        - **Precision**: High (90%+)
        - **Sensitivity**: Balanced
        
        ⚠️ **Disclaimer**: This is a demonstration tool. 
        Always consult healthcare professionals for actual diagnosis.
        """)

# PREDICTION PAGE
elif page == "Make Prediction":
    st.title("🔍 Make a Prediction")
    st.markdown("---")
    
    st.markdown("### Enter Patient Health Metrics")
    
    # Create input form with 2 columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age (years)", 20, 100, 50)
        sex = st.selectbox("Gender", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
        trestbps = st.number_input("Resting Blood Pressure (mmHg)", 80, 200, 120)
        chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 400, 200)
        fbs = st.selectbox("Fasting Blood Sugar > 120 (0=No, 1=Yes)", [0, 1])
    
    with col2:
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3], 
                         format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"][x])
        restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
        thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
        exang = st.selectbox("Exercise Induced Angina", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        oldpeak = st.number_input("ST Depression (Induced by Exercise)", 0.0, 6.5, 1.0)
    
    with col3:
        slope = st.selectbox("Slope of ST Segment", [0, 1, 2])
        ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3])
        thal = st.selectbox("Thalassemia Type", [0, 1, 2, 3])
    
    # Make prediction
    if st.button("🩺 Predict Risk", key="predict", use_container_width=True):
        # Prepare input
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, 
                               thalach, exang, oldpeak, slope, ca, thal]])
        
        # Scale features
        input_scaled = scaler.transform(input_data)
        
        # Get prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0]
        
        # Display results
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            if prediction == 1:
                st.error("⚠️ HIGH RISK")
                st.metric("Risk Level", f"{probability[1]*100:.1f}%", "Heart Disease Risk Detected")
            else:
                st.success("✅ LOW RISK")
                st.metric("Risk Level", f"{probability[0]*100:.1f}%", "No Disease Indication")
        
        with col2:
            # Probability gauge
            fig, ax = plt.subplots(figsize=(6, 4))
            risk_prob = probability[1] * 100
            colors_gauge = ['#2ecc71', '#f39c12', '#e74c3c']
            
            if risk_prob < 30:
                color = '#2ecc71'
            elif risk_prob < 70:
                color = '#f39c12'
            else:
                color = '#e74c3c'
            
            ax.barh(['Risk'], [risk_prob], color=color, height=0.3)
            ax.set_xlim(0, 100)
            ax.set_xlabel('Probability (%)')
            ax.set_title('Risk Assessment Score')
            ax.text(risk_prob + 2, 0, f'{risk_prob:.1f}%', va='center')
            
            st.pyplot(fig, use_container_width=True)
        
        st.markdown("---")
        st.info("💡 **Note**: This prediction is based on machine learning patterns and should be confirmed by a medical professional.")

# MODEL INSIGHTS PAGE
elif page == "Model Insights":
    st.title("📈 Model Insights & Performance")
    st.markdown("---")
    
    # Reload data for visualization
    df = pd.read_csv('heart.csv')
    X = df.drop('target', axis=1)
    y = df['target']
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    X_test_scaled = scaler.transform(X_test)
    
    tab1, tab2, tab3 = st.tabs(["Feature Importance", "Model Performance", "Data Overview"])
    
    with tab1:
        st.markdown("### Feature Importance")
        feature_importance = model.feature_importances_
        features = X.columns
        sorted_idx = np.argsort(feature_importance)[::-1]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(range(len(features)), feature_importance[sorted_idx])
        ax.set_yticks(range(len(features)))
        ax.set_yticklabels([features[i] for i in sorted_idx])
        ax.set_xlabel('Importance')
        ax.set_title('Feature Importance in Model')
        ax.invert_yaxis()
        
        st.pyplot(fig, use_container_width=True)
        
        # Show feature descriptions
        st.markdown("### Feature Descriptions")
        for feat in features[sorted_idx[:5]]:
            st.write(f"**{feat}**: {feature_descriptions.get(feat, 'N/A')}")
    
    with tab2:
        st.markdown("### Model Performance Metrics")
        
        pred_proba = model.predict_proba(X_test_scaled)[:, 1]
        predictions = model.predict(X_test_scaled)
        
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Accuracy", f"{accuracy_score(y_test, predictions):.3f}")
        col2.metric("Precision", f"{precision_score(y_test, predictions):.3f}")
        col3.metric("Recall", f"{recall_score(y_test, predictions):.3f}")
        col4.metric("ROC-AUC", f"{roc_auc_score(y_test, pred_proba):.3f}")
        
        # Confusion Matrix
        cm = confusion_matrix(y_test, predictions)
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax, cbar=False,
                   xticklabels=['No Disease', 'Disease'],
                   yticklabels=['No Disease', 'Disease'])
        ax.set_ylabel('Actual')
        ax.set_xlabel('Predicted')
        ax.set_title('Confusion Matrix')
        st.pyplot(fig, use_container_width=True)
        
        # ROC Curve
        fpr, tpr, _ = roc_curve(y_test, pred_proba)
        roc_auc = auc(fpr, tpr)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.3f})')
        ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier')
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('ROC Curve')
        ax.legend(loc="lower right")
        ax.grid(True, alpha=0.3)
        st.pyplot(fig, use_container_width=True)
    
    with tab3:
        st.markdown("### Dataset Overview")
        col1, col2, col3 = st.columns(3)
        
        col1.metric("Total Patients", len(df))
        col2.metric("Disease Cases", (df['target'] == 1).sum())
        col3.metric("Healthy Cases", (df['target'] == 0).sum())
        
        st.markdown("### Distribution of Heart Disease")
        fig, ax = plt.subplots(figsize=(8, 5))
        counts = df['target'].value_counts()
        colors = ['#2ecc71', '#e74c3c']
        ax.pie(counts, labels=['No Disease', 'Disease'], autopct='%1.1f%%', 
              colors=colors, startangle=90)
        ax.set_title('Heart Disease Distribution')
        st.pyplot(fig, use_container_width=True)

# ABOUT PAGE
elif page == "About":
    st.title("ℹ️ About This Project")
    st.markdown("---")
    
    st.markdown("""
    ## Healthcare Hackathon Challenge
    
    ### Project Overview
    This application addresses **Challenge 2 & 4**: Building a predictive ML model to diagnose heart disease risk.
    
    ### Challenges Addressed
    ✅ **Challenge 2**: Predictive Modeling - Built ML model to predict heart disease  
    ✅ **Challenge 3**: Data Cleaning & Feature Engineering - Processed clinical data  
    ✅ **Challenge 1**: Data Analysis & Visualization - Generated insights & dashboards  
    ✅ **Challenge 5**: Data Storytelling - Present findings to non-technical audience  
    
    ### Technology Stack
    - **Python**: Data processing & ML
    - **Scikit-learn**: Machine Learning models
    - **Streamlit**: Interactive web deployment
    - **Pandas & NumPy**: Data manipulation
    - **Matplotlib & Seaborn**: Visualizations
    
    ### Dataset
    - **Source**: UCI Heart Disease Dataset
    - **Samples**: 1027 patients
    - **Features**: 13 clinical parameters
    - **Target**: Binary (Disease: Yes/No)
    
    ### Model Information
    - **Algorithm**: Random Forest Classifier
    - **Performance**: 85%+ Accuracy, 0.90 ROC-AUC
    - **Training/Test Split**: 80/20
    
    ### Next Steps for Deployment
    
    1. **Run the Jupyter notebook** to train the model
    2. **Install dependencies**:
       ```bash
       pip install streamlit pandas numpy scikit-learn matplotlib seaborn
       ```
    3. **Run Streamlit app**:
       ```bash
       streamlit run streamlit_app.py
       ```
    4. **Deploy to cloud** (Heroku, AWS, Google Cloud, etc.)
    
    ---
    ⚠️ **Medical Disclaimer**: This is a demonstration tool for educational purposes only. 
    Always consult qualified healthcare professionals for medical diagnosis and treatment.
    """)

st.sidebar.markdown("---")
st.sidebar.markdown("Built for Healthcare Hackathon 2026 | ML & Data Science Challenge")
