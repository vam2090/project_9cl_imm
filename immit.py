# Программа для генерации координат равномерного прямолинейного движения по начальной и конечной точкам


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
    dec_degs = [round((lat_deg + lat_min / 60), 4), round(lon_deg + lon_min / 60, 4)]
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

#def immit_roads(coords):

start = nmea_to_dec(get_coordinates("$GPRMC,120000.00,A,5647.2096,N,06029.7433,E,_,_,041026,,,A*7A 1")[1:])
end = nmea_to_dec(get_coordinates("$GPRMC,120010.00,A,5647.2930,N,06029.8964,E,_,_,041026,,,A*7A")[1:])


data = open("/home/vova/workspace/project_9cl_imm/data/immit_data.txt", "w")

data.write("$GPRMC,120000.00,A,5647.2096,N,06029.7433,E,_,_,041026,,,A*7A\n")

lat_step = (end[0] - start[0]) / 98
lon_step = (end[1] - start[1]) / 98

for i in range(98):
    lat, lon = dec_to_nmea([round(start[0] + lat_step * i, 6), round(start[1] + lon_step * i, 6)])
    data.write("$GPRMC,120000.00,A," + str(lat) + ",N," + str(lon) + ",E,_,_,041026,,,A*7A\n")

data.write("$GPRMC,120010.00,A,5647.2930,N,06029.8964,E,_,_,041026,,,A*7A\n")

print(start, end)
print(nmea_to_dec(start), nmea_to_dec(end))
print(dec_to_nmea(nmea_to_dec(start)), dec_to_nmea(nmea_to_dec(end)))