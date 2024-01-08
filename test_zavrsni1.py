from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import os
import time
import filecmp

browser = ChromeOptions()
browser.add_argument("--window-size=1800,1080")
hrom = Chrome(options=browser)

hrom.get("http://gresnik.com/?page=pocetna")
hrom.save_screenshot("pocetna.png")
hrom.execute_script("document.body.style.zoom='40%'")
hrom.implicitly_wait(5)

procitajte_jos_trazeno = "Pročitajte još"
procitajte_jos = hrom.find_element(By.LINK_TEXT,"Pročitajte još")
assert procitajte_jos_trazeno in procitajte_jos.text
hrom.execute_script("arguments[0].click();", procitajte_jos)

procitajte_jos_main_trazeno = "Donald Tramp se izvinio premijeru Crne Gore"
procitajte_jos_main = hrom.find_elements(By.TAG_NAME,"h3")
# for i in procitajte_jos_main:
#     print(i.text)
procitajte_jos_main_sajt = procitajte_jos_main[1].text
assert procitajte_jos_main_sajt in procitajte_jos_main_trazeno

main = hrom.find_element(By.CLASS_NAME,"main")
slika = main.find_element(By.TAG_NAME,"img")
# print(slika.get_attribute("src"))
hrom.save_screenshot("trump.png")

donald_path = os.path.abspath("trump.jpg")
are_files_equal = filecmp.cmp("trump.jpg", donald_path)
assert are_files_equal
hrom.implicitly_wait(5)

ob = hrom.find_element(By.LINK_TEXT,"O Blogu")
ob.click()
hrom.save_screenshot("oblogu.png")

ulogovati_se = "Log in"
login = hrom.find_element(By.XPATH,"/html/body/nav/div/div[2]/div[2]/ul/li[4]/a")
assert ulogovati_se == login.text
login.click()
hrom.implicitly_wait(5)

username = hrom.find_element(By.XPATH,"/html/body/section/div/div/div/div/form/div/input[1]")
username.send_keys("Autor")
passwd = hrom.find_element(By.XPATH,"/html/body/section/div/div/div/div/form/div/input[2]")
passwd.send_keys("123")
hrom.save_screenshot("login.png")
passwd.send_keys(Keys.ENTER)

nc = "Novi članak"
novi_clanak = hrom.find_element(By.LINK_TEXT,"Novi članak")
hrom.save_screenshot("admin_panel.png")
assert nc == novi_clanak.text
novi_clanak.click()
hrom.save_screenshot("novi_clanak.png")

kp_trazeno = "Kratko uputstvo"
kp = hrom.find_elements(By.TAG_NAME,"h3")
# for i in novi_clanak:
#       print(i.text)
kp_sajt = kp[2].text
assert kp_trazeno in kp_sajt

sc_trazeno = "Svi Članci"
sc = hrom.find_element(By.LINK_TEXT,"Svi Članci")
assert sc_trazeno in sc.text
sc.click()
hrom.save_screenshot("svi_clanci.png")
hrom.implicitly_wait(5)

hrom.execute_script("document.body.style.zoom='40%'")
hrom.implicitly_wait(5)

vsp_trazeno = "Donald Tramp se izvinio premijeru Crne Gore"
vsp = hrom.find_element(By.LINK_TEXT,"Donald Tramp se izvinio premijeru Crne Gore")
assert vsp_trazeno == vsp.text
hrom.execute_script("arguments[0].click();", vsp)
hrom.save_screenshot("dtc.png")
hrom.implicitly_wait(5)


novi_clanak = hrom.find_element(By.CSS_SELECTOR, "ul.vertical.medium-horizontal.menu li:nth-child(2) a")
assert novi_clanak.text in nc
novi_clanak.click()
hrom.save_screenshot("novi_clanak_2.png")
hrom.implicitly_wait(5)

hrom.execute_script("document.body.style.zoom='40%'")
hrom.implicitly_wait(5)

naslov = hrom.find_element(By.NAME,"naslov")
naslov.send_keys("Zavrsni rad")

uvodni_tekst = hrom.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/div/form/fieldset[2]/textarea[1]")
uvodni_tekst.send_keys("Mihajlo Vasic")

teks = hrom.find_element(By.NAME,"tekst")
teks.send_keys("Potpis")

broj = hrom.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/div/form/fieldset[2]/textarea[3]")
broj.send_keys("1")
hrom.save_screenshot("novi_clanak_ispisan.png")

objavi_trazeno = "submit"
objavi = hrom.find_element(By.NAME,"submit")
hrom.execute_script("arguments[0].click();", objavi)
hrom.execute_script("document.body.style.zoom='40%'")
hrom.implicitly_wait(5)

svi_clanci = hrom.find_element(By.XPATH,"/html/body/nav/div/div[2]/div[2]/ul/li[3]/a")
hrom.execute_script("arguments[0].click();", svi_clanci)
hrom.execute_script("document.body.style.zoom='25%'")
hrom.save_screenshot("svi_clanci_1.png")
hrom.implicitly_wait(5)

zavrsni_rad = hrom.find_element(By.LINK_TEXT,"Zavrsni rad")
hrom.execute_script("arguments[0].click();", zavrsni_rad)
hrom.execute_script("document.body.style.zoom='40%'")
hrom.save_screenshot("delo.png")

brisanje_objave = hrom.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/div/form/fieldset[4]/input[2]")
hrom.execute_script("arguments[0].click();", brisanje_objave)
hrom.implicitly_wait(5)

logout_trazeno = "LogOut"
logout = hrom.find_element(By.XPATH,"/html/body/nav/div/div[2]/div[2]/ul/li[6]/a")
assert logout.text == logout_trazeno
hrom.save_screenshot("logout.png")
logout.click()
hrom.implicitly_wait(5)

pocetna_trazeno = "Početna"
pocetna = hrom.find_element(By.LINK_TEXT,"Početna")
assert pocetna_trazeno in pocetna.text
hrom.save_screenshot("pocetna_2.png")
pocetna.click()

time.sleep(10)