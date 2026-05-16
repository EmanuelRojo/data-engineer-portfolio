import yfinance as yf
import pandas as pd
import os
from datetime import datetime
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def extraer_historial_forex(ticker="EURUSD=X", start_date="2024-01-01", end_date="2025-12-31"):
    """
    Función profesional para extraer datos de Forex.
    Incluye manejo de errores y columnas de auditoría para el Data Warehouse.
    """
    print(f"💱 [INGESTA] Conectando con Yahoo Finance para extraer {ticker}...")
    
    try:
        # Extraemos el bloque de datos de internet
        df_raw = yf.download(tickers=ticker, start=start_date, end=end_date, interval="1d")
        
        if df_raw.empty:
            print("⚠️ [ALERTA] La API no devolvió datos para este rango de fechas.")
            return None
            
        # 🧹 LIMPIEZA Y ESTRUCTURACIÓN DE DATOS (Data Wrangling)
        df = df_raw.reset_index()
        
        # Nos aseguramos de mapear las columnas correctas
        df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
        
        # METRICAS DE AUDITORÍA: Clave para cualquier Data Lake profesional
        df["par_divisas"] = ticker
        df["fecha_ejecucion"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df["usuario_sistema"] = "pipeline_bot"
        
        # Crear la carpeta de destino si por alguna razón no existe
        os.makedirs("ingestion", exist_ok=True)
        path_destino = "ingestion/datos_eurusd.csv"
        
        # Guardamos el dataset crudo
        df.to_csv(path_destino, index=False)
        print(f"✅ [ÉXITO] Archivo guardado localmente en: {path_destino}")
        print(f"📊 Dataset listo con {len(df)} filas y {len(df.columns)} columnas.")
        
        return df
        
    except Exception as e:
        print(f"❌ [ERROR CRÍTICO] Falló la ingesta de datos: {str(e)}")
        return None

if __name__ == "__main__":
    extraer_historial_forex()