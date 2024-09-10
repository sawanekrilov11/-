import pytest
import requests
import allure
from config.settings import API_KEY
from config.settings import API_URL

HEADERS = {
    "X-API-KEY": API_KEY
}

@allure.step("Поиск рандомного фильма")
def test_random_movie():
    response = requests.get(f"{API_URL}movie/random", headers=HEADERS)
    assert response.status_code == 200
    assert 'id' in response.json()

@allure.step("Поиск фильма по ID")
def test_movie_by_id():
    movie_id = 2717
    response = requests.get(f"{API_URL}movie/{movie_id}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['id'] == movie_id

@allure.step("Поиск фильма по фильтрам")
def test_movies_by_filters():
    params = {"year": 2023, "genres.name": "криминал"}
    response = requests.get(f"{API_URL}movie", headers=HEADERS, params=params)
    assert response.status_code == 200
    assert len(response.json()['docs']) > 0

@allure.step("Поиск фильма с некорректным ID(Негативная проверка)")
def test_movie_with_invalid_id():
    movie_id = 99999999 
    response = requests.get(f"{API_URL}movie/{movie_id}", headers=HEADERS)
    assert response.status_code == 400

@allure.step("Поиск фильма с некорректным годом выпуска(Негативная проверка)")
def test_movie_with_invalid_year():
    params = {"year": 3000} 
    response = requests.get(f"{API_URL}movie", headers=HEADERS, params=params)
    assert response.status_code == 400
