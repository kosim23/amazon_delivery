📦 Amazon Delivery Time Predictor 🚚
This project utilizes Machine Learning to predict Amazon delivery times with high precision. By analyzing various factors such as courier performance, distance, weather conditions, and traffic density, the model provides accurate arrival estimates.

🚀 Key Features:
Model Architecture: Optimized XGBoost Regressor for high-performance regression.

Predictive Accuracy: Achieved an R2 Score of 0.7864.

Precision: Mean Absolute Error (MAE) of approximately 15.7 minutes.

Interactive Interface: User-friendly web application built with Streamlit.

📊 Exploratory Data Analysis (EDA):
A comprehensive analysis was conducted to understand the drivers of delivery efficiency:

Correlation Analysis: Studied the relationship between distance and delivery duration.

Key Drivers: Identified that Traffic Density and Courier Ratings are the most significant predictors of delivery speed.

Data Visualization: Utilized Matplotlib and Seaborn to visualize patterns in supply chain logistics.

🛠 Tech Stack:
Languages: Python

Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn

Deployment: Streamlit

⚙️ Installation & Usage:
Clone the repository:

Bash
git clone https://github.com/kosim23/amazon_delivery.git
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py

