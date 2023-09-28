"""
У нас есть класс BaseResponse, который только работает с контентом, но он не умеет генерировать headers.
Нужно создать свой кастомный класс ответа, который сможет это делать


Задания:
    1. Создайте класс CustomResponse, который будет наследником и от BaseResponse и от BaseHeadersMixin
    2. Переопределите в нем метод generate_headers, таким образом, чтобы в базовые headers
       еще добавлялся header Content-Length, значение у которого - байтовая длинна контента. Используйте super()
       для этого
    3. Создайте экземпляр класса CustomResponse и вызовите у него метод generate_headers, все ли хэдэры теперь на месте.
"""


from typing import Mapping


class BaseResponse:
    def __init__(self, content: str) -> None:
        self.content = content

    def get_byte_content_length(self) -> str:
        return len(self.content.encode('utf-8'))


class BaseHeadersMixin:
    def generate_base_headers(self) -> Mapping[str, str]:
        return {
            'Content-Type': 'application/x-www-form-urlencoded',
            'user-agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
            ),
        }

    def generate_headers(self) -> Mapping[str, str]:
        return self.generate_base_headers()


class CustomResponse(BaseResponse, BaseHeadersMixin):
    def generate_headers(self) -> Mapping[str, str]:
        custom_headers = super().generate_headers()
        custom_headers.update({
            "Content-Length": self.get_byte_content_length()
        })
        return custom_headers


if __name__ == '__main__':
    custom_response = CustomResponse(content='Hello, World!')
    print(custom_response.content)
    print(custom_response.generate_headers())
