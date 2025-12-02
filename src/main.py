import requests
import re
import os
from PIL import Image
from io import BytesIO
import api_request as api
import image_getter as img


dict = {}


def save_comic(url):
    image_url = url
    # print(image_url)
    file_name = re.search(re.compile(r"[^/]+$"), image_url)
    file_name = image_url[file_name.start() : file_name.end()]
    # print(file_name)
    save_path = ".." + os.sep + "comics" + os.sep + file_name
    # since this is a relative path the previous line only works when executing the main file from the src folder
    img.download_image(image_url, save_path)
    return file_name


def save_dict():
    with open(".." + os.sep + "names.csv", "at") as f:
        f.write("sep=;\n")
        f.write(f"number; filename; safe title; transcript; alt text\n")
        for key, value in dict.items():
            f.write(f"{key};")
            for s in value:
                f.write(re.sub(r";", ",", re.sub(r"\n", " ", s)) + ";")
            f.write("\n")


def fill_dict(data, file_name):
    dict[data["num"]] = [file_name, data["safe_title"], data["transcript"], data["alt"]]


def download_and_add_to_dict(number):
    data = api.get_data_by_number(number)
    print(data)
    file_name = save_comic(api.get_image_path(data))
    fill_dict(data, file_name)


max = api.get_current_num()
# for i in range(1, 5):
# download_and_add_to_dict(120)
# save_dict()
for i in range(1, max + 1):
    if i % 10 == 0:
        print(i)
    try:
        data = api.get_data_by_number(i)
        fill_dict(data, save_comic(api.get_image_path(data)))
    except:
        print(f"ERROR at number {i}!")
        continue
# print(dict)
save_dict()
