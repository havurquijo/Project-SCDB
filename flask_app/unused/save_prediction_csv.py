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


#was_saved = save_prediction_csv(values)
#if was_saved:
#    response = jsonify({'status': 'success', 'message': 'File successfully saved!', 'redirect': url_for('predict_tree')})
#else:
#    response = jsonify({'status': 'fail', 'message': 'Error while saving!'})
#return response