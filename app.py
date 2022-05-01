from flask import Flask, redirect, render_template, request, url_for

app=Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        height = request.form.get('height')
        weight = request.form.get('weight')
        result_helper = (int(height)/100)**2
        result = round(int(weight)/result_helper,2)
        if result<16:
            final_concl = 'Starvation'
        elif result>=16 and result<18.5:
            final_concl = 'Emaciation'
        elif result>=18.5 and result<25:
            final_concl = 'Normal'
        elif result>=25 and result<30:
            final_concl = 'Overweight'
        else:
            final_concl = 'Obesity'
        return render_template('result.html',height=height, weight=weight,result=result, final_concl=final_concl)
    return render_template('index.html')
@app.route('/result')
def sended_form():
    return render_template('result.html')
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html')
if __name__=="__main__":
    app.run(debug=True)