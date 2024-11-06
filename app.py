from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from datetime import datetime
app = Flask(__name__)

# Database URI (adjust path if necessary)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///symptoms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To avoid warnings

db = SQLAlchemy(app)


# Your models go here (e.g., Symptom class)

# Database model for storing symptoms
class Symptom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    severity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)  # Add the date column with default


# Load dataset and train model
data = pd.read_excel('G:\\DHARSHNI_WORKS\\Patient_symptom_tracker\\data\\rec.xlsx')

# Encode the 'Symptom' and 'Severity Level'
data['Severity Level'] = LabelEncoder().fit_transform(data['Severity Level'])  # Encode severity
symptom_encoder = LabelEncoder()
data['Symptom'] = symptom_encoder.fit_transform(data['Symptom'])  # Encode symptom

X = data[['Symptom', 'Severity Level']]  # Features
y = data['Recommendation']  # Target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Function to get recommendation based on symptom and severity
def get_recommendation(symptom, severity):
    severity_num = [int(severity)]  # Ensure severity is an integer
    symptom_encoded = symptom_encoder.transform([symptom])[0]  # Encode symptom
    input_data = pd.DataFrame({'Symptom': [symptom_encoded], 'Severity Level': severity_num})
    prediction = model.predict(input_data)
    return prediction[0]

# Create the database and tables (run this once to set up)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('Patient_UI.html')

@app.route('/log_symptom', methods=['POST'])
def log_symptom():
    data = request.json
    description = data.get('description')
    severity = data.get('severity')

    # Generate recommendation
    recommendation = get_recommendation(description, severity)  # Use the correct function

    # Save the symptom in the database
    new_symptom = Symptom(description=description, severity=severity)
    db.session.add(new_symptom)
    db.session.commit()

    # Return the response with recommendation
    return jsonify({
        'recommendation': recommendation,
        'status': 'success'
    })

@app.route('/get_data', methods=['GET'])
def get_data():
    symptoms = Symptom.query.all()
    symptoms_data = {
        "symptoms": [f"{symptom.description} [{symptom.date.strftime('%Y-%m-%d')}]" for symptom in symptoms],  # Using 'date'
        "severity": [symptom.severity for symptom in symptoms],
        "dates": [symptom.date.strftime('%Y-%m-%d') for symptom in symptoms]  # Using 'date'
    }
    return jsonify(symptoms_data)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created before running the app
    app.run(debug=True)
