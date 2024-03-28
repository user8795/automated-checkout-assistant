from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import time

def clickButton(XPATH_):
	button = wd.find_element(By.XPATH, XPATH_)
	button.click()

def awaitButtonANDClickButton(XPATH_):
	WebDriverWait(wd, 5).until(
		EC.presence_of_element_located((By.XPATH, XPATH_))
	)
	button = wd.find_element(By.XPATH, XPATH_)
	button.click()

def fillInputBox(XPATH_, inputText_):
	WebDriverWait(wd, 5).until(
	EC.presence_of_element_located((By.XPATH, XPATH_))
	)

	inputBox = wd.find_element(By.XPATH, XPATH_)
	inputBox.clear()
	inputBox.send_keys(inputText_ + Keys.TAB)



service = Service(executable_path = "chromedriver.exe")
wd = webdriver.Chrome()

#PAGE MUST BE SPECIFIED HERE
#open the page 
url = 'enterYourURLHere'
wd.get(url)


#NEXT STEP button click
#finding the add to cart element AND clicking it 
addButtonToCartXPATH = '//*[@id="ProductBuy"]/div/div[2]/button'
clickButton(addButtonToCartXPATH)
#CAN USE LINES BELOW OR CAN CALL THE FUNCTION ABOVE^ clickButton
# addButtonToCart = wd.find_element(By.XPATH, addButtonToCartXPATH)
# addButtonToCart.click()


#NEXT STEP button click
#wait for the page to load to click 
noThanksButtonXPATH = '//*[@id="modal-intermediary"]/div/div/div/div[4]/button[1]'
awaitButtonANDClickButton(noThanksButtonXPATH)
#CAN USE LINES BELOW OR CAN CALL THE FUNCTION ABOVE^ awaitButtonANDClickButton
# WebDriverWait(wd, 5).until(
# 	EC.presence_of_element_located((By.XPATH, noThanksButtonXPATH))
# )
# #finding the no thanks button
# noThanksButton = wd.find_element(By.XPATH, noThanksButtonXPATH)
# noThanksButton.click()


#NEXT STEP button click
#wait for the page to load to click 
proceedToCheckoutButtonXPATH = '//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]'
awaitButtonANDClickButton(proceedToCheckoutButtonXPATH)
#CAN USE LINES BELOW OR CAN CALL THE FUNCTION ABOVE^ awaitButtonANDClickButton
# WebDriverWait(wd, 5).until(
# 	EC.presence_of_element_located((By.XPATH, proceedToCheckoutButtonXPATH))
# )
# #finding the proceed to checkout button
# proceedToCheckoutButton = wd.find_element(By.XPATH, proceedToCheckoutButtonXPATH)
# proceedToCheckoutButton.click()


#NEXT STEP button click
#wait for the page to load to click 
continueAsGuestButtonXPATH = '//*[@id="app"]/div/div[2]/div/div/div/form[2]/div[2]/div/button'
awaitButtonANDClickButton(continueAsGuestButtonXPATH)
#CAN USE LINES BELOW OR CAN CALL THE FUNCTION ABOVE^ awaitButtonANDClickButton
# WebDriverWait(wd, 5).until(
# 	EC.presence_of_element_located((By.XPATH, continueAsGuestButtonXPATH))
# )
# #finding the continue as guest button
# continueAsGuestButton = wd.find_element(By.XPATH, continueAsGuestButtonXPATH)
# continueAsGuestButton.click()


#NEXT STEP
#wait until element appears for name entering
fullNameInputBoxXPATH = '//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[1]/input'
fillInputBox(fullNameInputBoxXPATH, "tim fernoth")

# WebDriverWait(wd, 5).until(
# 	EC.presence_of_element_located((By.XPATH, fullNameInputBoxXPATH))
# )
# fullNameInputBox = wd.find_element(By.XPATH, fullNameInputBoxXPATH)
# fullNameInputBox.clear()
# fullNameInputBox.send_keys("tech with tim" + Keys.TAB)


#NEXT STEP
phoneInputBoxXPATH = '//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[4]/input'
fillInputBox(phoneInputBoxXPATH, "6132223434")

#NEXT STEP
addressInputBoxXPATH = '//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[6]/label[2]/input'
fillInputBox(addressInputBoxXPATH, "74 Krosts Cres Kanata ON K2K 3E4 Canada")

#NEXT STEP
cityInputBoxXPATH = '//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[10]/label[2]/input'
fillInputBox(cityInputBoxXPATH, "greenhill")

#NEXT STEP 
provinceBoxXPATH = '//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[11]/label[2]/select'
provinceBox = wd.find_element(By.XPATH, provinceBoxXPATH)
Select(provinceBox).select_by_value('ON')

#NEXT STEP
postalCodeInputBoxXPATH = '//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[12]/input'
fillInputBox(postalCodeInputBoxXPATH, "K2K3E4")

#NEXT STEP
emailAddressInputBoxXPATH = '//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[14]/input'
fillInputBox(emailAddressInputBoxXPATH, "tester@email.com")

#NEXT STEP
saveButtonXPATH = '//*[@id="app"]/div/div/div/div/div[3]/button[2]'
clickButton(saveButtonXPATH)

time.sleep(50)
