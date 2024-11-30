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
