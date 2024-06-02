import pickle
from sklearn.tree import DecisionTreeClassifier
import numpy as np

class predict_decision_tree:
    # Attributes
    model = DecisionTreeClassifier()
    predictors_names = ['voteId', 'issueArea', 'petitionerState', 'respondentState', 'jurisdiction', 'caseOriginState', 'caseSourceState', 'certReason', 'lcDisposition']
    predictors_values = []

    def __init__(self) -> None:
        try:
            with open("models/decision_tree_model.pkl", "rb") as file:
                self.model = pickle.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("The file decision_tree_model.pkl was not found")
        except Exception as e:
            raise Exception(f"An error occurred while loading the model: {e}")

    def set_predictors(self, values: list) -> None:
        if len(values) != len(self.predictors_names):
            raise ValueError(f"Expected {len(self.predictors_names)} values, but got {len(values)}")
        self.predictors_values = values
    
    def predict_self(self) -> float:
        if not self.predictors_values:
            raise ValueError("Predictor values have not been set.")
        # Convert the predictors to the correct format for prediction (2D array)
        predictors_array = np.array(self.predictors_values).reshape(1, -1)
        return self.model.predict(predictors_array)[0]