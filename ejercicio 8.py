precio = input("escribe el precio del producto con dosdecimales: ")
print(precio[:precio.find('.')], 'quetzales y', precio[precio.find('.')+1:], 'centavos.')
