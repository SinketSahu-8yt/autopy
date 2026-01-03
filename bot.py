import os
import time
import subprocess
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- HELPER FUNCTIONS ---

def generate_password(length=12):
    """Ek random password banane ke liye"""
    chars = string.ascii_letters + string.digits + "!@#$"
    return ''.join(random.choice(chars) for i in range(length))

def get_temp_email():
    """mmail tool ka use karke naya email lena"""
    print("Fetching new email from mmail...")
    # mmail.py ko run karke output lena
    email = subprocess.getoutput("python mmail/mmail.py -n")
    return email.strip()

def check_for_otp():
    """mmail ke inbox se OTP ya code check karna"""
    print("Checking inbox for code...")
    inbox = subprocess.getoutput("python mmail/mmail.py -i")
    return inbox

# --- MAIN AUTOMATION ---

def start_bot(target_url):
    # 1. Email aur Password generate karo
    email = get_temp_email()
    password = generate_password()
    print(f"Generated Email: {email}")
    print(f"Generated Password: {password}")

    # 2. Browser Setup (Termux specific)
    chrome_options = Options()
    chrome_options.add_argument('--headless') # Browser screen nahi dikhayega
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # 3. Website par jana
        print(f"Opening: {target_url}")
        driver.get(target_url)
        time.sleep(5) # Page load hone ka wait

        # 4. Sign-up Form bharna (Example Selectors)
        # Note: 'email' aur 'password' name har site par alag ho sakte hain
        driver.find_element(By.NAME, "email").send_keys(email)
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(password)
        
        # Submit button click karna
        # driver.find_element(By.ID, "submit").click() 
        
        print("Form filled! Now check your mmail inbox for OTP.")
        
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # driver.quit() # Browser band karne ke liye
        pass

# Script start point
if __name__ == "__main__":
    target = input("Enter Signup URL: ")
    start_bot(target)
