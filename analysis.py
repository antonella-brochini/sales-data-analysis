import pandas as pd

# 1. Cargar archivo
df = pd.read_excel("Online Retail.xlsx")

# 2. Ver columnas y tipos
print(df.columns)
print(df.dtypes)

# 3. Limpiar nombres de columnas por si tienen espacios
df.columns = df.columns.str.strip()

# 4. Convertir Quantity y UnitPrice a numéricos correctamente
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")

# 5. Eliminar filas nulas en campos clave
df = df.dropna(subset=["Quantity", "UnitPrice", "Country"])

# 6. Filtrar valores válidos
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

# 7. Recalcular Revenue desde cero
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# 8. Verificar resultados
print(df[["Quantity", "UnitPrice", "Revenue"]].head(10))
print("Revenue total:", df["Revenue"].sum())

# 9. Guardar archivo limpio
df.to_excel("Online_Retail_Clean.xlsx", index=False)

print("Archivo limpio guardado como Online_Retail_Clean.xlsx")