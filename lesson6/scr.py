import xml.etree.ElementTree as ET
import math
from array import array

class GPSPoint:
    def __init__(self, lat, lon):
        self._lat = lat
        self._lon = lon

    def get_latitude(self):
        return self._lat

    def get_longitude(self):
        return self._lon

    def set_latitude(self, lat):
        self._lat = lat

    def set_longitude(self, lon):
        self._lon = lon

    latitude = property(get_latitude, set_latitude)
    longitude = property(get_longitude, set_longitude)

    def __str__(self):
        return "({}, {})".format(self._lat, self._lon)

class LocationManager:
    def __init__(self):
        self.locations = []

    def add_location(self,points):
        self.locations.insert(len(self.locations),points)

    @staticmethod
    def get_distance(gps1,gps2):
        R = 6371000; # metres
        φ1 = gps1.get_latitude() * math.pi/180; # φ, λ in radians
        φ2 = gps2.get_latitude() * math.pi/180;
        Δφ = (gps2.get_latitude()-gps1.get_latitude()) * math.pi/180;
        Δλ = (gps2.get_longitude()-gps1.get_longitude()) * math.pi/180;
        a = math.sin(Δφ/2) * math.sin(Δφ/2) + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ/2) * math.sin(Δλ/2);
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));

        distance = (R * c)/1000; # in metres
        return distance


    def create_gpx(self,filename): 
        root = ET.Element("gpx")
        root.set("version","1.1")
        root.tail = "\n"
        trk = ET.SubElement(root,"trk")
        trk.tail = "\n"
        name = ET.SubElement(trk,"name")
       
        name.tail = "\n"
        name.text = "Path"
 
        trkseg = ET.SubElement(trk,"trkseg")
        trkseg.tail = "\n"
        for location in self.locations:
            trkpt = ET.SubElement(trkseg,"trkpt")
            trkpt.set("lat",str(location[0]))
            trkpt.set("lon",str(location[1]))
            trkpt.tail = "\n"
        tree = ET.ElementTree(root)
        tree.write(filename,encoding="utf-8",xml_declaration=True)


manager = LocationManager()
gps_point1 = GPSPoint(49.8813139647,18.519038558)
gps_point2 = GPSPoint(49.8528778553,18.553199172)

filename = "locations.dat"
temp_list = []
new_list = []
with open(filename, "rb") as f:
            arr = array('f')
            arr.frombytes(f.read())
            for i, k in zip(arr[0::2], arr[1::2]):
                manager.add_location([i, k])
distance_sum = 0
counter = 0
for point in range(len(manager.locations)-1):
    gps_point1 = GPSPoint(manager.locations[counter][0],manager.locations[counter][1])
    gps_point2 = GPSPoint(manager.locations[counter+1][0],manager.locations[counter+1][1])
    distance_sum += manager.get_distance(gps_point1,gps_point2)
    counter += 1
print(distance_sum)
manager.create_gpx("map.gpx")




