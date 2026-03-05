# END-TO-END-DATA-SCIENCE-PROJECT

# DEEP-LEARNING-PROJECT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MAHANK YESAMBARE

*INTERN ID*: CTIS6742

*DOMAIN*: DATA SCIENCE

*MENTOR*: NEELA SANTOSH

# DISCRIPTION,

**End-to-End Data Science Project: Student Score Prediction System**

This project focuses on developing a simple yet complete end-to-end data science solution that predicts a student’s exam score based on the number of hours they study. The main objective of this project is to demonstrate the entire machine learning pipeline, starting from data collection and preprocessing to model training and deployment using a web API. The project is designed to show how machine learning models can be integrated into real-world applications.

The first step in this project was **data collection**. A dataset was created in CSV format containing two columns: *Hours* and *Score*. The “Hours” column represents the number of hours a student studies, while the “Score” column represents the marks obtained by the student in an exam. The dataset was stored in a file named **student_scores.csv** inside a data folder. This dataset helps the machine learning model understand the relationship between study hours and exam performance.

After collecting the data, the next step was **data preprocessing and loading**. The dataset was loaded into the Python environment using the **Pandas library**, which is widely used for data manipulation and analysis in data science. Pandas makes it easy to read CSV files and organize the data into structured tables called DataFrames. In this project, the “Hours” column was used as the input feature, while the “Score” column was used as the target variable that the model needs to predict.

The next stage of the project involved **machine learning model development**. For this purpose, the **Linear Regression algorithm** from the **Scikit-learn library** was used. Linear Regression is one of the simplest and most commonly used algorithms for predicting numerical values. It works by identifying a linear relationship between the input variable and the output variable. In this case, the model learns how exam scores change depending on the number of hours studied.

Once the model was trained successfully, it was necessary to **save the trained model** so that it could be reused later without retraining it every time. To achieve this, the **Pickle library** in Python was used to serialize the trained model and store it as a file named **model.pkl** inside a model folder. This file contains the learned parameters of the machine learning model and allows it to be loaded instantly whenever predictions are required.

After building and saving the model, the next step was **model deployment**. Deployment allows the machine learning model to be used in real-world applications through a web interface or API. For this purpose, the **Flask framework** was used. Flask is a lightweight Python web framework that allows developers to build APIs and web applications easily. In this project, Flask was used to create a REST API with two endpoints. The first endpoint ("/") confirms that the API is running successfully, while the second endpoint ("/predict") accepts input data in JSON format and returns the predicted exam score.

The API takes the number of study hours as input and sends it to the trained machine learning model. The model then processes the input and returns the predicted exam score. This result is sent back to the user in JSON format. The API can be tested using tools such as Thunder Client or Postman, which allow developers to send HTTP requests and receive responses.

The development environment used for this project was **Visual Studio Code (VS Code)**, which provided an integrated terminal, code editor, and extension support. A **Python virtual environment (venv)** was also created to manage project dependencies and ensure that the required libraries such as Pandas, Scikit-learn, Flask, and NumPy were installed separately from the global Python environment.

Overall, this project successfully demonstrates a complete **end-to-end data science workflow**. It includes dataset creation, data processing, machine learning model training, model saving, API development, and prediction testing. Even though the project uses a simple dataset and algorithm, it clearly illustrates how machine learning models can be built and deployed in real-world applications. This type of workflow is commonly used in industry for building intelligent systems that make predictions based on data.
<img width="1916" height="1018" alt="Image" src="https://github.com/user-attachments/assets/90656665-2554-4e66-b395-f09ce1a919a9" />
<img width="1242" height="531" alt="Image" src="https://github.com/user-attachments/assets/64dd2fac-b7c7-4fbb-9cf4-c6f6736dfa20" />
