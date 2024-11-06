let symptomsData = [];  // Array to hold logged symptoms
let severityData = [];  // Array to hold severity levels
//let labels = [];  // Array to hold labels for the chart
let chart;  // Variable to hold the chart instance

// Log a new symptom
// Log a new symptom and get recommendation from the ML model
function logSymptom() {
    const symptomDescription = document.getElementById("symptom-description").value;
    const severityLevel = document.getElementById("severity-level").value;

    // Validate input before sending
    if (!symptomDescription || !severityLevel) {
        alert("Please provide both symptom description and severity level.");
        return;
    }

    // AJAX call to log the symptom and get ML recommendation
    fetch('/log_symptom', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            description: symptomDescription,
            severity: severityLevel
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Check the response from the server
        // Show recommendation if available
        document.getElementById("recommendation").innerText = data.recommendation || "No recommendation available!";
        fetchSymptomHistory(); // Refresh the chart data
    })
    
    .catch(error => console.error('Error logging symptom:', error));
}


// Fetch symptom history and update chart
function fetchSymptomHistory() {
    fetch('/get_data')  // Adjust endpoint if necessary
        .then(response => response.json())
        .then(data => {
            console.log("Fetched Data:", data);  // Check structure of fetched data
            
            // Validate that the symptoms data contains description and date
            data.symptoms.forEach((entry, index) => {
                console.log("Entry:", entry);  // Log each symptom entry
                console.log("Severity:", data.severity[index]);  // Check severity
                console.log("Date:", data.dates[index]);  // Check date
            });
            
            symptomsData.length = 0;  // Clear existing data
            severityData.length = 0;
            labels.length = 0;
        
            // Process symptoms data
            data.symptoms.forEach((entry, index) => {
                if (entry && entry.description && entry.date) {
                    symptomsData.push(entry.description);
                    severityData.push(data.severity[index]);
                    labels.push(`${entry.description} (${data.dates[index]})`);
                } else {
                    console.warn("Missing description or date in entry:", entry);
                    // Optionally, log a placeholder value or skip this entry
                }
            });
            

            // Update chart if data is valid
            if (chart) {
                chart.data.labels = labels;
                chart.data.datasets[0].data = severityData;
                chart.update();
            }
        })
        .catch(error => console.error('Error fetching symptom history:', error));
}


// Fetch symptom history when the page loads
document.addEventListener('DOMContentLoaded', fetchSymptomHistory);
