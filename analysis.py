import pandas as pd

# ========================
# 1. Cargar datos
# ========================
df = pd.read_excel("Online Retail.xlsx")

# ========================
# 2. Limpieza de datos
# ========================
# Eliminar filas sin CustomerID
df = df.dropna(subset=["CustomerID"])

# Eliminar devoluciones (Quantity negativas)
df = df[df["Quantity"] > 0]

# ========================
# 3. Crear métricas base
# ========================
# Revenue (ventas)
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# ========================
# 4. Trabajar con fechas
# ========================
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["Date"] = df["InvoiceDate"].dt.date

# ========================
# 5. KPIs de negocio
# ========================
total_revenue = df["Revenue"].sum()
total_orders = df["InvoiceNo"].nunique()
avg_order_value = df.groupby("InvoiceNo")["Revenue"].sum().mean()
unique_customers = df["CustomerID"].nunique()

print("\n--- KPIs ---")
print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Average Order Value:", avg_order_value)
print("Unique Customers:", unique_customers)

# ========================
# 6. Análisis
# ========================
sales_by_country = df.groupby("Country")["Revenue"].sum().reset_index()
sales_by_date = df.groupby("Date")["Revenue"].sum().reset_index()
top_products = df.groupby("Description")["Quantity"].sum().reset_index()

# ========================
# 7. Exportar para Power BI
# ========================
df.to_csv("clean_data.csv", index=False)
sales_by_country.to_csv("sales_by_country.csv", index=False)
sales_by_date.to_csv("sales_by_date.csv", index=False)
top_products.to_csv("top_products.csv", index=False)

print("\nArchivos generados correctamente")
