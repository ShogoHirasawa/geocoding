import requests

def get_coordinates_and_osm_url(location_name):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location_name,
        "format": "json",
        "limit": 1
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()

    if data:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        osm_url = f"https://www.openstreetmap.org/?mlat={latitude}&mlon={longitude}#map=16/{latitude}/{longitude}"
        return latitude, longitude, osm_url
    else:
        return None, None, None

if __name__ == "__main__":
    location_name = input("Enter the location name: ")
    lat, lon, osm_url = get_coordinates_and_osm_url(location_name)
    
    if lat and lon and osm_url:
        print(f"Coordinates for {location_name}: Latitude: {lat}, Longitude: {lon}")
        print(f"OSM URL: {osm_url}")
    else:
        print(f"No coordinates or OSM URL found for {location_name}.")