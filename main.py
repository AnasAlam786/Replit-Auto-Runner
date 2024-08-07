import time
from selenium import webdriver
import pickle

def start():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    d = webdriver.Chrome(chrome_options=options)

    d.get("https://facebook.com")

    
    # First need to create cookies.pkl
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        d.add_cookie(cookie)

    d.get("https://replit.com/login")
    time.sleep(2)
    
    d.find_element_by_xpath('//*[@id="__next"]/div/div[2]/main/div/div[7]/div/div[3]/button/span/div').click()
    time.sleep(5)
    

    def run_repl(i):
        print(f"rerunning {i}")
        d.get(f"https://replit.com/@team94/a-{i}#main.py")
        time.sleep(5)
        try:
            d.find_element_by_xpath(
                "/html/body/reach-portal/div[2]/div/div/div[2]/div/div/div/div/div/button[1]"
            ).click()
        except:
            pass

        try:
            time.sleep(2)
            d.find_element_by_class_name("css-d8yyuf").click()
        except Exception as e:
            print(e)

        time.sleep(200)

    def check():
        for i in range(1, 12):

            try:
                d.get(f'https://a-{i}.team94.repl.co')
                time.sleep(10)
                text = d.find_element_by_xpath(
                    '/html/body/div/div[1]/div[2]/h1').text

                if "Repl Unavailable" in text:
                    print(f"{i} Paused {text}")
                    run_repl(i)

                elif "Run this Repl" in text:
                    print(f"{i} Paused {text}")
                    run_repl(i)

                elif "Unable" in text:
                    print(f"{i} Paused {text}")
                    run_repl(i)

                else:
                    print(f"{i} running...")

            except:
                print(f"{i} running...")

    while True:
        try:
            check()

        except Exception as e:
            print(e)



while True:
    try:
        start()
    except Exception as e:
        print(e)
