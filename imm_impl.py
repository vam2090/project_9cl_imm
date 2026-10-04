data = "$GPRMC,123519.00,A,5649.1234,N,06035.5678,E,000.1,234.5,041026,,,A*7A"

# Функция получения координат по протоколу NMEA.
# Входные параметры: nmea_string - строка в формате NMEA.
# Выходные параметры: coordinates - массив чисел: время, долгота и широта.

def get_coordinates(nmea_str):
    clean_nmea_str = nmea_str.lstrip('$').rstrip('*') # убираем лишние крайние символы
    nmea_list = clean_nmea_str.split(',') # превращаем в список, разделяя по запятым
    coordinates = [float(nmea_list[1]), float(nmea_list[3]), float(nmea_list[5])] 
    return coordinates

coordinates = get_coordinates(data)
print(coordinates)