from abc import ABC, abstractclassmethod
import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    InvalidSelectorException,
    NoSuchElementException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
)
from webdriver_manager.chrome import ChromeDriverManager

from pynput import keyboard


class BaseCrawler(ABC):
    SHORT_BREAK = 0.5

    def __init__(self, driver: WebDriver = None) -> None:
        if driver is None:
            self.driver: WebDriver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install(),
                )
            )
            self.driver.implicitly_wait(2)
        else:
            self.driver: WebDriver = driver

    def sleep(self, secs=None):
        if secs is None:
            secs = self.SHORT_BREAK
        time.sleep(secs)

    def scroll_to(self, bottom=200, top=None, smooth=True):
        if top is None:
            top_str = f"window.innerHeight - {bottom}"
        else:
            top_str = f"{top}"

        self.driver.execute_script(
            f"""
            window.scrollTo({{
                top: {top_str},
                {"behavior: 'smooth'," if smooth else ""}
            }})
            """
        )

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_el(self, el, smooth=True):
        window_h = self.driver.get_window_size()["height"]
        y = el.location["y"]

        top = y - int(window_h / 2)
        self.scroll_to(top=top, smooth=smooth)

    def scroll_from_top(self, top=400):
        self.scroll_to(top=0)
        self.sleep()
        self.scroll_to(top=top)
        self.sleep()

    def click(self, el, smooth=True, delay=True):
        self.scroll_to_el(el, smooth=smooth)
        if delay:
            if not smooth:
                self.sleep(0.3)
            else:
                self.sleep(0.7)
        el.click()
        if delay:
            self.sleep()

    def send_keys(self, el, value: str):
        self.scroll_to_el(el)
        self.sleep()
        el.send_keys(value)


class BaseCrawlerApp(ABC):
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_extension("./buster.crx")
        self.driver: WebDriver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install(),
            ),
            options=options,
        )
        # self.driver.implicitly_wait(2)
        self.crawler = BaseCrawler(driver=self.driver)

        self.is_command_down = False
        self.is_end = False
        self.is_paused = False
        self.ogloszenie = None

        # CMD/CTRL + SPACE = is_paused -> True
        # F4 = is_end -> True
        self._init_keyboard()

    def __on_press(self, key):
        if key == keyboard.Key.cmd or key == keyboard.Key.ctrl:
            self.is_command_down = True
        elif key == keyboard.Key.space:
            if self.is_command_down:
                self.is_paused = False

    def __on_release(self, key):
        if key == keyboard.Key.f4:
            # Stop listener
            self.is_end = True
            return False
        elif key == keyboard.Key.cmd or key == keyboard.Key.ctrl:
            self.is_command_down = False

    def _init_keyboard(self):
        # Collect events until released
        # with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        #     listener.join()

        listener = keyboard.Listener(
            on_press=self.__on_press, on_release=self.__on_release
        )
        listener.start()

    def pause(self):
        self.is_paused = True
