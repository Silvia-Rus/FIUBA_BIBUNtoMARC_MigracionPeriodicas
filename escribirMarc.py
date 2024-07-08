
class EscribirMARC:
    """
      Escribe un registro en un archivo.
    """

    def __init__(self, nombreArchivo):
        """
          Asigna el nombre del archivo en el cual se va a escribir.

          Args:
            nombreArchivo (str): nombre del archivo.
        """
        self.nombreArchivo = nombreArchivo

    def escribir(self, record):
        """
          Escribe en un archivo un registro.

          Args:
            record (record): el registro que se quiere escribir en el archivo.
        """
        record.fields.sort(key=lambda field: field.tag)
        with open(self.nombreArchivo, 'ab') as out:
            out.write(record.as_marc())

