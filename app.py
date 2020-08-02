
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
#

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            rating = request.form['Marrige_rating']
            if rating =='Very Good':
                Marrige_rating =5
            elif rating == 'Good':
                Marrige_rating= 4
            elif rating == 'Average':
                Marrige_rating= 3
            elif rating == 'Poor':
                Marrige_rating= 2
            else:
                Marrige_rating = 1

            Age=float(request.form['Age'])
            Yrs_married = float(request.form['Yrs_married'])
            children = float(request.form['children'])

            religious = request.form['Religious']
            if religious == 'Strongly Religious':
                Religious = 4
            elif religious == 'Average':
                Religious = 3
            elif religious == 'Nominal':
                Religious = 2
            else:
                Religious = 1

            education = request.form['Education']
            if education == 'Grade School':
                Education =9
            elif education == 'High School':
                Education = 12
            elif education == 'Some College':
                Education = 14
            elif education == 'College Graduate':
                Education = 16
            elif education == 'Gradute School':
                Education = 17
            else:
                Education = 20

            women_occupation = request.form['Women_occupation']
            if women_occupation =='Professional with advance Degree':
                Women_occupation = 6
            elif women_occupation == 'Manager/Business':
                Women_occupation = 5
            elif women_occupation == 'Teacher/Nurse/Writer':
                Women_occupation = 4
            elif women_occupation == 'White Collar':
                Women_occupation = 3
            elif women_occupation == 'Farming/Unskilled/semiskilled':
                Women_occupation = 2
            else:
                Women_occupation =1


            Men_occupation = request.form['men_occupation']
            if Men_occupation =='Professional with advance Degree':
                men_occupation = 6
            elif Men_occupation == 'Manager/Business':
                men_occupation = 5
            elif Men_occupation == 'Teacher/Nurse/Writer':
                men_occupation = 4
            elif Men_occupation == 'White Collar':
                men_occupation = 3
            elif Men_occupation == 'Farming/Unskilled/semiskilled':
                men_occupation = 2
            else:
                men_occupation =1

            filename = 'modelForAffairPrediction_1.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[Marrige_rating,Age,Yrs_married,children,Religious,Education,Women_occupation,men_occupation]])
            print('prediction is', prediction)
            prediction=print(prediction[0])
            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction[0])
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app