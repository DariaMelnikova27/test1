import os
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import allure


@allure.step("Waiting for availability {url}")
def wait_url_data(url, timeout=10):
    """Метод ожидания доступности урла"""
    while timeout:
        response = requests.get(url)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if 'video' in url:
                return response.content
            else:
                return response.text
    return None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--executor", action="store", default="192.168.0.102")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")
    parser.addoption("--driver_folder", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--url", action="store", default="https://spb.ticketland.ru/")
    parser.addoption("--status_code", default="200", type=int)


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    driver_folder = request.config.getoption("--driver_folder")
    url = request.config.getoption("--url")

    if executor == "local":

        if browser == 'firefox' or browser == "ff":
            options = FirefoxOptions()
            driver = webdriver.Firefox(
                executable_path=f"{driver_folder}{os.sep}geckodriver", options=options
            )
        elif browser == "chrome":
            options = ChromeOptions()
            driver = webdriver.Chrome(
                options=options, executable_path=f"{driver_folder}{os.sep}chromedriver"
            )
        elif browser == "edge":
            options = EdgeOptions()
            driver = webdriver.Edge(
                executable_path=f"{driver_folder}{os.sep}msedgedriver", options=options
            )
        elif browser == "yandex":
            options = ChromeOptions()
            driver = webdriver.Chrome(
                executable_path=f"{driver_folder}{os.sep}yandexdriver", options=options
            )
        elif browser == "safari":
            driver = webdriver.Safari()

        driver.maximize_window()
        request.addfinalizer(driver.close)
        driver.get(url)
        driver.url = url
        return driver

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "selenoid:options": {
                "screenResolution": "1280x720",
                "name": "Daria",
                "enableVNC": vnc,
                "enableVideo": video,
                "enableLog": logs
            },
            'timeZone': 'Europe/Moscow',
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    def finalizer():
        log_url = f"{executor}/logs/{driver.session_id}.log"
        video_url = f"http://{executor}:8080/video/{driver.session_id}.mp4"
        driver.quit()

        if request.node.status != 'passed':
            if logs:
                allure.attach(
                    name="selenoid_log_" + driver.session_id,
                    body=wait_url_data(log_url),
                    attachment_type=allure.attachment_type.TEXT)
            if video:
                allure.attach(
                    body=wait_url_data(video_url),
                    name="video_for_" + driver.session_id,
                    attachment_type=allure.attachment_type.MP4)

        if video and wait_url_data(video_url):
            requests.delete(url=video_url)

        if logs and wait_url_data(log_url):
            requests.delete(url=log_url)

    request.addfinalizer(finalizer)
    driver.get(url)
    driver.url = url
    return driver