import requests
import json


def get_data_by_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

    return data


def get_data_by_number(number):
    return get_data_by_url(f"https://xkcd.com/{number}/info.0.json")


def get_current_num():
    url = "https://xkcd.com/info.0.json"
    data = get_data_by_url(url)
    return data["num"]


def get_image_path(data):
    return data["img"]


if __name__ == "__main__":
    print("current number:" + get_current_num())
    print("filename of comic 5:" + get_image_path(5))
