# Татьяна Гранкина, 24-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def get_track_order(order_response):
    return order_response.json().get("track")

def positive_assert(order_body):
    # Выполнить запрос на создание заказа
    order_response = sender_stand_request.post_new_order(order_body)
    track = data.params_get.copy()
    # Сохранить номер трека заказа
    track["t"] = get_track_order(order_response)
    # Выполнить запрос на получения заказа по треку заказа
    track_response = sender_stand_request.get_order(track)
    # Проверяется, что код ответа равен 200
    assert track_response.status_code == 200

def test_order():
    positive_assert(data.order_body)