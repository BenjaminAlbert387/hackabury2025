from flask import * #< Server hosting
from API import uRLScan

app = Flask(__name__)

@app.route("/")
def entry():return redirect(url_for('home'))
    
@app.route("/home")
def home(): return render_template('index.html')

@app.route("/urlscanner")
def urlscanner(): 
    return render_template('uRLScanner.html', status="Waiting - Ready to scan URLs")

@app.route('/urlscanner', methods=['POST'])
def submit(): 
    input = request.form['uRL']
    print("### /urlscanner - INPUTTED URL: "+input)
    return render_template('uRLScanner.html', status=uRLScan(input))

@app.route('/emailscanner', methods=['POST'])
def scanemail():
    input = request.json()
    print(input)

if __name__ == '__main__':
    app.run(debug=True)