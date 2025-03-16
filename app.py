from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("fish_market_model.pkl")

# Load the LabelEncoder
encoder = joblib.load("species_encoder.pkl")

# List of available fish species
SPECIES_LIST = encoder.classes_.tolist()  # Get the original species names

@app.route('/')
def home():
    """Render the main HTML page."""
    return render_template("index.html")  

@app.route('/species', methods=['GET'])
def get_species():
    """Provide a list of available fish species."""
    return jsonify({"species": SPECIES_LIST})

@app.route('/predict', methods=['POST'])
def predict():
    """Predict the fish weight based on input features."""
    try:
        # Get JSON data from request
        data = request.get_json()
        print("Received Data:", data)  # Debugging

        # Validate input data
        required_fields = ["Species", "Length1", "Length2", "Length3", "Height", "Width"]
        for field in required_fields:
            if field not in data or data[field] == "":
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Convert data into DataFrame
        df = pd.DataFrame([data])
        print("DataFrame:", df)  # Debugging

        # Ensure species is in the dataset
        if df["Species"][0] not in SPECIES_LIST:
            return jsonify({"error": "Invalid species selected!"}), 400

        # Encode the Species column using the saved LabelEncoder
        df["Species"] = encoder.transform(df["Species"])
        print("Encoded DataFrame:", df)  # Debugging

        # Make prediction
        prediction = model.predict(df)
        print("Prediction:", prediction)  # Debugging

        # Return the prediction
        return jsonify({"prediction": float(prediction[0])})  

    except Exception as e:
        print("Error:", str(e))  # Debugging: Log any errors
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)