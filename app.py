from flask import Flask, jsonify
from waitress import serve

app = Flask(__name__)

@app.route('/')

@app.route('/app/data', methods=['GET'])
def get_data():
    return jsonify({
        'message' : 'Hello from the backend!',
        'status': 'success'
    })
if __name__=='__main__':
    serve(app, host='0.0.0.0',port=5000)