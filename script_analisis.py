import pandas as pd

def analizar_ventas():
    df = pd.read_csv('data/BD_Ventas.csv')
    df['Total_Venta'] = df['Cantidad'] * df['Precio']

    print("========================================")
    print("      REPORTE DE ANÁLISIS DE VENTAS     ")
    print("========================================\n")
    print("--- Primeras Filas ---")
    print(df.head(), "\n")

    print("--- Resumen General ---")
    print(f"Total Unidades Vendidas: {df['Cantidad'].sum()}")
    print(f"Ingreso Total General:   ${df['Total_Venta'].sum():,.2f}\n")

    print("--- Ventas por Vendedor ---")
    print(df.groupby('Vendedor')['Total_Venta'].sum())

if __name__ == '__main__':
    analizar_ventas()