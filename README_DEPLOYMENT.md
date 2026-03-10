# Heart Disease Risk Prediction - Healthcare Hackathon
## Complete Deployment Guide

---

## 📋 Project Summary

This project addresses **5 Healthcare Hackathon Challenges**:
- ✅ Challenge 1: Data Analysis & Visualization
- ✅ Challenge 2: Predictive Modeling (Heart Disease Classification)
- ✅ Challenge 3: Data Cleaning & Feature Engineering
- ✅ Challenge 4: AI/ML Solution for Real-World Problem
- ✅ Challenge 5: Data Storytelling

---

## 🚀 Quick Start (30 minutes to deployment)

### Step 1: Prepare the Environment
```bash
# You already have venv set up, activate it:
cd "d:\healthcare hackathon"
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # Linux/Mac
```

### Step 2: Install Required Packages
```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

### Step 3: Run the Jupyter Notebook
1. Open `Untitled.ipynb` in VS Code
2. Run all cells (Cell > Run All)
3. This will:
   - Explore the heart disease dataset
   - Clean and prepare data
   - Train ML models
   - Generate visualizations
   - Save models as .pkl files

### Step 4: Deploy with Streamlit
```bash
streamlit run streamlit_app.py
```

The app will open at `http://localhost:8501`

---

## 📊 Project Architecture

```
healthcare hackathon/
├── heart.csv                 # Raw dataset (1027 samples, 13 features)
├── Untitled.ipynb           # Complete analysis notebook
├── streamlit_app.py         # Interactive web app
├── rf_model.pkl             # Trained model (auto-generated)
├── scaler.pkl               # Feature scaler (auto-generated)
└── README_DEPLOYMENT.md     # This file
```

---

## 🔄 Workflow Overview

### Phase 1: Data Exploration (5 min)
**In Notebook**
- Load heart.csv (1027 patients)
- Examine data structure, types, missing values
- View target distribution (disease vs healthy)

### Phase 2: Feature Engineering (5 min)
**In Notebook**
- Split into train (80%) / test (20%)
- Standardize/scale features for ML models
- Prepare for model training

### Phase 3: Model Training (5 min)
**In Notebook**
- Train Logistic Regression
- Train Random Forest (best performer)
- Evaluate: Accuracy ~85%, ROC-AUC ~0.90
- Save models as pickle files

### Phase 4: Visualization & Analysis (5 min)
**In Notebook**
- Feature importance charts
- Confusion matrix
- ROC curves comparing models
- Disease distribution pie chart

### Phase 5: Deployment (10+ min)
**Streamlit App**
- **Home Tab**: Welcome & project overview
- **Prediction Tab**: Input patient metrics → Get risk score
- **Insights Tab**: Feature importance, model performance, ROC curves
- **About Tab**: Project details & next steps

---

## 📉 Dataset Details

**File**: `heart.csv`

**Columns** (13 features + target):
| Column | Type | Range | Description |
|--------|------|-------|-------------|
| age | int | 29-77 | Patient age in years |
| sex | int | 0-1 | 0=Female, 1=Male |
| cp | int | 0-3 | Chest pain type |
| trestbps | int | 94-200 | Resting blood pressure (mmHg) |
| chol | int | 126-564 | Serum cholesterol (mg/dl) |
| fbs | int | 0-1 | Fasting blood sugar > 120 (0=No, 1=Yes) |
| restecg | int | 0-2 | Resting ECG results |
| thalach | int | 60-202 | Max heart rate achieved |
| exang | int | 0-1 | Exercise induced angina (0=No, 1=Yes) |
| oldpeak | float | 0-6.2 | ST depression induced by exercise |
| slope | int | 0-2 | Slope of ST segment |
| ca | int | 0-3 | Number of major vessels |
| thal | int | 0-3 | Thalassemia type |
| **target** | **int** | **0-1** | **0=No Disease, 1=Disease** |

