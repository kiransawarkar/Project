from flask import Flask,render_template,jsonify,request
from matplotlib.legend_handler import HandlerLineCollection
from utlis import medical_Insurance

app=Flask(__name__)

@app.route('/')

def hello_flask():
    return 'hello'
@app.route('/medical')
def medical_insurance():
    age=36
    sex='male'
    bmi=27.9
    children= 4
    smoker='no'
    region='northeast'
    med_ins=medical_Insurance(age, sex, bmi, children, smoker,region)
    charges=med_ins.get_predicted_price()
    return jsonify({"result":f"Predicted price is {charges}"})
@app.route('/m')
def medical_I():
    data=request.form
    age=int(data['age'])
    sex=data['sex']
    bmi=int(data['bmi'])
    children= int(data['children'])
    smoker=data['smoker']
    region=data['region']
    med_ins=medical_Insurance(age, sex, bmi, children, smoker,region)
    charges=med_ins.get_predicted_price()
    return jsonify({"result":f"Predicted price is {charges}"})
app.run(host='0.0.0.0',port=5000,debug=True)









app.run()



