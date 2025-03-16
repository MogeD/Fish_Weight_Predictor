# Fish_Weight_Predictor

This project predicts the weight of fish based on their species and physical measurements using a machine learning model. The model is deployed locally using Flask and can be accessed via a web interface.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Model Training](#model-training)
7. [API Endpoints](#api-endpoints)
8. [Screenshots](#screenshots)
9. [Contributing](#contributing)
10. [License](#license)

---

## Project Overview

The Fish Market Weight Prediction project uses a dataset of fish measurements to train a machine learning model. The model predicts the weight of a fish based on its species and physical dimensions (Length1, Length2, Length3, Height, Width). 

---

## Features

- **Machine Learning Model**: A Linear Regression model trained on the Fish Market dataset.
- **Flask API**: A RESTful API for making predictions.
- **Web Interface**: A simple HTML form for inputting fish measurements and viewing predictions.
- **Dynamic Species Dropdown**: The species dropdown is populated dynamically from the Flask API.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/MogeD/fish-market-prediction.git
   cd fish-market-prediction
   
2. Install the required Python packages

3. Download the dataset:
- The dataset is available on Kaggle.
- Place the Fish.csv file in the project root directory.

4. Train the model (optional):
- Run the train_model.py script to train the model:
- This will generate the fish_market_model.pkl and species_encoder.pkl files.

### Usage
1. Start the Flask app: python app.py
2: Open your browser and navigate to http://localhost:5000.
3. Fill in the form with the fish measurements and click Predict.
4. The predicted weight will be displayed below the form.

### File Structure
fish-market-prediction/
   ├── app.py                  # Flask API and web interface
   
   ├── train_model.py          # Script to train the model
├── Fish.csv                # Dataset
├── fish_market_model.pkl   # Trained model
├── species_encoder.pkl     # LabelEncoder for species
├── templates/              # HTML templates
│   └── index.html
├── static/                 # Static files (CSS, JS)
│   └── style.css
├── screenshot/             # Screenshot files (PNG)
│   └── home.png
    └── prediction.png
└── README.md               # Project documentation

### Model Training
The model is trained using a Linear Regression algorithm. The training script (train_model.py) performs the following steps:
1. Loads the dataset.
2. Encodes the Species column using LabelEncoder.
3. Splits the data into training and testing sets.
4. Trains the model and evaluates its performance.
5. Saves the trained model and encoder to files (fish_market_model.pkl and species_encoder.pkl).

### API Endpoints
1. Home Page
URL: /

Method: GET

Description: Renders the main HTML page.

2. Get Species List
URL: /species

Method: GET

Description: Returns a list of available fish species.

3. Predict Weight
URL: /predict

Method: POST

Description: Predicts the weight of a fish based on input features.

Request Body: 
{
    "Species": "Bream",
    "Length1": 23.2,
    "Length2": 25.4,
    "Length3": 30.0,
    "Height": 11.52,
    "Width": 4.02
}

Response:
{
    "prediction": 290.5
}

### Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

### **Screenshots**
- `screenshots/home.png`: A screenshot of the home page.
- `screenshots/prediction.png`: A screenshot of the prediction result.
  
### Acknowledgments
Dataset: Fish Market Dataset on Kaggle
