import logging


def descifradoCesar(message):
    logging.info('Descifrado iniciado')
    # Abrimos nuestro txt para descifrar y uno nuevo para los resultados
    foo = open(message, 'r')
    fo = open("descifrado.txt", 'w')
    # Analizamos cada mensaje
    for line in foo:
        message = line
        SYMBOLS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
                   'fghijklmnopqrstuvwxyz1234567890 !?.')
        # Registramos nuestro mensaje
        fo.write("Mensaje " + line)
        fo.write("\n")
        # Intentamos descifrar el mensaje por fuerza bruta, llave por llave
        for key in range(len(SYMBOLS)):
            translated = ''
            for symbol in message:
                # Verificamos si cada caracter está en SYMBOLS
                if symbol in SYMBOLS:
                    # Obtenemos su posición en SYMBOLS
                    symbolIndex = SYMBOLS.find(symbol)
                    # Obtenemos la nueva posición del caracter
                    translatedIndex = symbolIndex - key
                    # Acomodamos la posición de ser necesario
                    if translatedIndex < 0:
                        translatedIndex = translatedIndex + len(SYMBOLS)
                    # Registramos el nuevo carácter
                    translated = translated + SYMBOLS[translatedIndex]
                else:
                    # De no encontrarse en SYMBOLS, se escribe directamente
                    translated = translated + symbol
            # Registramos la key y su posible resltado
            fo.write('Key #%s: %s' % (key, translated))
            fo.write("\n")
        # Se marca el final para un mensaje y se continua con el siguiente
        fo.write("--------------------------------------------------------")
        fo.write("\n")
    logging.info('Descifrado terminado')
    # Guardamos los archivos txt
    fo.close()
    foo.close()
