import pandas as pd
import numpy as np


chat_id = 436734951 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.03
    res = anderson_ksamp([x, y])
    return res.pvalue < alpha # Ваш ответ, True или False
