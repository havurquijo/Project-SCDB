from pickle import dump
from pandas import  DataFrame, read_csv
from os.path import exists
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier,plot_tree

class train_decision_tree:
    #atributtes
    previsors=[]
    toPredict=[]
    base=DataFrame()

    def __init__(self) -> None:
            address = "models/preprocessed_decision_tree.csv"
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
        self.save_model(tree_model_tree,"models/decision_tree_model.pkl")
        return accuracy

    def save_model(self,model,model_pkl_file)->None:
        # save the classification model as a pickle file

        with open(model_pkl_file, 'wb') as file:  
            dump(model, file)