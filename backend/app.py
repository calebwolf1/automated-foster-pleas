from flask import Flask, jsonify
from flask_cors import CORS
import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)
CORS(app)

def get_google_sheet_data():
    # Define the scope
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Authenticate using the credentials JSON file
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet by its name or URL
    sheet = client.open("My Sheet").sheet1  # Access the first sheet

    # Fetch all rows of data
    data = sheet.get_all_records()  # Returns a list of dictionaries
    return data

@app.route('/api/data', methods=['GET'])
def get_data():
    print(get_google_sheet_data())
    return jsonify({"message": "Hello from Flask!", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
