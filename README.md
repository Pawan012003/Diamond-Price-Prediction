# 💎 Diamond Price Prediction

This project uses machine learning to predict diamond prices based on their physical and quality attributes. It includes data preprocessing, model training, and a Flask web app for real-time predictions.

## 📊 Features

- Predicts diamond price using regression models.
- Interactive web interface built with Flask.
- Clean modular code for preprocessing and prediction.
- Notebook for EDA and insights.
- Easily extendable for deployment.

## 📁 Project Structure


## 🛠️ Installation

```bash
git clone https://github.com/Pawan012003/Diamond-Price-Prediction.git
cd Diamond-Price-Prediction
python -m venv venv
# Activate your environment:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt


🚀 Usage- 
1- To start the Flask app: python application.py
2- Then go to http://127.0.0.1:5000/ in your browser.

📚 Dataset-
The dataset includes diamond features such as:
1- Carat (weight)
2- Cut (Fair to Ideal)
3- Color (D to J)
4- Clarity (I1 to IF)
5- Depth, Table, and Dimensions

💡 Model Info-
1- Linear Regression and Random Forest Regressor models evaluated.
2- Pipeline includes OneHotEncoding, StandardScaler, and feature selection.

🤝 Contributing-
Feel free to fork this repo and create pull requests for enhancements or bug fixes.

📝 License
This project is licensed under the MIT License.
