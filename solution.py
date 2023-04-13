import numpy as np
from scipy.stats import ks_2samp


chat_id = 753540521 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    ks_stat, p_value = ks_2samp(x, y)
    alpha = 0.07
    critical_value = np.sqrt(-0.5 * np.log(alpha / 2)) / np.sqrt(len(x) + len(y))

    if ks_stat > critical_value:
        return True
    else:
        return False
