# Campus Placement Predictor

A Flask-based web application that predicts whether a student will be placed in campus recruitment based on academic and professional factors. The project uses a pre-trained Decision Tree Classifier model and provides a user-friendly interface with a modern design.

## Project Overview

The goal of this project is to predict campus placement outcomes using a machine learning model trained on the [Kaggle Campus Placement Dataset](https://www.kaggle.com/benroshan/factors-affecting-campus-placement). The model considers factors such as gender, academic percentages (SSC, HSC, Degree, MBA), specialization, technical degree, and work experience. The web application allows users to input their details and receive a prediction ("Will be Placed" or "Better Luck Next Time :("), along with a placement probability and, for non-placed predictions, 20 tips to improve interview performance.

### Features
- **Input Form**: Collects user data for gender, specialization, technical degree, work experience, and academic percentages.
- **Prediction Output**: Displays placement prediction and probability.
- **Tips for Improvement**: Provides 20 actionable tips for students predicted as "Not Placed."
- **Modern UI**: Responsive design with Bootstrap 4.3.1, gradient backgrounds, larger dropdowns, and animations.
- **Footer**: Credits the creator, Sadik Al Jarif, with © 2025.
- **Error Handling**: Validates user inputs and displays error messages for invalid entries.

## Technologies Used
- **Backend**: Flask, Python
- **Frontend**: HTML, CSS (Bootstrap 4.3.1, custom `style.css`), JavaScript
- **Machine Learning**: Scikit-learn (Decision Tree Classifier)
- **Libraries**: Pandas, NumPy
- **Model File**: `decision_tree_classifier.pkl`

## Project Structure
```
campus-placement-predictor/
├── static/
│   └── style.css           # Custom CSS for styling
├── templates/
│   └── index.html         # Combined form and results page
├── app.py                 # Flask application
├── decision_tree_classifier.pkl  # Pre-trained model
└── README.md              # Project documentation

```


## Setup Instructions

### Prerequisites
- Python 3.8+
- Virtual environment tool (e.g., `venv`)
- Git (optional, for cloning)

### Installation
1. **Clone the Repository** (or download the project files):
   ```
   git clone <repository-url>
   cd campus-placement-predictor
   ```
2. **Create a Virtual Environment:**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**

```
pip install flask pandas scikit-learn
```
## Verify Files:

- Ensure decision_tree_classifier.pkl is in the project root.

- Confirm index.html is in templates/ and style.css is in static/.

4. **Run the Application:**
```
python app.py
```

## Usage
- Access the Web App:
- Open http://127.0.0.1:5000 in a web browser.

- The homepage displays an introduction to campus recruitment and a form.

## Fill the Form:
- Gender: Select Male (1) or Female (0).

- Specialisation: Choose Marketing and Human Resources (1) or Marketing and Finance (0).

- Technical Degree: Select Commerce and Management (0), Others (1), or Science and Technology (2).

- Work Experience: Choose Yes (1) or No (0).

- Percentages: Enter SSC, HSC, Degree, and MBA percentages (0–100, e.g., 67.00).

- Click Predict Now.

## View Results:
- Placed: Shows "Will be Placed" with the placement probability and a congratulatory message.

- Not Placed: Shows "Better Luck Next Time :(" with 20 tips to improve interview skills.

- Click Go Back to reset the form.

