from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# مسیر به chromedriver
driver_path = 'D:/Installed_apps/chromedriver-win64/chromedriver.exe'

# ایجاد سرویس کروم و سپس راه‌اندازی مرورگر
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# رفتن به صفحه لاگین
driver.get("https://samad.app/login")

# صبر کوتاه برای بارگذاری صفحه
time.sleep(2)

# پیدا کردن و کلیک روی دکمه باز کردن لیست دانشگاه‌ها
university_button = driver.find_element(By.CLASS_NAME, "input-btn-edit")
university_button.click()

# صبر برای نمایش لیست دانشگاه‌ها
time.sleep(2)

# انتخاب دانشگاه "دانشگاه فنی و حرفه ای" از لیست
university_option = driver.find_element(By.XPATH, "//li[contains(text(), 'دانشگاه فنی و حرفه ای')]")
university_option.click()

# صبر کوتاه برای اعمال انتخاب
time.sleep(1)

# پیدا کردن فیلد نام کاربری و رمز عبور
username_field = driver.find_element(By.NAME, "username")  # توجه کنید که این selector ممکن است نیاز به تغییر داشته باشد
password_field = driver.find_element(By.NAME, "password")  # همینطور برای پسورد

# پر کردن فیلدها
username_field.send_keys("00131161907021")
password_field.send_keys("Mendokusai@samad")

# ارسال فرم (با زدن Enter)
password_field.send_keys(Keys.RETURN)

# صبر برای بارگذاری صفحه بعد از ورود
time.sleep(5)

# دریافت و چاپ HTML صفحه بعد از ورود
print(driver.page_source)

# بستن مرورگر
driver.quit()
