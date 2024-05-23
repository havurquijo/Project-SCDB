import requests
import zipfile
import os

url='http://scdb.wustl.edu/_brickFiles/2023_01/SCDB_2023_01_justiceCentered_Citation.csv.zip'
file_name_local = 'SCDB_2023_01_justiceCentered_Citation.csv.zip'

response = requests.get(url)
#Error managing
if response.status_code == 200:
    # Abrindo o arquivo local em modo de escrita binária (wb) e escreva o conteúdo baixado nele
    with open(file_name_local, 'wb') as local_file:
        local_file.write(response.content)
    print('Download concluído com sucesso.')
else:
    print('Falha ao baixar o arquivo. Status code:', response.status_code)

# Specify the path to the ZIP file
zip_file_path = 'SCDB_2023_01_justiceCentered_Citation.csv.zip'

# Specify the directory where you want to extract the contents
extract_dir = 'SCDB_2023_01_justiceCentered_Citation/'

# Create the directory if it doesn't exist
os.makedirs(extract_dir, exist_ok=True)

try:
    # Open the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all the contents to the specified directory
        zip_ref.extractall(extract_dir)
    print('File successfully extracted.')
except zipfile.BadZipFile:
    print('Invalid ZIP file.')
except zipfile.LargeZipFile:
    print('ZIP file is too large.')
except Exception as e:
    print('An error occurred:', e)