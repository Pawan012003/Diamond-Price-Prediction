from flask import Flask, request, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Add version to force CSS reload
app.config['VERSION'] = '1.0.1'

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html', version=app.config['VERSION'])
    else:
        # Collect form inputs
        form = request.form
        required_fields = ['carat', 'depth', 'table', 'x', 'y', 'z', 'cut', 'color', 'clarity']
        
        # Check for missing input
        if not all(form.get(field) for field in required_fields):
            return render_template('form.html', final_result="Please enter all the data.", version=app.config['VERSION'])

        try:
            # Convert float fields safely
            data = CustomData(
                carat=float(form.get('carat')),
                depth=float(form.get('depth')),
                table=float(form.get('table')),
                x=float(form.get('x')),
                y=float(form.get('y')),
                z=float(form.get('z')),
                cut=form.get('cut'),
                color=form.get('color'),
                clarity=form.get('clarity')
            )

            final_new_data = data.get_data_as_dataframe()
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_new_data)

            results = round(pred[0], 2)
            return render_template('form.html', final_result=f"Predicted Diamond Price: ${results}", version=app.config['VERSION'])

        except ValueError:
            return render_template('form.html', final_result="Please enter valid numeric values.", version=app.config['VERSION'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)