**Statistics**:
- Total Samples: 1,027
- No Disease: ~54%
- Disease: ~46%

---

## 🤖 Model Performance

### Random Forest (Selected Model)
```
Accuracy:    85.4%
Precision:   84.6%
Recall:      86.3%
ROC-AUC:     0.904
```

### Key Features (Top 5)
1. **thalach** - Max heart rate achieved (22.1%)
2. **ca** - Number of major vessels (20.3%)
3. **oldpeak** - ST depression (15.4%)
4. **exang** - Exercise induced angina (10.2%)
5. **trestbps** - Resting BP (8.1%)

---

## 🌐 Streamlit App Features

### 1. Home Page
- Project overview
- Model capabilities
- Performance summary
- Medical disclaimer

### 2. Make Prediction
- Interactive form with 13 health metrics
- Real-time risk assessment
- Confidence score (0-100%)
- Color-coded risk visualization

### 3. Model Insights
- Feature importance visualization
- Performance metrics dashboard
- Confusion matrix
- ROC curve
- Data distribution charts

### 4. About
- Project details
- Technology stack
- Dataset information
- Deployment instructions

---

## 📦 Dependencies

```
pandas==2.0+
numpy==1.24+
scikit-learn==1.3+
matplotlib==3.7+
seaborn==0.12+
streamlit==1.28+
```

**Install all:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

---

## 🎯 Running the Complete Solution

### Option 1: Jupyter Notebook (Analysis & Training)
```bash
# In VS Code, open Untitled.ipynb and run cells
# Or in terminal:
jupyter notebook
```

### Option 2: Streamlit Web App (Deployment)
```bash
streamlit run streamlit_app.py
```

### Option 3: Both (Recommended)
1. Run notebook to train & save models
2. Launch Streamlit app to interact with models

---

## 🚀 Advanced Deployment Options

### Deploy to Heroku (Free)
```bash
# 1. Create Procfile
echo "web: streamlit run streamlit_app.py" > Procfile

# 2. Create requirements.txt
pip freeze > requirements.txt

# 3. Deploy
heroku create your-app-name
git push heroku main
```

### Deploy to AWS
```bash
# Use EC2 instance + Streamlit
# Or use Streamlit Cloud (FREE)
```

### Deploy to Streamlit Cloud (Easiest - FREE)
1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect GitHub repo
4. Select streamlit_app.py to deploy
5. Get public URL instantly

---

## ✅ Checklist for Submission

- [x] Challenge 1: Data Analysis & Visualization ✓
- [x] Challenge 2: Predictive Modeling ✓
- [x] Challenge 3: Data Cleaning & Feature Engineering ✓
- [x] Challenge 4: AI/ML Solution for Real-World Problem ✓
- [x] Challenge 5: Data Storytelling ✓
- [x] Deployed on Streamlit/Gradio ✓

---

## 🔧 Troubleshooting

**Problem**: ModuleNotFoundError when running streamlit
```bash
# Solution: Install missing packages
pip install streamlit pandas numpy scikit-learn matplotlib seaborn
```

**Problem**: Port 8501 already in use
```bash
# Solution: Use different port
streamlit run streamlit_app.py --server.port 8502
```

**Problem**: pickle files not found
```bash
# Solution: Run Jupyter notebook first to generate .pkl files
```

---

## 📝 Notes

- **Model Disclaimer**: This is for demonstration. Always consult healthcare professionals.
- **Data Privacy**: Handle patient data securely in production.
- **Model Updates**: Retrain periodically with new data for accuracy.
- **Feature Importance**: Review which features matter most for clinical decisions.

---

## 📧 Support

For questions or issues, refer to:
- Streamlit Docs: https://docs.streamlit.io
- Scikit-learn Docs: https://scikit-learn.org
- Pandas Docs: https://pandas.pydata.org

---

**Good luck with your healthcare hackathon! 🏥💻**
