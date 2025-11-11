"""
Тесты для проверки API
"""
import pytest
import requests
import allure


@allure.epic("API Testing")
@allure.feature("Nomerogram API")
class TestNomerogramAPI:
    """Тесты для API Nomerogram"""
    
    BASE_URL = "https://api.nomerogram.ru"
    
    @allure.story("Проверка работоспособности API")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("api,method", [
        ("fssp", "physical"),
        ("fssp", "legal"),
    ])
    def test_check_api_performance(self, api, method):
        """Проверка работоспособности API и метода"""
        with allure.step(f"Проверка работоспособности API {api} метод {method}"):
            url = f"{self.BASE_URL}/{api}/{method}"
            
            with allure.step("Отправка запроса"):
                response = requests.get(url, timeout=10)
                
                allure.attach(
                    f"Request URL: {url}",
                    name="Request URL",
                    attachment_type=allure.attachment_type.TEXT
                )
                allure.attach(
                    str(response.headers),
                    name="Response Headers",
                    attachment_type=allure.attachment_type.TEXT
                )
                allure.attach(
                    str(response.status_code),
                    name="Response Status Code",
                    attachment_type=allure.attachment_type.TEXT
                )
                
            with allure.step("Проверка статус кода"):
                assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
            
            with allure.step("Проверка наличия поля performance"):
                data = response.json()
                assert "performance" in data, "Поле performance отсутствует в ответе"
                
                allure.attach(
                    str(data),
                    name="Response Body",
                    attachment_type=allure.attachment_type.JSON
                )
            
            with allure.step("Проверка, что API работает"):
                assert data.get("performance") is not None, "Performance не может быть None"
    
    @allure.story("Проверка доступности сервиса")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_api_health_check(self):
        """Проверка доступности API"""
        with allure.step("Проверка доступности API"):
            response = requests.get(f"{self.BASE_URL}/health", timeout=5)
            assert response.status_code in [200, 404], "API недоступен"


@allure.epic("API Testing")
@allure.feature("Simple API Tests")
class TestSimpleAPI:
    """Простые тесты API"""
    
    @allure.story("Проверка HTTP методов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_http_get(self):
        """Проверка GET запроса"""
        with allure.step("Выполнение GET запроса"):
            response = requests.get("https://httpbin.org/get", timeout=5)
            assert response.status_code == 200
    
    @allure.story("Проверка HTTP методов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_http_post(self):
        """Проверка POST запроса"""
        with allure.step("Выполнение POST запроса"):
            data = {"test": "value"}
            response = requests.post("https://httpbin.org/post", json=data, timeout=5)
            assert response.status_code == 200
            result = response.json()
            assert result["json"]["test"] == "value"

