config = open("./data/bike_path.txt", "r")
bike_path = [list(map(float, pair.split(','))) for pair in config.readline().split()]
# Функция получения координат по протоколу NMEA.
# Входные параметры: nmea_string - строка в формате NMEA.
# Выходные параметры: coordinates - массив чисел: время, широта и долгота.

def get_coordinates(nmea_str):
    clean_nmea_str = nmea_str.lstrip('$').rstrip('*') # убираем лишние крайние символы
    nmea_list = clean_nmea_str.split(',') # превращаем в список, разделяя по запятым
    coordinates = [float(nmea_list[1]), float(nmea_list[3]), float(nmea_list[5])] 
    return coordinates


# Функция переводит градусы в формате NMEA (ГГММ.ММММ) в десятичный формат (ГГ.ГГГГГГ)
# Входные данные: массив с широтой и долготой в градусах в формате NMEA
# Выходные данные: массив с широтой и долготой в градусах в десятичном формате

def nmea_to_dec(nmea_degs):
    lat_deg = nmea_degs[0] // 100
    lat_min = nmea_degs[0] % 100
    lon_deg = nmea_degs[1] // 100
    lon_min = nmea_degs[1] % 100
    dec_degs = [round((lat_deg + lat_min / 60), 8), round(lon_deg + lon_min / 60, 8)]
    return dec_degs


# Функция переводит градусы в десятичном формате (ГГ.ГГГГГГ) в формат NMEA (ГГММ.ММММ)
# Входные данные: массив с широтой и долготой в градусах в десятичном формате
# Выходные данные: массив с широтой и долготой в градусах в формате NMEA

def dec_to_nmea(dec_degs):
    lat_deg = int(dec_degs[0])
    lat_min = (dec_degs[0] - lat_deg) * 60
    lon_deg = int(dec_degs[1])
    lon_min = (dec_degs[1] - lon_deg) * 60
    nmea_degs = [f"{lat_deg:02d}{lat_min:7.4f}", f"{lon_deg:03d}{lon_min:7.4f}"]
    return nmea_degs


# Функция определяет, находится ли точка на данных координатах внутри четырёхугольника с вершинами в данных координатах
# Входные данные: массив с координатами точки, массив с массивами с координатами каждой вершины четырёхугольника
# Выходные данные: булево значение True, если точка находится внутри четырёхугольника и False, если точка находится за его пределами

def point_in_quad(point, quad):
  px, py = point
  signs = []
  for i in range(4):
    x1, y1 = quad[i]
    x2, y2 = quad[(i + 1) % 4]
    cross_product = (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)
    signs.append(cross_product)
  has_positive = any(s > 1e-9 for s in signs)
  has_negative = any(s < -1e-9 for s in signs)

  return not (has_positive and has_negative)

def main():
    with open("./data/immit_data.txt", "r") as file:
        for i in range(100):
            coords = get_coordinates(file.readline())[1:]
            coords = nmea_to_dec(coords)
            if point_in_quad(coords, bike_path):
                print("СИМ находится в разрешённой зоне")
            else:
                print("СИМ находится в запрещённой зоне")

main()