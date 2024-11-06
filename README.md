# Patient-Symptom-Tracker

**Project Overview**
The Patient Symptom Tracker  is a web-based application designed to help track and manage patient symptoms. The application allows users to log symptoms along with their severity, and based on the input, a recommendation is provided using a machine learning model. The recommendation can guide users on the next steps to take, such as consulting a specialist or seeking medical attention.
**Key Features:**
•	Symptom logging with severity levels.
•	Real-time chart updates displaying symptom history.
•	Machine learning-based recommendations based on symptom and severity.
•	Data persistence using a SQL database.
•	Responsive and interactive UI for smooth user experience.
**Installation Steps**
Prerequisites
Before you start, make sure you have the following installed:
•	Python 3.x (with pip package manager)
•	Node.js and npm (for front-end package management)
Backend Setup
1.	Clone the repository to your local machine:
git clone <https://github.com/Dharsh-04/Patient-Symptom-Tracker>
cd <Patient-Symptom-Tracker>
2.	Install required Python packages:
pip install -r requirements.txt 
3.	Ensure that you have all the necessary files, such as the model (symptom_recommendation_model.pkl), encoders (symptom_encoder.pkl and severity_encoder.pkl), and the rec.xlsx file for training data.
4.	Set up the database:
o	Make sure to run the Flask application once to create the required database tables:
                     flask run
**Frontend Setup**
1.	If you haven't already, navigate to the frontend directory and install the dependencies:
cd static  
npm install
2.	You can now run the frontend separately or integrate it with the Flask backend as described in the instructions

**Usage Instructions**
1.	Run the Backend:
flask run
This starts the Flask server locally, typically on http://127.0.0.1:5000.
2.	Access the Web Application: Open your browser and go to http://127.0.0.1:5000/ to access the Patient Symptom Tracker interface.
3.	Log Symptoms:
o	Enter symptom details (e.g., 'Fever', 'Cough') and severity (e.g., '5').
o	Click "Log Symptom" to send the data to the backend. The chart will update in real-time, and a recommendation will be displayed.
4.	View Symptom History: The symptom history will be shown in the chart, updating each time a new symptom is logged.



**Technologies Used**
Backend
•	Flask: Lightweight Python web framework for building the backend API.
•	Flask-SQLAlchemy: ORM for database interactions.
•	Scikit-learn: Used for building and using the machine learning model to generate recommendations.
•	Pandas: Used for data manipulation and encoding categorical features.
•	Joblib: Used to serialize the machine learning model and encoders.
•	SQLite: For storing symptom data.
Frontend
•	HTML5, CSS3, and JavaScript: Basic web technologies to build a responsive and interactive user interface.
•	Chart.js: JavaScript library for rendering interactive charts.
•	Fetch API: For sending asynchronous HTTP requests to the backend.
•	Bootstrap: Frontend framework for styling and responsive design.

**Future Improvements** 
While the current version of the project offers basic functionality, here are some potential improvements:
1.	User Authentication:
o	Allow users to create accounts, log in, and access their personal symptom history.
2.	Data Visualization Enhancements:
o	Implement advanced visualizations like trend analysis or heat maps to track symptoms over time.
3.	Advanced Machine Learning Models:
o	Use more sophisticated models (e.g., Random Forest, SVM) or neural networks to provide more accurate recommendations.
o	Train the model with a larger dataset for better performance and reliability.
4.	Real-time Notifications:
o	Implement email or SMS notifications to alert users about critical symptoms based on the severity they log.
5.	Mobile App Version:
o	Develop a mobile app for both iOS and Android to allow patients to track symptoms on-the-go.
6.	Integrating with Healthcare APIs:
o	Integrate the application with healthcare APIs to retrieve additional data (e.g., medical conditions, drugs, treatments).

