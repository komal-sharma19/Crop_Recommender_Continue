from flask import Flask, request, render_template
import numpy as np
import pickle

# --- Load the pre-trained models ---
try:
    model = pickle.load(open('model.pkl', 'rb'))
    sc = pickle.load(open('standscaler.pkl', 'rb'))
    mx = pickle.load(open('minmaxscaler.pkl', 'rb'))
except FileNotFoundError:
    print("Error: Make sure model.pkl, standscaler.pkl, and minmaxscaler.pkl are in the same directory.")
    exit()

# --- Initialize Flask App ---
app = Flask(__name__)

# --- Crop and Image Dictionaries (Same as before) ---
CROP_NAMES = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut",
    6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon",
    11: "Grapes", 12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil",
    16: "Blackgram", 17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas",
    20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

CROP_IMAGES = {
    'Rice': 'static/rice.jpg',
    'Maize': 'static/maize.webp',
    'Jute': 'static/jute.webp',
    'Cotton': 'static/cotton.jpeg',
    'Coconut': 'static/coconut.jpeg',
    'Papaya': 'static/papaya.webp',
    'Orange': 'static/orange.webp',
    'Apple': 'static/apple.webp',
    'Muskmelon': 'static/muskmelon.webp',
    'Watermelon': 'static/watermelon.webp',
    'Grapes': 'static/grapes.webp',
    'Mango': 'static/mango.webp',
    'Banana': 'static/banana.webp',
    'Pomegranate': 'static/pomegranate.webp',
    'Lentil': 'static/lentil.webp',
    'Blackgram': 'static/blackgram.webp',
    'Mungbean': 'static/mungbean.webp',
    'Mothbeans': 'static/mothbean.webp',
    'Pigeonpeas': 'static/pigeonbean.webp',
    'Kidneybeans': 'static/kidneybean.webp',
    'Chickpea': 'static/chickpea.webp',
    'Coffee': 'static/coffee.webp'
}

# Route for the welcome page
@app.route('/')
def welcome():
    """Renders the welcome page."""
    return render_template("welcome.html")

# Route for the main form page
@app.route('/recommend')
def index():
    """Renders the main form page without any prediction result."""
    return render_template("index.html")

# Route to handle the form submission and prediction
@app.route("/predict", methods=['POST'])
def predict():
    """Handles form submission, makes prediction, and renders the page with results."""
    try:
        # Get data from form
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosporus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])

        # Create feature list and preprocess data
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        mx_features = mx.transform(single_pred)
        sc_mx_features = sc.transform(mx_features)
        
        # Make prediction
        prediction = model.predict(sc_mx_features)
        prediction_value = prediction[0]

        # Prepare results for the template
        if prediction_value in CROP_NAMES:
            crop_name = CROP_NAMES[prediction_value]
            result = f"{crop_name} "
            image_url = CROP_IMAGES.get(crop_name)
        else:
            result = "Sorry, we could not determine the best crop with the provided data."
            crop_name = None
            image_url = None

        # Render the form page again, but this time with prediction results
        return render_template('index.html', result=result, crop_name=crop_name, image_url=image_url)

    except Exception as e:
        error_message = f"An error occurred: {e}"
        return render_template('index.html', result=error_message)


if __name__ == "__main__":
    app.run(debug=True)