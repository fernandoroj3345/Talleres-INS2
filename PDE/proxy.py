#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Proxy
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
class College:
    '''Recurso que se quiere restringir el acceso'''

    def studyingInCollege(self):
        print("ID del estudiante es correcto")


class CollegeProxy:
    '''Solo accede al recurso de uso intensivo si se dan condiciones previas'''

    def __init__(self):

        self.feeBalance = 1000
        self.id = None
        self.college = None

    def studyingInCollege(self):

        print("\n\nAcceso al Proxy. Revisa el saldo antes de acceder al recurso")
        if self.feeBalance <= 500:
            self.college = College()
            print("Validación de ID(%s) contra el database externo:\n" % (self.id))
            self.college.studyingInCollege()
        else:
            print("Estudiante ID(%s) Debe ponerse al día con la matricula" % (self.id))

main method

if __name__ == "__main__":

    import os
    os.system('clear')

#*--- Instancia los objetos a operar back to back
    
    collegeProxy = CollegeProxy()


    # Estudiante con pagos demorados
    collegeProxy.id="Gomez,Pepe"
    collegeProxy.studyingInCollege()
    
    # Estudiante con pagos al dia
    collegeProxy.id="Alvarez,Mica"
    collegeProxy.feeBalance = 100
    collegeProxy.studyingInCollege()
"""
##################################################################################
class College:
    '''Recurso que se quiere restringir el acceso'''

    def studyingInCollege(self, student_id):
        print(f"ID del estudiante '{student_id}' es correcto. Acceso concedido al college.")


class CollegeProxy:
    '''Proxy que valida saldo y agrega capa de encriptación al ID'''

    def __init__(self):
        self.feeBalance = 1000
        self.id = None
        self.college = None

    def _encrypt(self, text):
        # Encriptación simple: corrimiento César +3 (solo para demo)
        encrypted = ''.join(chr((ord(char) + 3) % 256) for char in text)
        return encrypted

    def _decrypt(self, encrypted_text):
        decrypted = ''.join(chr((ord(char) - 3) % 256) for char in encrypted_text)
        return decrypted

    def studyingInCollege(self):
        print("\n\nAcceso al Proxy. Revisa el saldo antes de acceder al recurso")

        if self.feeBalance <= 500:
            # Encriptar ID antes de validación
            encrypted_id = self._encrypt(self.id)
            print(f"ID encriptado para validación: {encrypted_id}")

            # Aquí podrías agregar validación contra base externa usando el ID encriptado
            # Para este ejemplo, asumimos que la validación pasa si el ID no está vacío

            # Desencriptar para pasar al recurso original
            decrypted_id = self._decrypt(encrypted_id)
            print(f"ID desencriptado para acceso al recurso: {decrypted_id}")

            self.college = College()
            self.college.studyingInCollege(decrypted_id)
        else:
            print(f"Estudiante ID({self.id}) debe ponerse al día con la matrícula")


if __name__ == "__main__":
    import os
    os.system('clear')

    collegeProxy = CollegeProxy()

    # Estudiante con pagos demorados
    collegeProxy.id = "Gomez,Pepe"
    collegeProxy.studyingInCollege()

    # Estudiante con pagos al día
    collegeProxy.id = "Alvarez,Mica"
    collegeProxy.feeBalance = 100
    collegeProxy.studyingInCollege()


"""
Se añadió un método _encrypt y _decrypt con una encriptación (corrimiento César) para ilustrar la capa adicional.

El proxy encripta el ID antes de la validación (simulada aquí) y luego lo desencripta para pasar al recurso College.

La validación real podría ser más compleja, incluyendo consultas a bases de datos o servicios externos con el ID encriptado.

El acceso al recurso College solo se da si el saldo está al día (feeBalance <= 500).

El método studyingInCollege en College ahora recibe el ID desencriptado para mostrarlo.
"""