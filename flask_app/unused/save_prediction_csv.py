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