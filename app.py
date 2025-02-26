from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "message": "Hello, World!",
        "status": "success"
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy"
    })

if __name__ == '__main__':
    # Run the app on 0.0.0.0 to make it accessible outside the container
    app.run(host='0.0.0.0', port=5001, debug=True)