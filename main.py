from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk

def start_automation():
    LINK = entry.get()
    if LINK.strip() != '':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=chrome_options)
        print('thank you sir, just relax we will do all the work')
        driver.get(LINK)
        wait = WebDriverWait(driver, 10)
        data = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="plaintext"]/ul')))
        links = data.text.splitlines()
        for link in links:
            driver.get(link)
            download_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/button')))
            driver.execute_script("arguments[0].click();", download_button)
            time.sleep(0.2)
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.execute_script("arguments[0].click();", download_button)
            time.sleep(2)
    else:
        print('incorrect link brother')
window = tk.Tk()
window.geometry('350x200')
entry = tk.Entry(fg='black', bg='orange', width=50)
label = tk.Label(text='paste your link here sir', font=('Arial', 20))
label.pack()
entry.pack(pady=40)
button = tk.Button(window, text='Enter', command=start_automation)
button.pack()
window.mainloop()