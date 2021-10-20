from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import fixture


@fixture(scope='module')
def client():
    yield (browser := webdriver.Firefox())
    browser.quit()


def test_open_suckless(client):
    client.get('http://www.suckless.org')
    client.maximize_window()
    assert 'suckless.org' in client.title


def test_go_to_dwm(client):
    client.find_element(By.PARTIAL_LINK_TEXT, 'dwm').click()
    assert 'dwm' in client.title
    assert client.current_url == 'http://dwm.suckless.org/'
