data = "$GPRMC,123519.00,A,5649.1234,N,06035.5678,E,000.1,234.5,041026,,,A*7A"

def get_coordinates(nmea_string):
    clean_nmea_string = nmea_string.lstrip('$').rstrip('*') # убираем лишние крайние символы
    nmea_list = clean_nmea_string.split(',') # превращаем в список, разделяя по запятым
    coordinates = [float(nmea_list[1]), float(nmea_list[3]), float(nmea_list[5])] 
    print(coordinates)

get_coordinates(data)