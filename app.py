from flask import Flask, request, jsonify

app = Flask(__name__)

# Route 1: Return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200590360"})

# Route 2: Webhook for Dialogflow
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    # Get the intent name
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName", "")

    # Response based on intent
    if intent_name == "Motivational Quote":
        response_text = "Believe in yourself! Every day is a new opportunity to grow."
    else:
        response_text = "I'm not sure how to respond to that."

    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
    app.run(port=5000, debug=True)