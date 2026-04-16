# Sales Data Analysis

Análisis de datos de ventas realizado con Python y Power BI para explorar tendencias, comportamiento de clientes, productos más vendidos y rendimiento por país.

## Overview

Este proyecto analiza un dataset de ventas online con el objetivo de extraer insights de negocio y presentarlos de forma clara mediante visualizaciones.  

El análisis fue desarrollado usando **Python** para limpieza y exploración de datos, y **Power BI** para la construcción de dashboards interactivos.

## Objectives

- Limpiar y preparar los datos para su análisis
- Explorar tendencias de ventas a lo largo del tiempo
- Identificar los países con mayores ventas
- Detectar los productos más vendidos
- Obtener insights útiles para la toma de decisiones comerciales

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- OpenPyXL
- Power BI
- Git & GitHub

## Dataset

El proyecto utiliza un dataset de ventas online que incluye información como:

- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

## Data Cleaning

Durante el proceso de preparación de datos se realizaron tareas como:

- Eliminación de valores nulos
- Eliminación de registros inválidos o cancelados
- Conversión de fechas
- Creación de métricas derivadas como `TotalSales`

## Analysis Performed

Se analizaron distintos aspectos del negocio, entre ellos:

- Evolución de ventas en el tiempo
- Ventas por país
- Productos más vendidos
- Comportamiento general del volumen de compras

## Visualizations

El proyecto incluye visualizaciones como:

- Línea de ventas por mes
- Barras de ventas por país
- Top productos por cantidad vendida
- Indicadores generales de desempeño

## Power BI Dashboard

Además del análisis en Python, se creó un dashboard en Power BI para presentar los resultados de forma visual e interactiva.

El dashboard permite:

- Explorar ventas por período
- Comparar países
- Analizar productos destacados
- Comunicar insights de negocio de manera clara

## Insight

Hay crecimiento de ventas en el tiempo (2010 → 2011), lo que sugiere una demanda en expansión.

Esto indica que el negocio mantiene un crecimiento sostenido sin grandes fluctuaciones, lo que es una señal positiva de estabilidad y previsibilidad en los ingresos.


###  Country Concentration Risk

La facturación está muy concentrada por país: United Kingdom lidera claramente, seguido de Japan y luego RSA; el resto aporta bastante menos.

La brecha entre el primer país y el resto es considerable, lo que indica una fuerte dependencia de un único mercado.

Esto implica:
- Riesgo si disminuye la demanda en UK
- Oportunidad de expansión en otros países
- Posible necesidad de estrategias de diversificación


###  Product Distribution (Top Products)

En productos, hay un top seller muy marcado (PAPER CRAFT , LITTLE BIRDIE) y luego un segundo grupo fuerte (MEDIUM CERAMIC TOP STORAGE JAR, etc.), este indicador es útil para priorizar stock y campañas.

Sugerencias:
- Priorizar stock de productos más demandados
- Optimizar campañas de marketing
- Detectar mejores patrones de consumo 

Este enfoque ayuda a enfocar recursos en los productos que generan mayor impacto en el negocio.

