class Cancion:
    def __init__(self, titulo, disco, artista, idioma, genero, rep ) :
        self.titulo = titulo
        self.disco = disco
        self.artista = artista
        self.idioma = idioma
        self.genero = genero
        self.rep = rep


def to_string(cancion):
    r = ""
    r += ("\n\n☻Titulo:" + " " + str(cancion.titulo))
    r += '{:^30}'.format("-Album: " + str(cancion.disco))
    r += '{:>30}'.format("-Artista: " + str(cancion.artista))
    r += ("\n  -Idioma: " + str(cancion.idioma))
    r += '{:^30}'.format("-Genero: " + str(cancion.genero))
    r += '{:>30}'.format("-Reproducciones: " + str(cancion.rep))
    return r
