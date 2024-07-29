from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Edge Driver path
_edge_driver_path = r'C:\webdriver\msedgedriver.exe'

# Options for Edge Driver
_options = Options()
_options.use_chromium = True  
_options.add_argument('--inprivate')
_options.add_argument('--disable-cache')
_options.add_argument('--disable-application-cache')
_options.add_experimental_option("detach", True) # Keep Browser open
_options.add_argument("--log-level=3")

# Start Driver
_service = Service(executable_path=_edge_driver_path)
_driver = webdriver.Edge(service=_service, options=_options)

def start_wordle():
  url = "https://www.nytimes.com/games/wordle/index.html" # Wordle URL
  _driver.get(url) 

  # Start game by clicking start button and closing the How-To-Play pop-up
  wait = WebDriverWait(_driver, 10)
  play_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="Play"]')))
  play_button.click()
  close_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Close"]')))
  close_button.click()


def exit_wordle():
  _driver.quit()



def get_word_results(guess_number):
  row_div = _driver.find_element(By.CSS_SELECTOR, f'div[aria-label="Row {guess_number}"]')

  # Define the aria-labels you are looking for
  aria_labels = ["1st letter", "2nd letter", "3rd letter", "4th letter", "5th letter"]

  # Find the divs with the specified aria-labels within the Row 1 div
  letter_divs = [row_div.find_element(By.CSS_SELECTOR, f'div[aria-label*="{label}"]') for label in aria_labels]

  # Extract the text or any other required attribute from the found divs
  states = []
  for div in letter_divs:
    states.append(div.get_attribute("data-state"))
  
  return states


def input_guess(guess):
  body = _driver.find_element(By.CSS_SELECTOR, 'body')
  body.send_keys(guess)
  body.send_keys(Keys.ENTER)

# time.sleep(3)
# body = driver.find_element(By.CSS_SELECTOR, 'body')
# body.send_keys('arose')
#body.send_keys(Keys.ENTER)

# time.sleep(3)
# body.send_keys('chimp')
# body.send_keys(Keys.ENTER)

# time.sleep(3)
# body.send_keys('chimp')
# body.send_keys(Keys.ENTER)
