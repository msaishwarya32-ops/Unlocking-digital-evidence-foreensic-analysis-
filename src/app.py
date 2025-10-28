from flask import Flask, render_template_string, request, jsonify
import re

app = Flask(__name__)

# Dictionary of keywords and responses (same as before)
responses = {
    "digital forensics": "Digital forensics involves investigating digital devices to recover evidence for legal or security purposes.",
    "tools": "Common tools include Autopsy (disk imaging), Volatility (memory analysis), Wireshark (network traffic), and EnCase (comprehensive investigations).",
    "evidence collection": "Steps: 1) Secure the scene. 2) Document details. 3) Create forensic images with tools like dd or FTK Imager. 4) Maintain chain of custody.",
    "chain of custody": "It's a documented record of evidence handling from collection to court, ensuring integrity and admissibility.",
    "file carving": "Recover deleted files by searching for headers/footers in raw data. Tools like Scalpel or Foremost help.",
    "forensic image": "An exact bit-for-bit copy of a storage device, preserving original data without changes.",
    "memory forensics": "Analyzes RAM dumps for processes, passwords, or malware. Volatility is a key tool.",
    "encrypted data": "Use cracking tools like John the Ripper or Hashcat, or obtain legal decryption keys.",
    "challenges": "Include anti-forensics (e.g., data wiping), large volumes, cloud data, and court admissibility.",
    "goodbye": "Thanks for chatting! Remember, digital forensics requires expertise and legal compliance."
}

def get_response(user_input):
    user_input = user_input.lower()
    for key, response in responses.items():
        if re.search(r'\b' + re.escape(key) + r'\b', user_input):
            return response
    return "I'm sorry, I don't have information on that. Try asking about tools, evidence, or chain of custody."

# HTML template for the web page
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Forensics Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 20px; }
        .chat-container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        .chat-box { height: 300px; overflow-y: auto; border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; background: #fafafa; }
        input[type="text"] { width: 80%; padding: 10px; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
        button:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div class="chat-container">
        <h1>Digital Forensics Chatbot</h1>
        <div id="chat-box" class="chat-box"></div>
        <input type="text" id="user-input" placeholder="Ask about digital forensics...">
        <button onclick="sendMessage()">Send</button>
    </div>
    <script>
        function sendMessage() {
            const input = document.getElementById('user-input');
            const chatBox = document.getElementById('chat-box');
            const message = input.value.trim();
            if (message) {
                chatBox.innerHTML += '<p><strong>You:</strong> ' + message + '</p>';
                fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: message })
                })
                .then(response => response.json())
                .then(data => {
                    chatBox.innerHTML += '<p><strong>Bot:</strong> ' + data.response + '</p>';
                    chatBox.scrollTop = chatBox.scrollHeight;
                });
                input.value = '';
            }
        }
        document.getElementById('user-input').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') sendMessage();
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    response = get_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
