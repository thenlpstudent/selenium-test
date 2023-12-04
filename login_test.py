from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = "https://chinternal.caresystemsinc.com/Capital_Health_QA_Trunk/html_interface/staff/login.jsp"; 




LOGIN_SUCCESS   = 0
LOGIN_UNSUCCESS = 1 
LOGIN_ADMIN     = 2 

def login_testcase(url, username, password, expected_type):
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        driver.get(url)
        username_text = driver.find_element(by=By.ID, value="txtUsername")
        password_text = driver.find_element(by=By.ID, value="txtPassword")
        login_btn = driver.find_element(by=By.CLASS_NAME, value="btn-primary")
        username_text.send_keys(username)
        password_text.send_keys(password)

        login_btn.click()
        time.sleep(5) 

        isPassed = False 
        if (expected_type == LOGIN_SUCCESS):
                message_box = driver.find_element(by=By.ID, value="messagebox_modal")
                if (message_box != None):
                        message_title = driver.find_element(by=By.ID, value="messagebox_title") 
                        messagetext = message_title.text 
                        if (messagetext == "Confirm"):
                                isPassed = True 
                else:
                       isPassed = 'dashboard.jsp' in driver.current_url   

        
        driver.quit()
        return isPassed

isPassed = login_testcase( url, "Rcanada", "admin", LOGIN_SUCCESS)
print(isPassed)
isPassed = login_testcase( url, "Vcanada", "admin", LOGIN_SUCCESS)
print(isPassed) 