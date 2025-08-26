# Crop_Recommender_Continue




Crop Recommendation System
A web-based application that leverages a machine learning model to recommend the most suitable crop to grow based on soil and environmental factors. This tool is designed to help farmers make informed decisions and improve their agricultural productivity.

📋 Table of Contents
Features

How It Works

Technologies Used

Setup and Installation

Usage

File Structure

Screenshots

✨ Features
Intelligent Crop Recommendation: Utilizes a trained machine learning model to predict the optimal crop.

User-Friendly Interface: A simple web form for users to input environmental and soil parameters.

Comprehensive Inputs: Takes into account seven key factors for prediction:

Nitrogen (N) content in the soil

Phosphorus (P) content in the soil

Potassium (K) content in the soil

Temperature (°C)

Relative Humidity (%)

Soil pH

Rainfall (mm)

Visual Feedback: Displays the name and an image of the recommended crop.

⚙️ How It Works
The application operates through a straightforward workflow:

User Input: The user enters the soil and environmental data into a form on the web interface.

Data Processing: The Flask backend receives the form data.

Data Scaling: The input features are scaled using pre-fitted MinMaxScaler and StandardScaler to match the format used for training the model.

Prediction: The pre-processed data is fed into the trained machine learning model (model.pkl) which predicts the most suitable crop.

Display Result: The application displays the name and an image of the predicted crop on the webpage.

💻 Technologies Used
This project is built with the following technologies:


Backend: Flask 


Machine Learning: Scikit-learn 


Data Handling: NumPy, Pandas 

Frontend: HTML (Rendered via Flask Templates)

🚀 Setup and Installation
To run this project locally, follow these steps:

Clone the Repository

Bash

git clone https://github.com/your-username/Crop_Recommendation.git
cd Crop_Recommendation
Create a Virtual Environment (Recommended)

Bash

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install Dependencies
Install all the required Python libraries from the requirements.txt file.

Bash

pip install -r requirements.txt
Ensure Model Files are Present
Make sure the following pre-trained model and scaler files are in the root directory of the project:

model.pkl

minmaxscaler.pkl

standscaler.pkl

Run the Application

Bash

python app.py
Access the Application
Open your web browser and navigate to:

http://127.0.0.1:5000
📖 Usage
Once the application is running, you will see a welcome page. Click the link to proceed to the recommendation form.

Fill in all the seven input fields with the appropriate values for your environment.

Click the "Predict" button.

The page will reload, displaying the name of the recommended crop and its image below the form.

📁 File Structure
Crop_Recommendation/
│
├── app.py              # Main Flask application file
├── model.pkl           # Trained machine learning model
├── minmaxscaler.pkl    # Saved MinMaxScaler object
├── standscaler.pkl     # Saved StandardScaler object
├── requirements.txt    # Project dependencies 
├── templates/
│   ├── index.html      # Main page with the form and results
│   └── welcome.html    # Welcome page
│
├── static/
│   └── (images of crops like rice.jpg, maize.webp, etc.)
│
└── README.md
📸 Screenshots
(Add screenshots of your application here to give users a visual overview.)

Welcome Page

Prediction Form & Result
