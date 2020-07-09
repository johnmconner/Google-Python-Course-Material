import geoip2.database
import folium as f
from pygtail import Pygtail

reader = geoip2.database.Reader(r'C:\Users\John\Python\Attack Map\python\Geolite2-City.mmdb')


def get_LL(IP):
    response = reader.city(IP)
    LL = [response.location.latitude, response.location.longitude]
    return LL


def get_location_IP():
    ip_list = []
    for line in Pygtail(r'C:\Users\John\Python\Attack Map\python\logstash-IP.log'):
        ip_list.append(line.strip('\n'))
    return ip_list

def gen_map():
    map = f.Map(location=[38,-77])
    return map

def add_marker(map, ip_list):
    for IP in ip_list:
        f.Marker(get_LL(IP), popup=IP).add_to(map)
    map.save('map1.html')

map = gen_map()
ip_list = get_location_IP()
add_marker(map, ip_list)


