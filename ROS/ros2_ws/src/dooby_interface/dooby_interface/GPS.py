from gps import *


def getPositionData():
    gpsd = gps(mode=WATCH_ENABLE)
    nx = gpsd.next()
    # For a list of all supported classes and fields refer to:
    # https://gpsd.gitlab.io/gpsd/gpsd_json.html
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
    return latitude, longitude

lat, lon = getPositionData()
print(lat)
print(lon)
