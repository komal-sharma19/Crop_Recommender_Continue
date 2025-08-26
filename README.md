# Crop_Recommender_Continue




# 🌾 Crop Recommendation System  

A web-based application that leverages a machine learning model to recommend the most suitable crop to grow based on soil and environmental factors. This tool is designed to help farmers make informed decisions and improve their agricultural productivity.  

---

## 📋 Table of Contents  
- [Features](#-features)  
- [How It Works](#%EF%B8%8F-how-it-works)  
- [Technologies Used](#-technologies-used)  
- [Setup and Installation](#-setup-and-installation)  
- [Usage](#-usage)  
- [File Structure](#-file-structure)  
- [Screenshots](#-screenshots)  

---

## ✨ Features  
- **Intelligent Crop Recommendation:** Utilizes a trained machine learning model to predict the optimal crop.  
- **User-Friendly Interface:** A simple web form for users to input environmental and soil parameters.  
- **Comprehensive Inputs:** Takes into account seven key factors for prediction:  
  - Nitrogen (N) content in the soil  
  - Phosphorus (P) content in the soil  
  - Potassium (K) content in the soil  
  - Temperature (°C)  
  - Relative Humidity (%)  
  - Soil pH  
  - Rainfall (mm)  
- **Visual Feedback:** Displays the name and an image of the recommended crop.  

---

## ⚙️ How It Works  
The application operates through a straightforward workflow:  

1. **User Input:** The user enters the soil and environmental data into a form on the web interface.  
2. **Data Processing:** The Flask backend receives the form data.  
3. **Data Scaling:** The input features are scaled using pre-fitted MinMaxScaler and StandardScaler to match the format used for training the model.  
4. **Prediction:** The pre-processed data is fed into the trained machine learning model (`model.pkl`) which predicts the most suitable crop.  
5. **Display Result:** The application displays the name and an image of the predicted crop on the webpage.  

---

## 💻 Technologies Used  
- **Backend:** Flask  
- **Machine Learning:** Scikit-learn  
- **Data Handling:** NumPy, Pandas  
- **Frontend:** HTML (Rendered via Flask Templates)  

---

## 🚀 Setup and Installation  

Follow these steps to set up the project locally:  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/Crop_Recommendation.git
cd Crop_Recommendation


### 2. Create a Virtual Environment (Recommended)  
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate


### 3. Install Dependencies  
Install all required packages using:  
```bash
pip install -r requirements.txt


### 4.Ensures Model Files are present

Make sure the following pre-trained model and scaler files are in the root directory of the project:
model.pkl
minmaxscaler.pkl
standscaler.pkl

### 5. Run the application
```bash
python.py


## 📖 Usage  

1. Launch the application.  
2. You will see a **Welcome Page** – click the link to go to the form.  
3. Enter values for all seven environmental and soil input fields:  
   - Nitrogen (N)  
   - Phosphorus (P)  
   - Potassium (K)  
   - Temperature (°C)  
   - Relative Humidity (%)  
   - Soil pH  
   - Rainfall (mm)  
4. Click **Predict**.  
5. The result will display the **recommended crop** along with its **image**.  


## 📁 File Structure  

Crop_Recommendation/
│
├── app.py # Main Flask application file
├── model.pkl # Trained machine learning model
├── minmaxscaler.pkl # Saved MinMaxScaler object
├── standscaler.pkl # Saved StandardScaler object
├── requirements.txt # Project dependencies
│
├── templates/
│ ├── index.html # Main page with the form and results
│ └── welcome.html # Welcome page
│
├── static/
│ └── (images of crops like rice.jpg, maize.webp, etc.)
│
└── README.md


---

## 📸 Screenshots  

### 🌱 Welcome Page  
![Welcome Page](static/screenshots/welcome.png)  

### 🌾 Prediction Form & Result  
![Prediction Result](static/screenshots/result.png)  
