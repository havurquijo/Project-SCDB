from pathlib import Path
import requests
import pandas as pd
from zipfile import ZipFile, BadZipFile, LargeZipFile

class mine_decision_tree:
    # Attributes
    base = pd.DataFrame()

    def __init__(self) -> None:
        pass

    def download_file(self) -> bool:
        csv_path = Path("models/SCDB_2023_01_justiceCentered_Citation/SCDB_2023_01_justiceCentered_Citation.csv")
        if csv_path.exists():
            return True

        url = 'http://scdb.wustl.edu/_brickFiles/2023_01/SCDB_2023_01_justiceCentered_Citation.csv.zip'
        file_name_local = Path('models/SCDB_2023_01_justiceCentered_Citation.csv.zip')

        response = requests.get(url)
        # Error handling
        if response.status_code == 200:
            # Write the downloaded content to a local file
            file_name_local.parent.mkdir(parents=True, exist_ok=True)
            with open(file_name_local, 'wb') as local_file:
                local_file.write(response.content)
            print('Download completed successfully.')
        else:
            print('Failed to download the file. Status code:', response.status_code)
            return False

        # Extract the ZIP file
        extract_dir = Path('./models/SCDB_2023_01_justiceCentered_Citation/')
        extract_dir.mkdir(parents=True, exist_ok=True)

        try:
            with ZipFile(file_name_local, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            print('File successfully extracted.')
            return True
        except BadZipFile:
            print('Invalid ZIP file.')
            return False
        except LargeZipFile:
            print('ZIP file is too large.')
            return False
        except Exception as e:
            print('An error occurred:', e)
            return False

    def load_base(self) -> None:
        address = Path("models/SCDB_2023_01_justiceCentered_Citation/SCDB_2023_01_justiceCentered_Citation.csv")
        if address.exists():
            data = pd.read_csv(address, encoding='ISO-8859-1')
            self.base = data[['voteId', 'issueArea', 'petitionerState', 'respondentState', 'jurisdiction', 'caseOriginState', 'caseSourceState', 'certReason', 'lcDisposition', 'decisionDirection']]
        else:
            if self.download_file():
                self.load_base()
            else:
                raise FileNotFoundError("The file couldn't be loaded.")

    def preprocess(self) -> None:
        if not self.verify_preprocessed():
            self.base['voteId'] = self.base['voteId'].str[-2:]
            # Eliminate NaN values
            self.base.dropna(subset=['petitionerState', 'respondentState', 'jurisdiction', 'caseOriginState', 'caseSourceState', 'issueArea', 'decisionDirection', 'certReason', 'lcDisposition'], inplace=True)
            self.base = self.base[self.base.decisionDirection != 3]
            # Save the preprocessed data
            self.base.to_csv('models/preprocessed_decision_tree.csv', sep=';', index=False)

    def verify_preprocessed(self) -> bool:
        address = Path("models/preprocessed_decision_tree.csv")
        return address.exists()
