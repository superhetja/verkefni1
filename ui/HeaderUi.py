from models.Color import Color

class Header:

    def __init__(self):
        pass
    
    def __str__(self):
        return Color.BOLD + 'Bílaleiga ehf.' + Color.END

    # def print_header(self):
    #     print(Color.BOLD + 'Bílaleiga ehf.' + Color.END)
