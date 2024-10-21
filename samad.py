import requests

# ارسال یک درخواست GET به یک URL
response = requests.get('https://samad.app/login')

# بررسی وضعیت پاسخ
print(response.status_code)  # وضعیت 200 نشان‌دهنده موفقیت آمیز بودن درخواست است

# مشاهده محتویات پاسخ
print(response.text)