import os

import gspread
from jinja2 import Template
from oauth2client.service_account import ServiceAccountCredentials

# Thiết lập Google Sheets API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Kết nối với Google Sheets
sheet = client.open("My Certificates").sheet1
data = sheet.get_all_records()
# data = data.reverse()

# Đọc template HTML và render với dữ liệu mới
with open("templates/index.html") as file_:
    template = Template(file_.read())
    rendered_html = template.render(data=data)

# Lưu file HTML đã được render
with open("index.html", "w") as f:
    f.write(rendered_html)
