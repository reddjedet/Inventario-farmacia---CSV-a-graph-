import pandas as pd
import matplotlib.pyplot as plt

# 1. Carga de datos desde un archivo local
try:
    df = pd.read_csv("ubicación del .csv")
    df["mes"] = df["mes"].str.strip()

    # 2. Gráfico de barras
    ventas_por_producto = (
        df.groupby("producto")["ventas"].sum().sort_values(ascending=False)
    )
    plt.figure(figsize=(8, 5))
    ventas_por_producto.plot(kind="bar", color="skyblue")
    plt.title("Ventas totales por producto")
    plt.xlabel("Producto")
    plt.ylabel("Cantidad de ventas (unidades)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # 3. Gráfico de líneas
    meses_orden = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]
    df["mes"] = pd.Categorical(df["mes"], categories=meses_orden, ordered=True)
    ventas_por_mes = (
        df.groupby("mes")["ventas"].sum().reindex(meses_orden, fill_value=0)
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    ventas_por_mes.plot(kind="line", marker="o", color="purple", ax=ax)
    plt.title("Ventas a lo largo del año")
    plt.xlabel("Mes")
    plt.ylabel("Cantidad de ventas (unidades)")
    plt.grid(True)

    # SOLUCIÓN: Usar la función set_xticks para mostrar todas las etiquetas de los meses
    ax.set_xticks(range(len(meses_orden)))
    ax.set_xticklabels(meses_orden, rotation=90)

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: El archivo 'hoja1.csv' no se encuentra en la ruta especificada.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
