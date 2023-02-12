import pickle
from flask import Flask,render_template,request
app=Flask(__name__)
model=pickle.load(open('House.pkl','rb'))
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home',methods=['POST'])
def result():
      view=int(request.form.get('view'))
      sqft_living15=int(request.form.get('sqft_living15'))
      bathrooms=int(request.form.get('bathrooms'))
      sqft_above=int(request.form.get('sqft_above'))
      grade=int(request.form.get('grade'))
      sqft_living=int(request.form.get('sqft_living'))
      prediction=model.predict([[view,sqft_living15,bathrooms,sqft_above,grade,sqft_living]])
      return render_template('home.html',p=prediction)
app.run()
