# California Housing Price Prediction


![Alt Text](interface.jpg)
## Overview

This project aims to predict the median house value in California using a machine learning model. The dataset used is the California Housing dataset, which contains various features such as median income, housing median age, and average rooms per dwelling. The model is built using Python and Flask for serving the predictions.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

- **App.py**: Flask application for serving the model and making predictions.
- **requirements.txt**: List of dependencies required to run the project.
- **Procfile**: Configuration file for deploying the app on platforms like Heroku.
- **Summary.md**: Summary of the project.
- **StepByStep.ipynb**: Jupyter notebook with step-by-step implementation of the project.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/california-housing-price-prediction.git
    cd california-housing-price-prediction
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Train the model and save it as `gradient_boosting_model.pkl` (this step is already done in the provided notebook).

2. Run the Flask application:
    ```bash
    python App.py
    ```

3. The API will be available at `http://127.0.0.1:5000/`. Use the `/predict` endpoint to get predictions.

## Deployment

To deploy the application on Heroku, follow these steps:

1. Install the Heroku CLI and log in:
    ```bash
    heroku login
    ```

2. Create a new Heroku app:
    ```bash
    heroku create your-app-name
    ```

3. Push the code to Heroku:
    ```bash
    git push heroku main
    ```

4. Open the deployed app:
    ```bash
    heroku open
    ```

## API Endpoints

- **GET /**: Welcome message.
- **POST /predict**: Make a prediction. Send a JSON payload with the key `features` containing an array of input features.

## Example Request

```json
{
    "features": [8.3252, 41.0, 6.984127, 1.023810, 322.0, 2.555556, 37.88, -122.23]
}
```

## Example Response

```json
{
    "prediction": [2.345]
}
```


## Model

The model used for this project is a Random Forest Regressor. The model was trained on the California Housing dataset and achieved an R² score of 0.80 on the test set. The model was evaluated using cross-validation and hyperparameter tuning.

## Results

The model was able to predict the median house value with a mean absolute error of $50,000. The model was also able to capture the relationship between the median income and the median house value. The model was deployed using Flask and can be accessed at [https://california-housing-price-prediction.herokuapp.com/](https://california-housing-price-prediction.herokuapp.com/).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
