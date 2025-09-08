import time
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import logging
import schedule
import pyttsx3  # for voice alerts

# Configuration
THRESHOLD_DOWNLOAD = 20  # Mbps
THRESHOLD_UPLOAD = 5     # Mbps
CSV_FILE = "internet_speed_log.csv"

# Setup logging
logging.getLogger('selenium').setLevel(logging.WARNING)

# TTS engine
engine = pyttsx3.init()

# Chrome options
chrome_option = Options()
chrome_option.add_argument("--headless")
chrome_option.add_argument("--disable-blink-features=AutomationControlled")
chrome_option.add_argument("--window-size=1920,1080")
chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])  # Hide DevTools logs

chrome_service = ChromeService(ChromeDriverManager().install())

def wait_for_non_zero_value(by, value_id, timeout=60):
    for _ in range(timeout):
        try:
            element = driver.find_element(by, value_id)
            text = element.text.strip()
            if text and text != "0":
                return text
        except:
            pass
        time.sleep(1)
    return "0"

def get_full_speed_metrics():
    try:
        driver.get("https://fast.com/")

        # Wait for "Show more info" to be clickable, not just present
        show_more = WebDriverWait(driver, 90).until(
            EC.element_to_be_clickable((By.ID, 'show-more-details-link'))
        )
        show_more.click()
        time.sleep(1)

        # Wait for values to become non-zero
        download = wait_for_non_zero_value(By.ID, 'speed-value')
        upload = wait_for_non_zero_value(By.ID, 'upload-value')
        latency = wait_for_non_zero_value(By.ID, 'latency-value')

        return {
            "Download": float(download),
            "Upload": float(upload),
            "Latency": float(latency)
        }

    except Exception as e:
        return {"Error": str(e)}

def log_to_csv(data):
    is_new = False
    try:
        with open(CSV_FILE, 'r'):
            pass
    except FileNotFoundError:
        is_new = True

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["Timestamp", "Download (Mbps)", "Upload (Mbps)", "Latency (ms)"])
        writer.writerow([
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data["Download"],
            data["Upload"],
            data["Latency"]
        ])

def check_and_alert(data):
    alert_msgs = []
    if data["Download"] < THRESHOLD_DOWNLOAD:
        alert_msgs.append(f"Download speed is low: {data['Download']} Mbps")
    if data["Upload"] < THRESHOLD_UPLOAD:
        alert_msgs.append(f"Upload speed is low: {data['Upload']} Mbps")
    
    for msg in alert_msgs:
        print("⚠️ ALERT:", msg)
        engine.say(msg)
        engine.runAndWait()

def run_test():
    global driver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_option)
    try:
        data = get_full_speed_metrics()
        if "Error" not in data:
            print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] ✅ Speed Test Result:")
            print(f"Download: {data['Download']} Mbps | Upload: {data['Upload']} Mbps | Latency: {data['Latency']} ms")
            log_to_csv(data)
            check_and_alert(data)
        else:
            print("❌ Error:", data["Error"])
    finally:
        driver.quit()

# Initial test run
#run_test()

# Schedule: every 30 minutes
#schedule.every(30).minutes.do(run_test)

#while True:
#schedule.run_pending()
