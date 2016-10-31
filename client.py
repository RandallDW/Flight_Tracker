from geopy.geocoders import Nominatim

"""
__author__ = "Sheng Wei, Xuanyu Duan, Dong Wang, Sheila Zhu"
__copyright__ = "Copyright 2016, client"
__credits__ = ["Sheng Wei", "Xuanyu Duan", "Dong Wang",
                    "Sheila Zhu"]
__version__ = "1.0.0"
"""

"""
    Args:
        location_add(str): location address
    Returns:
		(location.latitude, location.longitude)(tuple):
				insert location's latitude and longitude
"""
def getLocation(location_add):
	geolocator = Nominatim()
	location = geolocator.geocode(location_add)
	return (location.latitude, location.longitude)



if __name__ == "__main__":
	print(getLocation('Blacksburg, VA'))

