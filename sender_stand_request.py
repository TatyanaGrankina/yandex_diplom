import requests
import configuration

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

def get_order(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params=track_order)