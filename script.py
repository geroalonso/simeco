#importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date
from selenium.webdriver.chrome.options import Options


chrome_options = Options()  
chrome_options.add_argument("--headless") 
chrome_options.add_argument("user-agent= G.Alonso Scraper contact me if my bot is behaving intrusively: geronimoalonso@icloud.com")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.implicitly_wait(10) #set implicit wait
url = 'https://z0723.cponline.org.ar/lsm/login?code=01' #set the website
driver.get(url) #open the browser

sociotipo = Select(driver.find_element_by_id("loginValida_socioTipo"))
sociotipo.select_by_visible_text("SIMECO")

doctipo = Select(driver.find_element_by_id("loginValida_doctoTipo"))
doctipo.select_by_visible_text("DOCUMENTO NACIONAL DE IDENTIDAD")

dni = driver.find_element_by_xpath("//input[@name = 'doctoNumero']")
dni.send_keys(7670684)


socio = driver.find_element_by_xpath("//input[@name = 'socio']")
socio.send_keys('001084')

nacimiento = driver.find_element_by_xpath("//input[@name = 'nacimiento']")
nacimiento.send_keys("30/03/1949")

ingresar = driver.find_element_by_xpath("//button[contains(text(), 'Ingresar')]")
ingresar.click()

consulcc = driver.find_element_by_xpath("//input[@title = 'Consultar Cuenta Corriente']")
consulcc.click()


driver.switch_to.window(driver.window_handles[-1])
deuda = driver.find_element_by_xpath("//table//tr[2]/td[6]").text

print('La deuda al dia de hoy es: $' + str(deuda))

driver.quit()