import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--headless")
# Set up the Selenium WebDriver
driver = webdriver.Chrome(options = options)  # Adjust this based on your preferred browser and its corresponding WebDriver


# Navigate to the website
driver.get("https://lanes-germany.com/meknes/telc-anmeldung/")
i = 1
while (i==1) :

    try :
        # Wait until the booking becomes available (modify the waiting time according to your needs)
        wait = WebDriverWait(driver, 5)  # Wait for a maximum of 60 seconds
        booking_button = wait.until(EC.element_to_be_clickable((By.ID, "booking-button")))

        # Click the booking button
        booking_button.click()

        # Fill out the necessary form fields (modify the element locators and values accordingly)
        name_input = driver.find_element(By.ID, "name")
        name_input.send_keys("ABD-ELHAQ AZROUR")

        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("abdelhakazrour3@gmail.com")

        # Submit the reservation request (modify the element locator accordingly)
        submit_button = driver.find_element(By.ID, "submit-button")
        submit_button.click()

        print('inscription done ')
        # Close the browser window
    except Exception as e :
        print('ba9i mabdat inscription')
    driver.quit()
    time.sleep(60)