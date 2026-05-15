import yfinance as yf
import pandas as pd
from datetime import datetime

def extraer_forex_eurusd():
    print("💱 Conectando con Yahoo Finance para extraer historial 2024-2025...")
    
    ticker = "EURUSD=X"
    
    # Fijamos el rango exacto de fechas para agarrar los dos años enteros
    df_historico = yf.download(tickers=ticker, start="2024-01-01", end="2025-12-31", interval="1d")
    
    if not df_historico.empty:
        df = df_historico.reset_index()
        
        # Limpiamos las columnas para quedarnos con lo importante
        df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
        df["extraido_en"] = datetime.now()
        
        # Guardamos el CSV local con los dos años completos
        df.to_csv("ingestion/datos_eurusd.csv", index=False)
        
        print(f"✅ ¡Datos históricos extraídos con éxito!")
        print(f"📊 Total de días de mercado guardados: {len(df)} filas.")
        print("\n⏳ Primeros días del 2024:")
        print(df.head(3))
        print("\n⏳ Últimos días del 2025:")
        print(df.tail(3))
        return df
    else:
        print("❌ No se pudieron obtener datos. Revisá las fechas o la conexión.")
        return None

if __name__ == "__main__":
    extraer_forex_eurusd()


