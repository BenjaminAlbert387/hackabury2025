from flask import * #< Server hosting
from API import uRLScan
import json

app = Flask(__name__)

@app.route("/")
def entry():return redirect(url_for('home'))
    
@app.route("/home")
def home(): return render_template('index.html')

@app.route("/urlscanner")
def urlscanner(): 
    return render_template('uRLScanner.html', status="Waiting - Ready to scan URLs")

@app.route("/emailscanner")
def emailscanner(): return render_template('emailscanner.html')

@app.route('/urlscanner', methods=['POST'])
def submit(): 
    input = request.form['uRL']
    print("### /urlscanner - INPUTTED URL: "+input)
    return render_template('uRLScanner.html', status=uRLScan(input))

@app.route('/scan', methods=['POST'])
def scanemail():
    input = request.form
    print(input)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)