"""
Базовые тесты
"""
import pytest
import allure
import time


@allure.epic("Basic Tests")
@allure.feature("Simple Operations")
class TestBasicOperations:
    """Базовые тесты для демонстрации"""
    
    @allure.story("Математические операции")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_addition(self):
        """Тест сложения"""
        with allure.step("Сложение двух чисел"):
            result = 2 + 2
            assert result == 4
    
    @allure.story("Математические операции")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_multiplication(self):
        """Тест умножения"""
        with allure.step("Умножение двух чисел"):
            result = 3 * 4
            assert result == 12
    
    @allure.story("Работа со строками")
    @allure.severity(allure.severity_level.MINOR)
    def test_string_operations(self):
        """Тест операций со строками"""
        with allure.step("Проверка конкатенации строк"):
            result = "Hello" + " " + "World"
            assert result == "Hello World"
        
        with allure.step("Проверка длины строки"):
            assert len(result) == 11
    
    @allure.story("Работа со списками")
    @allure.severity(allure.severity_level.MINOR)
    def test_list_operations(self):
        """Тест операций со списками"""
        with allure.step("Создание списка"):
            test_list = [1, 2, 3, 4, 5]
            assert len(test_list) == 5
        
        with allure.step("Добавление элемента"):
            test_list.append(6)
            assert len(test_list) == 6
            assert test_list[-1] == 6


@allure.epic("Basic Tests")
@allure.feature("Performance Tests")
class TestPerformance:
    """Тесты производительности"""
    
    @allure.story("Проверка времени выполнения")
    @allure.severity(allure.severity_level.NORMAL)
    def test_fast_operation(self):
        """Быстрая операция"""
        start = time.time()
        result = sum(range(1000))
        duration = time.time() - start
        
        allure.attach(
            f"Время выполнения: {duration:.4f} секунд",
            name="Performance",
            attachment_type=allure.attachment_type.TEXT
        )
        
        assert result == 499500
        assert duration < 0.1, "Операция слишком медленная"

