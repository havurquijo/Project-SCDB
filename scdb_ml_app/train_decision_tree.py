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
from pickle import dump
from pandas import  DataFrame, read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from pathlib import Path
from os import getcwd
from os.path import join

class train_decision_tree:
    #atributtes
    previsors=[]
    toPredict=[]
    base=DataFrame()
    current_directory=getcwd()

    def __init__(self) -> None:
            address = Path(join(self.current_directory,"scdb_ml_app\\models\\preprocessed_decision_tree.csv"))
            self.base = read_csv(address,sep=';')
            self.previsors = self.base.iloc[:,0:9].values
            self.toPredict = self.base.iloc[:,9].values    

    def train(self, max_depth=6,test_size=0.3,random_state=1)->float:
        #data split
        X_train, X_test, y_train, y_test = train_test_split(self.previsors,self.toPredict,test_size=test_size,random_state=random_state)
        #Object DecisionTreeClassifier created
        tree_model_tree = DecisionTreeClassifier(max_depth=max_depth)
        #training the models
        tree_model_tree.fit(X_train,y_train)

        #Results tree model
        y_predicted_tree = tree_model_tree.predict(X_test)
        confusion_tree = confusion_matrix(y_test,y_predicted_tree)
        print("Confusion matrix in tree model is: ")
        print(confusion_tree)
        accuracy = accuracy_score(y_test,y_predicted_tree)
        print("")
        print("Accuracy in tree model was:")
        print(f"{accuracy*100:.1f}%")
        #saving model
        self.save_model(tree_model_tree,Path(join(self.current_directory,"scdb_ml_app\\models\\decision_tree_model.pkl")))
        return accuracy

    def save_model(self,model,model_pkl_file)->None:
        # save the classification model as a pickle file

        with open(model_pkl_file, 'wb') as file:  
            dump(model, file)