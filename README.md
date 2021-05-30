Es un paquete que te permitira obtener datos de un usuario de Minecraft y de los Servicios de Mojan y servidores de Minecraft

Repositorio del proyecto en Github: https://github.com/fab-henao/MC.git

//// Importar el modulo ////

from MC_API.Servicios_MC import Servicios_MCC as MCS

MCS.services_Check() /// No devuelve nada, solo impreme los servicios

from MC_API.User_MC import Servicios_MCC as MCU

MCU.get_History_Names() /// Devuelve un Objeto

MCU.get_Name_Free() /// No devuelve nada, imprime si esta disponible o no el nombre

MCU.get_Render_Skin() /// Devuele una respuesta Request

