import pytest
from pages.main_page import MainPage
from data import EXPECTED_ANSWERS
import allure

@allure.title('''
Проверка соотвествия ответов в разделе "Вопросы о важном" на главной странице:
1. Последовательно кликаем на вопросы
2. Получаем текст ответа
3. Сравниваем с ожидаемым результатом
''')
class TestFAQ:
    
    @pytest.mark.parametrize("idx", EXPECTED_ANSWERS.keys())
    def test_faq_expected_answers(self, driver, idx):
        page = MainPage(driver)
        page.open_main()
        page.scroll_to_faq()         
        page.toggle_question(idx)
        page.wait_answer_visible(idx)
        
        actual_text = page.answer_text(idx)

        actual_text = " ".join(actual_text.split())
        expected_text = " ".join(EXPECTED_ANSWERS[idx].split())

        assert actual_text == expected_text, (
            f"\n Ошибка в ответе на вопрос {idx}\n"
            f"Ожидалось: {expected_text}\n"
            f"Получено: {actual_text}\n"
        )
