import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib  # Import joblib for saving the model

# Load the dataset
data = pd.read_excel('G:\\DHARSHNI_WORKS\\Patient_symptom_tracker\\data\\rec.xlsx')  # Make sure the file extension is correct

# Initialize LabelEncoders
symptom_encoder = LabelEncoder()
severity_encoder = LabelEncoder()

# Encode the categorical features to numerical values
data['Symptom'] = symptom_encoder.fit_transform(data['Symptom'])
data['Severity Level'] = severity_encoder.fit_transform(data['Severity Level'])  # Convert severity to numerical

# Define features and target
X = data[['Symptom', 'Severity Level']]  # Features
y = data['Recommendation']  # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple model (Logistic Regression as an example)
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'G:\\DHARSHNI_WORKS\\Patient_symptom_tracker\\data\\symptom_recommendation_model.pkl')

# Save the encoders for later use
joblib.dump(symptom_encoder, 'G:\\DHARSHNI_WORKS\\Patient_symptom_tracker\\data\\symptom_encoder.pkl')
joblib.dump(severity_encoder, 'G:\\DHARSHNI_WORKS\\Patient_symptom_tracker\\data\\severity_encoder.pkl')

# Function to get a recommendation based on symptom and severity level
def get_recommendation(symptom, severity):
    severity_num = severity_encoder.transform([severity])  # Ensure severity is in the same format
    symptom_num = symptom_encoder.transform([symptom])  # Convert symptom to numerical
    input_data = pd.DataFrame({'Symptom': symptom_num, 'Severity Level': severity_num})
    prediction = model.predict(input_data)
    return prediction[0]

# Example usage
user_symptom = 'Fever'  # Change this to test different symptoms
user_severity = '4'  # Ensure this matches the encoding in your dataset
recommendation = get_recommendation(user_symptom, user_severity)
print(f"Recommendation for {user_symptom} (Severity {user_severity}): {recommendation}")
