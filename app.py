from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200590360"})

# Webhook route for Dialogflow fulfillment
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    response_text = "This is a response from your Flask webhook."

    res = {
        "fulfillmentText": response_text
    }

    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
