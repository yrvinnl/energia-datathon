import pandas as pd 

def transformar_columnas(df):
    # Convertir fechas desde formato entero YYYYMMDD
    df["FECHA_CORTE"] = pd.to_datetime(df["FECHA_CORTE"].astype(str), format="%Y%m%d", errors="coerce")
    df["FECHA_EMISION"] = pd.to_datetime(df["FECHA_EMISION"].astype(str), format="%Y%m%d", errors="coerce")
    df["FECPUESTASERVICIO"] = pd.to_datetime(df["FECPUESTASERVICIO"], errors="coerce", dayfirst=True)

    # Convertir columnas categóricas para optimizar memoria y análisis
    df["CODEMP"] = df["CODEMP"].astype("category")
    df["DESCRIPCION_PASTORAL"] = df["DESCRIPCION_PASTORAL"].astype("category")
    df["PROPIEDAD"] = df["PROPIEDAD"].astype("category")
    df["SECTOR"] = df["SECTOR"].astype("category")
    df["COD_SISTEMA_ELECTRICO"] = df["COD_SISTEMA_ELECTRICO"].astype("category")
    df["NOMBRE_SISTEMA_ELECTRICO"] = df["NOMBRE_SISTEMA_ELECTRICO"].astype("category")
    df["ALIMENTADOR"] = df["ALIMENTADOR"].astype("category")
    df["SUBESTACION"] = df["SUBESTACION"].astype("category")

    # Convertir códigos únicos a string para evitar ambigüedad
    df["CODLUMINARIA"] = df["CODLUMINARIA"].astype("string")
    df["CODTRAMOBT"] = df["CODTRAMOBT"].astype("string")
    df["CODTRAMOVIA"] = df["CODTRAMOVIA"].astype("string")

    return df

def antiguamiento_luminarias(df):
    df["ANTIGUEDAD"] = ((df["FECHA_CORTE"] - df["FECPUESTASERVICIO"]).dt.days / 365.25).astype(int).round(1)
    # Filtrar luminarias con antigüedad mayor a cero
    df_filtrado = df[df["ANTIGUEDAD"] > 0].copy()
   
    return df_filtrado