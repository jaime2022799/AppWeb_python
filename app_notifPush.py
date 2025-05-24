from os import path
from notifypy import Notify

notificacion = Notify()
notificacion.title = "AppWeb"
notificacion.message = "se a notificado con el servidor del sitio web"
icono = "logotipo.PNG"

direccion = path.abspath(path.dirname(__file__))
notificacion.icon = path.join(direccion, icono)

notificacion.send()