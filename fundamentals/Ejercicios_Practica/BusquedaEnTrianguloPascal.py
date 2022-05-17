def pascal(row, column):
    if row < 0 and column < 0:
        return 0
    elif row == column or column == 0:
        return 1
    else:
        valor1 = pascal(row - 1, column - 1)
        valor2 = pascal(row - 1, column)
        resultado = valor1 + valor2
        return resultado


print("Ingrese la posición para econtrar el elemento.")
row = int(input("Ingrese la fila donde quiere buscar: ", ))
column = int(input("Ingrese la columna del elemento: ", ))
print("El elemento en la fila ", row, " y columna ", column, "es: ", pascal(row, column))
