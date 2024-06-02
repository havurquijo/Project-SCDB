'''
SCDB-ML-app is a deployed app to analize the U.S. Supreme Court Database
Copyright (C) 2024  HERMES A. V. URQUIJO

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
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