import requests
import json

def extraer_datos_cripto():
    # URL de la API pública de CoinGecko
    url = "https://coingecko.com"
    
    print("🚀 Conectando con la API de CoinGecko...")
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        print("✅ Datos extraídos con éxito:")
        print(json.dumps(datos, indent=4))
    else:
        print(f"❌ Error al conectar con la API: {respuesta.status_code}")

if __name__ == "__main__":
    extraer_datos_cripto()
