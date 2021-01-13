import numpy as np
import cv2
import utils
import requests
import shutil
import time

FILE_NAME = "trained.npz"

with np.load(FILE_NAME) as data:
    train = data['train']
    train_labels = data['train_labels']

knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

def check(test, train, train_labels):
    ret, result, neighbours, dist = knn.findNearest(test, k=1)
    return result

def get_result(file_name):
    image = cv2.imread(file_name)
    chars = utils.extract_chars(image)
    result_string = ""

    for char in chars:
        matched = check(utils.resize20(char[1]), train, train_labels)

        if matched < 10:
            result_string += str(int(matched))
            continue
        if matched == 10:
            matched = "+"
        elif matched == 11:
            matched = "-"
        elif matched == 12:
            matched = "*"
        result_string += matched
    return result_string

print(get_result("2.png"))

host = "http://localhost:10000"
url = '/start'

with requests.Session() as s:
    answer = ''
    for i in range(0, 100):
        start_time = time.time()
        params = {'ans': answer}