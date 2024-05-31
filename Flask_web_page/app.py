from flask import Flask, redirect, url_for, render_template, request,jsonify # type: ignore
from mine_decision_tree import mine_decision_tree as mine_tree_class
from predict_decision_tree import predict_decision_tree as predict_tree_class
from train_decision_tree import train_decision_tree as train_tree_class
import time
from os.path import exists
from numpy import savetxt, loadtxt
from pandas import DataFrame
from markupsafe import escape
from tkinter.filedialog import asksaveasfilename
from tkinter import *
from flask_caching import Cache

app = Flask(__name__)

# Configure the cache
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

@app.route("/")#url for routing
#This function basically writes the html page
def homePage():
    #This value at the return should be changed by a html document separately created
    return render_template("index.html")

@app.route("/<some_url>")
def notFound(some_url):
    match some_url:
        case "user":
            return redirect(url_for("admin"))
        case "admin":
            return redirect(url_for("user"))
        case _:
            return render_template("notFound.html")

@app.route("/admin")
def admin():
    return "<h1>Admin page</h1>"

@app.route("/user")
@app.route("/user/<user_name>")
def user(user_name='default'):
    return f"<h1>User page, user name {escape(user_name)}</h1>"

@app.route("/predict_tree", methods=["POST","GET"])
def predict_tree():
    if exists("models/accuracy_tree.txt"):
        accuracy = loadtxt("models/accuracy_tree.txt")
        visible=True
    else:
        visible=False
        accuracy=0
    if request.method == "POST":
        voteId = float(request.form["voteID"])
        issueArea = float(request.form["issueArea"])
        petitionerState = float(request.form["petitionerState"])
        respondentState = float(request.form["respondentState"])
        jurisdiction = float(request.form["jurisdiction"])
        caseOriginState = float(request.form["caseOriginState"])
        caseSourceState = float(request.form["caseSourceState"])
        certReason = float(request.form["certReason"])
        lcDisposition = float(request.form["lcDisposition"])
        predict_tree_ = predict_tree_class()  
        predict_tree_.set_predictors([voteId,issueArea,petitionerState,respondentState,jurisdiction,caseOriginState,caseSourceState,certReason,lcDisposition])      
        decisionDirection=predict_tree_.predict_self()
        return redirect(url_for("predicted_tree",
                                accuracy_visible="p_shown", 
                                accuracy_var=f"{accuracy*100:.1f}"+"%",
                                decisionDirection=decisionDirection,
                                voteId = voteId,
                                issueArea = issueArea,
                                petitionerState = petitionerState,
                                respondentState = respondentState,
                                jurisdiction = jurisdiction,
                                caseOriginState = caseOriginState,
                                caseSourceState = caseSourceState,
                                certReason = certReason,
                                lcDisposition = lcDisposition
                               ))
    if visible:
        return render_template("predict_tree.html",accuracy_visible="p_shown", accuracy_var=f"{accuracy*100:.1f}"+"%",decisionDirection="= Not calculated yet")
    else:
        return render_template("predict_tree.html",accuracy_visible="p_hidden", accuracy_var="0.0"+"%",decisionDirection="= Not calculated yet")

@app.route("/predicted_tree", methods=["GET","POST"])
def predicted_tree():
    values = request.args.to_dict()
    accuracy_visible = values.get('accuracy_visible', '')
    accuracy_var = values.get('accuracy_var', '')
    voteId = values.get("voteId", '')
    issueArea = values.get("issueArea", '')
    petitionerState = values.get("petitionerState", '')
    respondentState = values.get("respondentState", '')
    jurisdiction = values.get("jurisdiction", '')
    caseOriginState = values.get("caseOriginState", '')
    caseSourceState = values.get("caseSourceState", '')
    certReason = values.get("certReason", '')
    lcDisposition = values.get("lcDisposition", '')
    decisionDirection = values.get("decisionDirection", '')
    if request.method=="POST":
        values = request.values.to_dict()
        print(values)
        was_saved=False
        df = DataFrame([values])  # Wrap new_values in a list to create a DataFrame with one row
        tk = Tk()
        filename = asksaveasfilename(initialfile = 'Untitled.csv',
            defaultextension=".csv",filetypes=[("All Files","*.*"),("Comma Separated Values Source File","*.csv")])
        tk.destroy()
        try:
            df.to_csv(filename, sep=';', index=False)
            print("Data saved successfully.")
            was_saved= True
        except Exception as e:
            print(f"Error saving data: {e}")
        

        #was_saved = save_prediction_csv(values)
        if was_saved:
            response = jsonify({'status': 'success', 'message': 'File successfully saved!', 'redirect': url_for('predict_tree')})
        else:
            response = jsonify({'status': 'fail', 'message': 'Error while saving!'})
        return response
    return render_template("predicted_tree.html",
                           accuracy_visible=accuracy_visible,
                           accuracy_var=accuracy_var,
                           decisionDirection=decisionDirection,
                           voteId=voteId,
                           issueArea=issueArea,
                           petitionerState=petitionerState,
                           respondentState=respondentState,
                           jurisdiction=jurisdiction,
                           caseOriginState=caseOriginState,
                           caseSourceState=caseSourceState,
                           certReason=certReason,
                           lcDisposition=lcDisposition)


@app.route("/mine_tree", methods=["POST","GET"])
def mine_tree():
    mine_tree_=mine_tree_class()
    if request.method == "POST":
        mine_tree_.download_file()
        mine_tree_.load_base()
        mine_tree_.preprocess()
        return jsonify({'status': 'success', 'message':'Data mined succesfully!', 'redirect': url_for('train_tree')})
    return render_template("mine_tree.html")

@app.route("/train_tree", methods=["POST","GET"])
def train_tree():
    if request.method == "POST":
        mine_tree_=mine_tree_class()
        if not mine_tree_.verify_preprocessed():
            return jsonify({'status': 'fail', 'message':'File not found, download the file of data first', 'redirect': url_for('mine_tree')})
        max_depth = int(request.form["max_depth"])
        test_size = int(request.form["test_size"])
        random_states = int(request.form["random_states"])
        train_tree_=train_tree_class()
        accuracy = train_tree_.train(max_depth=max_depth,test_size=test_size/100.0,random_state=random_states)
        savetxt("models/accuracy_tree.txt",[accuracy])
        # Simulate a long-running process
        time.sleep(2)
        #passos para ver se o arquivo foi baixado 
        return jsonify({'status': 'success', 'message':'Machine trained succesfully!', 'redirect': url_for('predict_tree',show_accuracy="true",accuracy_visible="p_shown",accuracy_var=f"{accuracy*100:.1f}"+"%")})
    return render_template("train_tree.html")

def save_prediction_csv(new_values)->bool:
    if new_values:
        df = DataFrame([new_values])  # Wrap new_values in a list to create a DataFrame with one row
        tk = Tk()
        filename = asksaveasfilename(initialfile = 'Untitled.csv',
            defaultextension=".csv",filetypes=[("All Files","*.*"),("Comma Separated Values Source File","*.csv")])
        if filename is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return False
        tk.destroy()
        try:
            df.to_csv(filename, sep=';', index=False)
            print("Data saved successfully.")
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
    else:
        print("No data to save.")
    return False   

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
