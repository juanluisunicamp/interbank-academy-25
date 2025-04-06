import argparse
import csv

#Detecta si el delimitador es ',' o ';' en el archivo CSV
def detectar_delimitador(archivo_csv):
    with open(archivo_csv, mode='r', encoding='utf-8-sig') as archivo:
        primera_linea = archivo.readline()
        if ';' in primera_linea:
            return ';'
        return ','

def procesar_transacciones(archivo_csv):
    balance               = 0
    transaccion_max_id    = ""
    transaccion_max_monto = float('-inf')
    creditos              = 0
    debitos               = 0

    try:
        # Detectar delimitador automáticamente
        delimitador = detectar_delimitador(archivo_csv)

        with open(archivo_csv, mode='r', encoding='utf-8-sig') as archivo:
            lector_csv = csv.reader(archivo, delimiter=delimitador)
            next(lector_csv) 

            for fila in lector_csv:
                id_transaccion, tipo, monto = fila[0], fila[1], float(fila[2])

                if tipo == "Crédito":
                    balance  += monto
                    creditos += 1
                elif tipo == "Débito":
                    balance -= monto
                    debitos += 1

                if monto > transaccion_max_monto:
                    transaccion_max_monto = monto
                    transaccion_max_id    = id_transaccion

        print("Reporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {balance:.2f}")
        print(f"Transacción de Mayor Monto: ID {transaccion_max_id} - {transaccion_max_monto:.2f}")
        print(f"Conteo de Transacciones: Crédito: {creditos} Débito: {debitos}")

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

def main():
    parser = argparse.ArgumentParser(description='Procesar un archivo CSV de transacciones bancarias.')
    parser.add_argument('archivo', help='Ruta del archivo CSV')

    args = parser.parse_args()
    procesar_transacciones(args.archivo)

if __name__ == '__main__':
    main()