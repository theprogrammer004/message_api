from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variable to store the current message
current_message = "Hello"

# Endpoint to fetch the current message
@app.route('/message', methods=['GET'])
def get_message():
    global current_message
    return current_message

# Endpoint to update the message
@app.route('/message', methods=['POST'])
def update_message():
    global current_message
    data = request.get_json()
    
    if 'message' in data:
        current_message = data['message']
        return jsonify({"status": "success", "message": "Message updated!"}), 200
    else:
        return jsonify({"status": "error", "message": "No message provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
