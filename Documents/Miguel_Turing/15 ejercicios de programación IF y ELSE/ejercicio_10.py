user_correcto = "admin"
password_correcto = "12345"

usuario = input("Ingrese el usuario: ")
password = input("Ingrese la contraseña: ")

if usuario == user_correcto and password == password_correcto:
    print("Acceso concedido")
else:
    print("Acceso denegado. Usuario o contraseña incorrectos.")