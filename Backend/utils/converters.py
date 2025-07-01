
from geopy.geocoders import Nominatim

def get_coords_from_city(cidade_str: str) -> tuple | None:
    """Converte o nome de uma cidade em coordenadas lat/lon."""
    try:
        geolocator = Nominatim(user_agent="projeto_horoscopo_ia_gezebot")
        print(f"Buscando coordenadas para '{cidade_str}'...")
        location = geolocator.geocode(cidade_str)
        
        if location:
            return (location.latitude, location.longitude)
        else:
            print("Localização não encontrada.")
            return None
    except Exception as e:
        print(f"Ocorreu um erro na geocodificação: {e}")
        return None