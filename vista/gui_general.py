from tkinter import filedialog, messagebox

class GuiGeneral:
    """
    Clase que encapsula funciones generales de la interfaz gráfica usando Tkinter.
    """

    @staticmethod
    def cargar_archivo():
        """
        Abre un cuadro de diálogo para seleccionar un archivo y retorna la ruta seleccionada.
        :return: Ruta del archivo seleccionado por el usuario.
        """
        return filedialog.askopenfilename()

    @staticmethod
    def mostrar_mensaje_informativo(mensaje: str):
        """
        Muestra un mensaje informativo al usuario.
        :param mensaje: Texto a mostrar en la ventana de información.
        """
        messagebox.showinfo(title='Información', message=mensaje)

    @staticmethod
    def mostrar_mensaje_error(mensaje: str):
        """
        Muestra un mensaje de error al usuario.
        :param mensaje: Texto a mostrar en la ventana de error.
        """
        messagebox.showerror(title='Error', message=mensaje)
