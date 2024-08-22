import json
import os

import gspread
from jinja2 import Template
from oauth2client.service_account import ServiceAccountCredentials

# Thiết lập Google Sheets API

# Đọc thông tin xác thực từ secret
credentials_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])

# Xác định phạm vi truy cập
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

# Xác thực và khởi tạo client
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_info, scope)
client = gspread.authorize(credentials)

# Mở Google Sheets bằng URL hoặc tên
spreadsheet = client.open("My Certificates")
sheet = spreadsheet.sheet1  # Mở sheet đầu tiên

# Đọc dữ liệu từ sheet
data = sheet.get_all_records()

# Đảo ngược thứ tự dữ liệu để hiển thị từ mới nhất lên đầu
data.reverse()


# Đọc template HTML và render với dữ liệu mới
with open("templates/index.html") as file_:
    template = Template(file_.read())
    rendered_html = template.render(data=data)

# Lưu file HTML đã được render
with open("index.html", "w") as f:
    f.write(rendered_html)
