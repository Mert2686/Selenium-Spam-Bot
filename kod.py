from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

username = "mrtcn_26_86"#input("\nGirilcek Hesabın Kullanıcı adı: ")
şifre = "HeLyUm25_70"
hedef_hesap = "gaffar_krt"
nah = "biticen ulAN"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com/?hl=tr")
sleep(4)
user = driver.find_element_by_name("username")
user.send_keys(username)
password = driver.find_element_by_name("password")
password.send_keys(şifre)
sleep(1)
giriş_buton = driver.find_element_by_xpath("//div[@class='                     Igw0E     IwRSH      eGOV_         _4EzTm    bkEs3                          CovQj                  jKUp7          DhRcB                                                    ']")
giriş_buton.click()
sleep(5)
şimdi_değil1 = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
şimdi_değil1.click()
sleep(4)
şimdi_değil2 = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
şimdi_değil2.click()
sleep(3)
arama_kutusu = driver.find_element_by_xpath("//div[@class='eyXLr wUAXj ']")
arama_kutusu.click()
sleep(2)
ara3 = driver.find_element_by_xpath('//input[@type="text"]')
ara3.send_keys(hedef_hesap)
sleep(2)
hedef_tıkla = driver.find_element_by_xpath("//div[@class='z556c']")
hedef_tıkla.click()
sleep(5)
foto_tıkla = driver.find_element_by_xpath("//div[@class='_9AhH0']")
foto_tıkla.click()
sleep(2)

for atak in nah:
            üç_nokta = driver.find_element_by_xpath("//div[@style='height: 24px; width: 24px;']")
            üç_nokta.click()
            sleep(2)
            şikayet = driver.find_element_by_xpath("//button[contains(text(), 'Şikayet Et')]")
            şikayet.click()
            sleep(2)
            spam = driver.find_element_by_xpath("//div[@class='                  fXpnZ      rBNOH        eGOV_     ybXk5    _4EzTm                                                                                   XfCBB            g6RW6               ']")
            spam.click()
            sleep(1)
            spam_kapat = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
            spam_kapat.click()
            sleep(3)
            diğer_foto = driver.find_element_by_xpath("//a[@class=' _65Bje  coreSpriteRightPaginationArrow']")
            diğer_foto.click()
                
