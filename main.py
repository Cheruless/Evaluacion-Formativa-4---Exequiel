from funciones import *

proceso = True;

while proceso:
    print("*** MENU PRINCIPAL ***");
    print("1.- Turistas por país.");
    print("2.- Turista por mes.");
    print("3.- Eliminar turista.");
    print("4.- Salir.");
    
    opc = 0;
    while ((opc < 1) or (opc > 4)):
        try:
            opc = int(input("Ingrese opción: "));
            if( (opc < 1) or (opc > 4) ):
                print("Debe ingresar una opción válida!!");
        except ValueError:
            print("INGRESE NUMEROS ENTEROS.");
    
    match(opc):
        case 1:
            print(turistas_por_pais(input("Ingrese pais a buscar: ")));
        case 2:
            mesIngresado = 0;
            while ( (int(mesIngresado) < 1) | (int(mesIngresado) > 12) ):
                mesIngresado = input("Ingrese mes a buscar: ").zfill(2);
                if ( (int(mesIngresado) < 1) | (int(mesIngresado) > 12) ):
                    print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.");
                else:
                    print(f"El número de turistas equivale al {turistas_por_mes(mesIngresado)}% del total.");
        case 3:
            eliminar_turista();
        case 4:
            print("Programa terminado...");
            proceso = False;