from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Thiết lập các thông tin API của Google
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('./certificates.json', scope)
client = gspread.authorize(creds)

# Kết nối đến Google Sheets và lấy dữ liệu
sheet = client.open("My Certificates").sheet1
data = sheet.get_all_records()

@app.route('/')
def home():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
