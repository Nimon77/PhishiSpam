from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import string
import random
import asyncio

def spamDriver():
	driver = webdriver.Chrome()
	driver.get('https://steamcommuty.com/tradeoffer/new/?partner=178761549&token=r98Wq4_Hk')

	click = 0
	while (click == 0):
		try:
			driver.find_element_by_xpath('//*[@id="pagebtn_next"]').click()
			click = 1
		except Exception as e:
			print(e)
			driver.maximize_window()
			time.sleep(1)
	time.sleep(2)
	driver.minimize_window()
	random.seed()
	while 1:
		letters = string.ascii_letters.join(string.digits)
		user = ''.join(random.choice(letters) for i in range(random.randrange(5, 15)))
		passw = ''.join(random.choice(letters) for i in range(5, 25))
		print(f'{user}:{passw}')
		try:
			driver.find_element_by_xpath('//*[@id="input_username"]').clear()
			driver.find_element_by_xpath('//*[@id="input_password"]').clear()
			driver.find_element_by_xpath('//*[@id="input_username"]').send_keys(user)
			driver.find_element_by_xpath('//*[@id="input_password"]').send_keys(passw)
			driver.find_element_by_xpath('//*[@id="login_btn_signin"]/button').click()
			time.sleep(5)
		except Exception as e:
			print(e)
	
	driver.quit()

async def main():
	await asyncio.gather(
		asyncio.to_thread(spamDriver),
		asyncio.to_thread(spamDriver),
		asyncio.to_thread(spamDriver),
		asyncio.to_thread(spamDriver)
	)

asyncio.run(main())
