from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from os import system as sys
option = Options()
driver = None


header = '''
/ ___|  ___  _   _ _ __   __| | ___| | ___  _   _  __| |
\___ \ / _ \| | | | '_ \ / _` |/ __| |/ _ \| | | |/ _` |
 ___) | (_) | |_| | | | | (_| | (__| | (_) | |_| | (_| |
|____/ \___/ \__,_|_| |_|\__,_|\___|_|\___/ \__,_|\__,_|

 ____  _
|  _ \| | __ _ _   _  ___ _ __
| |_) | |/ _` | | | |/ _ \ '__|
|  __/| | (_| | |_| |  __/ |
|_|   |_|\__,_|\__, |\___|_|
               |___/

Tarun Kumar | Python Bootcamp 2020

'''


def print_header():
    sys("clear")
    print(header)


def play_pause():
    play_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.sound__header div div div")))
    play_btn.click()


def search(q):
    search_bar = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div/div[2]/div/div[1]/span/span/form/input')
    search_bar.click()
    search_bar.send_keys(q.strip() + '\n')


def search_and_play():
    song_to_play = input("\n\nEnter the song you want to play: ")
    song_to_play = song_to_play.title()
    search(song_to_play)
    play_pause()
    play_pause_exit = 0
    while(play_pause_exit != 2):
        print(
            f"{'Playing' if play_pause_exit == 0 else 'Paused'} {song_to_play}, press P to {'pause' if play_pause_exit == 0 else 'play'} it")
        print('or enter X to exit the program')

        input_value = input()
        if input_value.lower() == 'p':
            play_pause()
            print_header()
            if play_pause_exit == 0:
                play_pause_exit = 1
            else:
                play_pause_exit = 0
        elif input_value.lower() == 'x':
            play_pause_exit = 2
        else:
            print_header()
    print("Exiting the program")


def initiate_browser():
    driver = webdriver.Chrome(options=option)
    driver.set_network_conditions(
        offline=False,
        latency=500,  # additional latency (ms)
        download_throughput=500 * 1024,  # maximal throughput
        upload_throughput=500 * 1024)  # maximal throughput
    return driver


def main():
    global driver
    print_header()
    driver = initiate_browser()
    driver.get("https://www.soundcloud.com")
    search_and_play()
    driver.quit()


if __name__ == "__main__":
    main()
