import logging


def cifradoCesar(message):
    logging.info('Cifrado iniciado')
    # Abrimos un txt para escribir el resultado
    fo = open("cifrado.txt", 'w')
    # Declaramos una llave
    key = len(message)
    SYMBOLS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
               'fghijklmnopqrstuvwxyz1234567890 !?.')
    translated = ''
    for symbol in message:
        # Buscamos la posicion de cada carácter en SYMBOLS
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            # Ciframos esa letra con nuestra llave
            translatedIndex = symbolIndex + key

            # Posicionamos el índice dentro de SYMBOLS
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Añadimos la nueva letra al mensaje cifrado
            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Si el símbolo no esta en SYMBOLS este se escribe directamente
            translated = translated + symbol
    logging.info('Cifrado terminado')
    # Guardamos nuestro mensaje en el txt
    fo.write(translated)
    fo.close()
