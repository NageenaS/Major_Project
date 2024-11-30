# Plant Disease Detection and Diagnosis

This project uses machine learning models to detect plant diseases based on images of leaves. The system is built with **Streamlit**, **TensorFlow**, and **Keras**, allowing users to upload images of plant leaves and receive information about the possible disease affecting the plant, along with treatment recommendations.

## Features

- **Image Upload and Prediction**: Users can upload images of plant leaves, and the model will predict the disease, if any.
- **Disease Information**: Once a disease is detected, the app displays detailed information about the disease, its symptoms, and potential treatments.
- **Image Search**: For further clarity, the app can display images of the disease from the web.

## Technologies Used

- **Streamlit**: For the web application interface.
- **TensorFlow & Keras**: For loading and using pre-trained models for plant disease classification.
- **BeautifulSoup**: For scraping images from the web for disease references.
- **Google Images API**: To search and display disease-related images.

## How to Run the Project

To run the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NageenaS/Major_Project.git
   cd Major_Project
   ```
2. **Install dependencies: Create a virtual environment (optional) and install the necessary dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application: To run the Streamlit application, use the following command**:
   ```bash
   streamlit run app.py
   ```
## Usage
- After launching the application, you can utilize the interface to:
## Home Page
The home page consists of two main tabs:

1. **Description**:
   Provides an overview of the application and its functionality.
2. **Plant Disease Info**:
   Allows you to upload an image of a plant leaf for disease detection.
   ![image](https://github.com/user-attachments/assets/b055325b-db95-47b7-bba9-3bdd93e25fdd)
## Steps to Use the Application:
- Upload a plant leaf image: On the home page, you’ll find an option to upload an image of a plant leaf for analysis.
  ![image](https://github.com/user-attachments/assets/d1d51239-de48-4146-8e0b-dd5c4c90d56c)
- Submit the image for disease detection: Once the image is uploaded, click the “Submit” button to initiate the detection process.

- View the results: The application will display the predicted plant disease along with the accuracy of the prediction.
  ![image](https://github.com/user-attachments/assets/658a0669-c0e1-4d53-acca-499b35c3adec)

- Interpret the results: Detailed information about the identified disease will be shown, along with suggested remedies or further steps for treatment.
  ![image](https://github.com/user-attachments/assets/095df95a-a88e-4cfc-a8c3-ff3a91b9679f)
