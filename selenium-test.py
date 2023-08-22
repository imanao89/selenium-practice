from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# google検索
def google_search(driver, keyword):
    driver.get('https://www.google.co.jp/')
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    search_box.submit()

    sleep(5)

if __name__ == "__main__":
    # WebDriver のオプションを設定する
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    search_term = input("Googleで検索するキーワードを入力してください: ")
    print('connectiong to remote browser...')
    with webdriver.Chrome(options=options) as driver:
        google_search(driver, search_term)

        # タイトルに「selenium」が含まれることを確認する。
        assert 'selenium' in driver.title
        # ブラウザを終了する。
        driver.quit()


