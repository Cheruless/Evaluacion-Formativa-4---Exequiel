from turistas import *

def turistas_por_pais(pais):
    listaTuristas = [];
    for datos in turistas.values():
        if( pais.lower() in datos[1].lower() ):
            listaTuristas.append(datos[0]);
    return listaTuristas if(len(listaTuristas)) else "No hay turistas de ese pais.";

def turistas_por_mes(mes):
    contTotal = contMes = 0;
    for datos in turistas.values():
        contTotal += 1;
        if( mes in (datos[2].split('-'))[1] ):
            contMes += 1;
    return round((contMes/contTotal)* 100, 1)  if (contTotal) else 0;

def eliminar_turista():
    nombreTurista = input("Ingrese el nombre del turista a eliminar: ");
    for key, datos in turistas.items():
        if (datos[0].lower() == nombreTurista.lower()):
            del turistas[key];
            print("Turista eliminado con éxito.");
            return;
    print("Turista no encontrado. No se pudo eliminar.");

