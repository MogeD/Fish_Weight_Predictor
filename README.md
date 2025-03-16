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
