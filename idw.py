import numpy as np


def idw_method(latitude: float, longitude: float, sensors_locations: np.ndarray, values: list[float], p: int) -> float:
    nominator = []
    denominator = []
    for i in range(0, len(values)):
        dist = np.sqrt((latitude - sensors_locations[i][1]) ** 2 + (longitude - sensors_locations[i][2]) ** 2)
        if dist == 0:
            return values[i]
        else:
            wk = 1 / dist ** p
            weighted_value = wk * values[i]
            nominator.append(weighted_value)
            denominator.append(wk)
    return sum(nominator) / sum(denominator)
