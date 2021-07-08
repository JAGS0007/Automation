import configparser

configuracion = configparser.ConfigParser()

configuracion['General'] = {'chrome' : 'ChromeDriverManager().install()'}
configuracion['Paginas'] = {'page' : 'http://www.google.com'}

with open('C:\\Users\\ING\\Desktop\\Automation\\Automation\\Archivos_Ini_y_Config\\configuracion.ini', 'w') as archivoconfig:
    configuracion.write(archivoconfig)