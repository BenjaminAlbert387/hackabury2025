from flask import Flask, redirect, render_template, request, url_for, jsonify #< Server hosting
from services import uRLScan, text_scan
import logging


app = Flask(__name__)

@app.route("/")
def entry():return redirect(url_for('home'))
    
@app.route("/home")
def home(): return render_template('index.html')

@app.route("/urlscanner")
def urlscanner(): 
    return render_template('uRLScanner.html', status="Waiting - Ready to scan URLs")


@app.route('/quiz')
def render_quiz() : return render_template('quiz.html')

@app.route("/emailscanner")
def emailscanner(): return render_template('emailscanner.html')

@app.route('/urlscanner', methods=['POST'])
def submit(): 
    input = request.form['uRL']
    logging.info("### /urlscanner - INPUTTED URL: "+input)
    return render_template('uRLScanner.html', status=uRLScan(input))



@app.route('/scanemail', methods=['POST'])
def scanemail():
     try:
        # Check if request is JSON
        if not request.is_json:
            return jsonify({"Error": "Expected JSON body"}), 400

        data = request.get_json()
        input_text = data.get("input_text")

        
        report = text_scan(input_text)
        return jsonify({"report": report})

        #return text_scan(input_text)
     except Exception as error:
        return jsonify({"Error": f"Unexpected server error: {error}"}), 500


if __name__ == '__main__':
    app.run(debug=True)