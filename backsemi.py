from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app/data', methods=['GET'])
def get_data():
    return jsonify({
        'message' : 'Hello from the backend!',
        'status': 'success'
    })
if __name__=='__main__':
    app.run(debug=False)