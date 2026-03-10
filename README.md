# ❤️ Heart Disease Risk Prediction System

An AI-powered web application that predicts the risk of heart disease using machine learning. Built for the Healthcare Hackathon Challenge.

## 🎯 Features

- **Real-time Predictions**: Get instant heart disease risk assessment
- **Model Insights**: Understand feature importance and model performance
- **Interactive Dashboard**: Explore data visualizations and patterns
- **Medical-Grade Analysis**: Built with scikit-learn Random Forest classifier

## 🏥 Challenges Addressed

✅ Challenge 1: Data Analysis & Visualization  
✅ Challenge 2: Predictive Modeling  
✅ Challenge 3: Data Cleaning & Feature Engineering  
✅ Challenge 4: AI/ML Solution for Real-World Problem  
✅ Challenge 5: Data Storytelling  

## 📊 Model Performance

- **Accuracy**: ~85%
- **ROC-AUC**: ~0.90
- **Precision**: 90%+
- **Recall**: Balanced

## 🚀 Quick Start - Local Development

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. **Clone the repository** (or extract files)
   ```bash
   git clone https://github.com/YOUR_USERNAME/heart-disease-predictor.git
   cd heart-disease-predictor
   ```

2. **Create virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Open your browser**
   ```
   http://localhost:8501
   ```

## 🌐 Deployment on Streamlit Cloud

### Step 1: Prepare GitHub Repository

```bash
# Initialize git (if not done)
git init
git add .
git commit -m "Initial commit - Heart Disease Predictor"

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/heart-disease-predictor.git
git branch -M main
git push -u origin main
```

### Step 2: Create Streamlit Cloud Account

1. Visit [share.streamlit.io](https://share.streamlit.io)
2. Sign up with your GitHub account
3. Authorize Streamlit to access your repositories

### Step 3: Deploy the Application

1. Click **"New app"** in Streamlit Cloud dashboard
2. Select your repository:
   - **Repository**: YOUR_USERNAME/heart-disease-predictor
   - **Branch**: main
   - **Main file path**: streamlit_app.py
3. Click **"Deploy"**
4. Wait 2-3 minutes for deployment

### Step 4: Access Your Live App

Your application will be available at:
```
https://heart-disease-predictor.streamlit.app
```

## 📁 Project Structure

```
heart-disease-predictor/
├── streamlit_app.py          # Main application
├── Untitled.ipynb            # Jupyter notebook for model training
├── heart.csv                 # Dataset
├── rf_model.pkl              # Trained Random Forest model
├── scaler.pkl                # Feature scaler
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore file
├── .streamlit/
│   └── config.toml           # Streamlit configuration
└── README.md                 # This file
```

## 📋 Requirements

- pandas==2.0.3
- numpy==1.24.3
- scikit-learn==1.3.0
- matplotlib==3.7.2
- seaborn==0.12.2
- streamlit==1.28.1

## 🔧 Configuration Files

### `.streamlit/config.toml`
Configures Streamlit appearance and behavior:
- Theme colors for professional look
- Max upload size
- Error details visibility

### `.gitignore`
Prevents unnecessary files from being committed:
- Virtual environments
- Python cache files
- IDE configuration
- Jupyter checkpoints

## ⚠️ Medical Disclaimer

This application is a **demonstration tool for educational purposes only**. It should not be used for actual medical diagnosis or treatment decisions. Always consult qualified healthcare professionals for medical advice.

## 📚 Dataset Information

- **Source**: UCI Heart Disease Dataset
- **Samples**: 1,027 patients
- **Features**: 13 clinical parameters
- **Classes**: Binary (Disease present/absent)

### Features

1. **age** - Age of the patient (years)
2. **sex** - Gender (0=Female, 1=Male)
3. **cp** - Chest pain type (0-3)
4. **trestbps** - Resting blood pressure (mmHg)
5. **chol** - Serum cholesterol (mg/dl)
6. **fbs** - Fasting blood sugar > 120 mg/dl
7. **restecg** - Resting ECG results
8. **thalach** - Maximum heart rate achieved
9. **exang** - Exercise induced angina
10. **oldpeak** - ST depression induced by exercise
11. **slope** - Slope of ST segment
12. **ca** - Number of major vessels
13. **thal** - Thalassemia type

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python-based GUI)
- **ML Framework**: scikit-learn
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Deployment**: Streamlit Cloud (AWS)

## 📝 How to Use

### Make a Prediction
1. Navigate to "Make Prediction" tab
2. Enter patient health metrics
3. Click "Predict Risk"
4. View risk assessment with confidence score

### View Model Insights
1. Go to "Model Insights" tab
2. Explore feature importance
3. Review model performance metrics
4. Analyze confusion matrix and ROC curve

### Learn About the Project
1. Visit "About" page
2. Read project overview and challenges addressed
3. Review deployment instructions

## 🚀 Future Improvements

- Add export functionality for predictions
- Implement batch prediction feature
- Integrate real medical APIs
- Add patient data storage
- Implement multi-language support
- Add interpretability features (SHAP values)

## 💬 Support & Questions

For issues, questions, or suggestions, please open an issue on GitHub.

## 📄 License

This project is open source and available for educational purposes.

---

**Built for Healthcare Hackathon 2026 | ML & Data Science Challenge**

Last Updated: March 2026
