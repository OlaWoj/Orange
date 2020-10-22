from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    wd = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    wd.get("https://www.orange.pl/")

    def close_driver():
        wd.quit()

    request.addfinalizer(close_driver)
    return wd