from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

filetxt = input("What is your txt File Name")
def open_website_in_tab(url, driver):
    try:
        # Open the URL in a new tab
        driver.execute_script(f"window.open('{url}', '_blank');")
        print(f"Opened: {url}")

        # Switch to the newly opened tab
        driver.switch_to.window(driver.window_handles[-1])

        # Maximize the browser window
        driver.maximize_window()

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    except Exception as e:
        print(f"Failed to open: {url} - {e}")


if __name__ == "__main__":
    # Initialize Chrome webdriver
    driver = webdriver.Chrome()

    with open(filetxt, 'r') as file:
        urls = file.readlines()

        for url in urls:
            url = url.strip()  # Remove any leading or trailing whitespace
            open_website_in_tab(url, driver)

        print("All websites opened. Close the browser manually to exit.")

    # Wait for user interaction before closing the browser
    input("Press Enter to close the browser...")
    driver.quit()