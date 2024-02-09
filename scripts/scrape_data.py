import requests

def get_dolar_values():
    url = "https://dolarapi.com/v1/dolares"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the response

        data = response.json()

        table = "\`\`\`Markdown\n| Casa                    | Compra    | Venta     | Fecha de Actualización       |\n|-------------------------|-----------|-----------|------------------------------|\n"

        for entry in data:
            casa = entry.get("nombre")
            compra = entry.get("compra")
            venta = entry.get("venta")
            fecha_actualizacion = entry.get("fechaActualizacion")

            # Add each row to the table
            table += f"| {casa:<24} | {compra:<9} | {venta:<9} | {fecha_actualizacion:<28} |\n"

        table += "\`\`\`"
        return table

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return "Unable to fetch Dolar values."

if __name__ == "__main__":
    data = get_dolar_values()

    # Now, you can use 'data' as needed, such as sending it to Discord
    print(data)