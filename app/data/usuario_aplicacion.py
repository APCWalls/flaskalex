from app.data.modelo.usuarios import Usuario

class UsuarioAplicacion:

    def select_all(self,db) -> list[Usuario]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM usuario')
        usuarios_en_db = cursor.fetchall()
        usuarios : list[Usuario]= list()
        for usuario_en_db in usuarios_en_db:
            usuarios.append(Usuario(usuario_en_db[0], usuario_en_db[1], usuario_en_db[2]))
        cursor.close()
        return usuarios