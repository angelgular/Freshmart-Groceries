from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the services that ESB will communicate with
SERVICES = {
    "employee-service-1": "http://127.0.0.1:5000",  # First employee service
    "employee-service-2": "http://127.0.0.1:5001"   # Second employee service
}

@app.route('/employees', methods=['GET', 'POST'])
def employees():
    """Forward employee-related requests to the appropriate service"""
    service_url = SERVICES["employee-service-1"] + "/employees"  # Default to service 1

    if request.method == "GET":
        response = requests.get(service_url)
    elif request.method == "POST":
        response = requests.post(service_url, json=request.json)

    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    print("🚀 ESB is running on port 3000...")
    app.run(host="127.0.0.1", port=3000, debug=True)
