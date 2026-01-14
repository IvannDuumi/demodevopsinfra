from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status')
def status():
    # Simulamos una respuesta real de una API
    return jsonify({
        "status": "online",
        "service": "Backend-Fintexa",
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)