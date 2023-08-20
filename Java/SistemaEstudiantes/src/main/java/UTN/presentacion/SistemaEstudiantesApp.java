package UTN.presentacion;
import UTN.datos.EstudianteDAO;
import UTN.dominio.Estudiante;
import java.util.Scanner;


public class SistemaEstudiantesApp {
    public static void main(String[] args) {
        var salir = false; 
        var consola = new Scanner(system.in);
        //se crea una instancia de la clase servicio
        var estudianteDao =  new EstudianteDao();
        while(!salir){
            try {
                mostrarMenu();
                salir = ejecutarOpciones(consola,estudianteDao);
            } catch(Exception e){
                System.out.println("Ocurrio un error al ejecutar la operacion: "+e.getMessage());
            }
        }
        if (conexion != null) {
            System.out.println("Conexión exitosa: " + conexion);
        } else {
            System.out.println("Ocurrió un error al conectarse.");
        }

    } // Fin main
} // Fin clase Main