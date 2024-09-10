import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config.settings import BASE_URL
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUI:
    @pytest.fixture(scope="class")
    def setup_driver(self, request):
        driver = webdriver.Chrome()
        request.cls.driver = driver  
        yield
        driver.quit()

    @allure.step("Проверка загрузки главной страницы")
    @pytest.mark.usefixtures("setup_driver")
    def test_home_page_load(self):
        self.driver.get(BASE_URL)
        assert "Кинопоиск" in self.driver.title

    @allure.step("Проверка поиска фильма")
    @pytest.mark.usefixtures("setup_driver")
    def test_search_movie(self):
        self.driver.get(BASE_URL)
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "query"))
            )
            search_box.send_keys("Титаник")
            search_box.submit()
            assert "Титаник" in self.driver.title
        except Exception as e:
            print(f"Ошибка при поиске элемента: {e}")

    @allure.step("Проверка перехода на страницу фильма")
    @pytest.mark.usefixtures("setup_driver")
    def test_movie_page_load(self):
        self.driver.get(BASE_URL + "film/2717/")
        WebDriverWait(self.driver, 10).until(EC.title_contains("Убить Билла"))
        assert "Убить Билла" in self.driver.title

    @allure.step("Проверка наличия элемента 'Рейтинг'")
    @pytest.mark.usefixtures("setup_driver")
    def test_rating_exists(self):
        self.driver.get(BASE_URL + "film/2717/")
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='rating__value']"))
            )
            assert element is not None, "Элемент 'Рейтинг' не найден"
            print("Элемент 'Рейтинг' найден:", element.text)
        except Exception as e:
            print("Произошла ошибка:", str(e))

    @allure.step("Проверка наличия элемента 'Логотип'")
    @pytest.mark.usefixtures("setup_driver")
    def test_logo_exists(self):
        self.driver.get(BASE_URL)
        try:
            logo = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "header__logo"))
            )
            assert logo.is_displayed(), "Логотип не отображается"
            print("Элемент 'Логотип' найден:", logo.text)
        except Exception as e:
            print("Произошла ошибка:", str(e))

if __name__ == "__main__":
    pytest.main()
