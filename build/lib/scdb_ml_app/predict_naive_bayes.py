'''
SCDB-ML-app is a deployed app to analyze the U.S. Supreme Court Database
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
from sklearn.naive_bayes import GaussianNB
import numpy as np
from pathlib import Path
from os import getcwd
from os.path import join

class predict_naive_bayes:
    # Attributes
    model = GaussianNB()
    predictors_names = ['voteId', 'issueArea', 'petitionerState', 'respondentState', 'jurisdiction', 'caseOriginState', 'caseSourceState', 'certReason', 'lcDisposition']
    predictors_values = []
    current_directory=getcwd()

    def __init__(self) -> None:
        try:
            with open(Path(join(self.current_directory,"scdb_ml_app\\models\\decision_naive_bayes.pkl")), "rb") as file:
                self.model = pickle.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("The file decision_naive_bayes.pkl was not found")
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