class Argentina():
    def capital(self):
        print('Buenos Aires é a capital da Argentina.')
    def lingua_oficial(self):
        print('O espanhol é a lingua oficial da Argentina.')

class Brasil():
    def capital(self):
        print('A capital do Brasil é Brasília.')
    def lingua_oficial(self):
        print('A linguagem oficial do Brasil é o Português.')

obj_arg = Argentina()
obj_bra = Brasil()
for pais in (obj_arg, obj_bra):
    pais.capital()
    pais.lingua_oficial()