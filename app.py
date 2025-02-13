import gspread
import os
import json
from jinja2 import Template
from google.oauth2.service_account import Credentials

# Đọc credentials từ biến môi trường (GitHub Secrets hoặc Local)
service_account_info = json.loads(os.getenv("GOOGLE_CREDENTIALS"))

# Xác thực Google Sheets API
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
creds = Credentials.from_service_account_info(service_account_info, scopes=scope)
client = gspread.authorize(creds)

try:
    # Kết nối Google Sheets
    sheet = client.open("certificate").sheet1
    data = sheet.get_all_records()

    # Đảo ngược dữ liệu để hiển thị chứng chỉ mới nhất
    data.reverse()

    # Render HTML template
    with open("templates/index.html") as file_:
        template = Template(file_.read())
        rendered_html = template.render(data=data)

    # Lưu kết quả ra file index.html
    with open("index.html", "w") as f:
        f.write(rendered_html)

    print("✅ HTML đã được tạo thành công!")

except Exception as e:
    print(f"❌ Lỗi khi truy cập Google Sheets: {e}")
