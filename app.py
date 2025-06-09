from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
try:
    with open('decision_tree_classifier.pkl', 'rb') as file:
        rf = pickle.load(file)
except FileNotFoundError:
    print("Error: 'decision_tree_classifier.pkl' file not found.")
    exit(1)
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

@app.route('/', methods=['GET', 'POST'])
def predict_placement():
    if request.method == 'POST':
        try:
            # Extract form data
            mydict = request.form
            gender = int(mydict['gender'])
            spec = int(mydict['spec'])
            tech = int(mydict['tech'])
            work = int(mydict['work'])
            ssc = float(mydict['ssc'])
            hsc = float(mydict['hsc'])
            dsc = float(mydict['dsc'])
            mba = float(mydict['mba'])

            # Create input DataFrame with correct feature names and order
            input_features = pd.DataFrame([[
                gender, mba, ssc, dsc, spec, hsc, tech, work
            ]], columns=['gender', 'mba_p', 'ssc_p', 'degree_p', 'specialisation', 'hsc_p', 'degree_t', 'workex'])

            # Predict
            predicted_class = rf.predict(input_features)[0]
            predicted_prob = rf.predict_proba(input_features)[0]

            # Log for debugging
            print(f"Input: {input_features.values[0]}, Predicted: {predicted_class}, Prob: {predicted_prob}")

            # Select probability
            proba = predicted_prob[1] if predicted_class == 1 else predicted_prob[0]

            # Map prediction
            placemap = {1: 'Will be Placed', 0: 'Better Luck Next Time :('}
            predicted_class_send = placemap[predicted_class]

            # Render index.html with results
            return render_template(
                'index.html',
                predictedclasssend=predicted_class_send,
                predictedprob=round(proba * 100, 2),
                placed=(predicted_class == 1)
            )
        except ValueError as e:
            print(f"ValueError: {e}")
            return render_template('index.html', error_message="Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"Error: {e}")
            return render_template('index.html', error_message=f"An error occurred: {str(e)}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)