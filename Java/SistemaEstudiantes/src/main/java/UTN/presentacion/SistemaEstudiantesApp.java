package UTN.presentacion;

import UTN.datos.EstudianteDAO;
import UTN.dominio.Estudiante;


import java.util.Scanner;

public class SistemaEstudiantesApp {
    public static void main(String[] args) {
        var salir = false;
        var consola = new Scanner(System.in); //Para leer informacion de la consola
        //Se crea una instancia de la clase servicio, esto lo hacemos fuera del ciclo
        var estudianteDao = new EstudianteDAO();//Esta instancia debe hacerse una vez
        while(!salir){
            try {
                mostrarMenu();//Mostramos el menu
                //Este sera el metodo que devolvera un booleano
                salir = ejecutarOpciones(consola, estudianteDao);//Este arroja una excepcion
            } catch(Exception e){
                System.out.println("Ocurrio un error al ejecutar la operacion: "+e.getMessage());
            }
        }//Fin while
    } //Fin main

    private static void mostrarMenu(){
        System.out.print("""
                ******* Sistema de Estudiantes *******
                1. Listar Estudiantes
                2. Buscar Estudiantes
                3. Agregar Estudiante
                4. Modificar Estudiante
                5. Eliminar Estudiante
                6. Salir
                Elije una opcion: 
                """);
    }
    //Metodo para ejecutar las opciones, va a regresar un valor booleano, ya que es el que
    //puede modificar el valor de la variable salir, si es verdadero termina el ciclo while
    private static boolean ejecutarOpciones(Scanner consola, EstudianteDAO estudianteDAO){
        var opcion = Integer.parseInt(consola.nextLine());
        var salir = false;
        switch(opcion){
            case 1 -> { //Listar estudiantes
                System.out.println("Listado de estudiantes...");
                //no muestra la informacion, solo recupera la info y regresa una lista
                var estudiantes = estudianteDAO.listarEstudiantes();//recibe el listado
                //vamos a iterar cada objeto de tipo estudiante
                estudiantes.forEach(System.out::println);//para imprimir la lista
            }//Fin caso 1
            case 2 -> { //Buscar estudiante por id
                System.out.print("Introduce el id_estudiante a buscar: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                var estudiante = new Estudiante(idEstudiante);
                var encontrado = estudianteDAO.buscarEstudiantePorId(estudiante);
                if(encontrado)
                    System.out.println("Estudiante encontrado: "+estudiante);
                else
                    System.out.println("Estudiante No encontrado: "+estudiante);
            }//Fin caso 2
            case 3 -> { //Agregar estudiante
                System.out.println("Agregar estudiante: ");
                System.out.print("Nombre: ");
                var nombre = consola.nextLine();
                System.out.print("Apellido: ");
                var apellido = consola.nextLine();
                System.out.print("Telefono: ");
                var telefono = consola.nextLine();
                System.out.print("Email: ");
                var email = consola.nextLine();
                //crear objeto estudiante(sin id)
                var estudiante = new Estudiante(nombre, apellido, telefono, email);
                var agregado = estudianteDAO.agregarEstudiante(estudiante);
                if(agregado)
                    System.out.println("Estudiante agregado: "+estudiante);
                else
                    System.out.println("Estudiante No agregado: "+estudiante);
            }//Fin caso 3
            case 4 -> {//Modificar estudiante
                System.out.println("Modificar estudiante: ");
                //Aqui lo primero es especificar cual es el id del objeto a modificar
                System.out.print("Id Estudiante: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                System.out.print("Nombre: ");
                var nombre = consola.nextLine();
                System.out.print("Apellido: ");
                var apellido = consola.nextLine();
                System.out.print("Telefono: ");
                var telefono = consola.nextLine();
                System.out.print("Email: ");
                var email = consola.nextLine();
                //crea el objeto estudiante a modificar
                var estudiante =
                        new Estudiante(idEstudiante, nombre, apellido, telefono, email);
                var modificado = estudianteDAO.modificarEstudiante(estudiante);
                if(modificado)
                    System.out.println("Estudiante modificado: "+estudiante);
                else
                    System.out.println("Estudiante NO modificado: "+estudiante);
            }//Fin caso 4
            case 5 -> {//Eliminar estudiante
                System.out.print("Eliminar estudiante: ");
                System.out.print("Id estudiante: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                var estudiante = new Estudiante(idEstudiante);
                var eliminado = estudianteDAO.eliminarEstudiante(estudiante);
                if(eliminado)
                    System.out.println("Estudiante eliminado: "+estudiante);
                else
                    System.out.println("Estudiante No eliminado: "+estudiante);
            }//Fin caso 5
            case 6 -> { //salir
                System.out.println("Hasta pronto!!!");
                salir = true;
            }//Fin caso 6
            default -> System.out.println("Opcion no reconocida, ingrese otra opcion");
        }//Fin switch
        return salir;
    }
}// Fin clase