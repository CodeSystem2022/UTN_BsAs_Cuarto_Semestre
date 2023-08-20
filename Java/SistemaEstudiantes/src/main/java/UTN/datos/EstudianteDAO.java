package UTN.datos;

import UTN.dominio.Estudiante;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import static UTN.conexion.Conexion.getConnection;

public class EstudianteDAO {

    // Método listar()
    public List<Estudiante> listar() {
        List<Estudiante> estudiantes = new ArrayList<>();
        // Creamos algunos objetos que son necesarios para comunicarnos con la base de datos
        PreparedStatement ps; // Envia querys a la base de datos
        ResultSet rs; // Guarda la información que devuelve la base de datos

        // Creamos un objeto de tipo conexion
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022;";


        try {
            ps = con.prepareStatement(sql); // Enviamos la consulta sql a la conexión
            rs = ps.executeQuery(); // Guardamos los datos resultantes para itinerar y crear los estudiantes
            while (rs.next()) {
                // Creamos un objeto estudiante para guardar los datos recibidos
                Estudiante estudiante = new Estudiante();
                estudiante.setIdEstudiante(rs.getInt("idestudiantes2022"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                // Agregamos el estudiante a la lista
                estudiantes.add(estudiante);
            }
        } catch (Exception e) {
            System.out.println("Ocurrió un error al listar datos: " + e.getMessage());
        } finally {
            // Cerramos la conexión al terminar la consulta
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Ocurrió un error al cerrar la conexión: " + e.getMessage());
            }
        } // Fin finally
        return estudiantes;
    } // Fin método listar()

    // Método buscarPorId() ó findById()
    public boolean buscarPorId(Estudiante estudiante) {
        // Creamos algunos objetos que son necesarios para comunicarnos con la base de datos
        PreparedStatement ps; // Envia querys a la base de datos
        ResultSet rs; // Guarda la información que devuelve la base de datos

        // Creamos un objeto de tipo conexion
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022 WHERE idestudiantes2022 =?;";

        try {
            ps = con.prepareStatement(sql); // Enviamos la consulta sql a la conexión
            ps.setInt(1, estudiante.getIdEstudiante());
            rs = ps.executeQuery(); // Guardamos los datos resultantes para itinerar y crear los estudiantes
            if (rs.next()) {
                // Creamos un objeto estudiante para guardar los datos recibidos

                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                return true;

            }
        } catch (Exception e) {
            System.out.println("Ocurrió un error al buscar por Id: " + e.getMessage());
        } finally {
            // Cerramos la conexión al terminar la consulta
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Ocurrió un error al cerrar la conexión: " + e.getMessage());
            }
        } // Fin finally
        return false;
    }

    // Agregar estudiante
    public boolean agregarEstudiante(Estudiante estudiante) {
        // Creamos algunos objetos que son necesarios para comunicarnos con la base de datos
        PreparedStatement ps; // Envia querys a la base de datos
        // Creamos un objeto de tipo conexion
        Connection con = getConnection();
        String sql = "INSERT INTO estudiantes2022 (nombre, apellido, telefono, email) VALUES (?,?,?,?);";
        try {
            ps = con.prepareStatement(sql); // Enviamos la consulta sql a la conexión
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());

            ps.execute(); // Ejecutamos, no es necesario guardar resultados
            return true;
        } catch (Exception e) {
            System.out.println("Ocurrió un error al agregar un estudiante: " + e.getMessage());
        } finally {
            // Cerramos la conexión al terminar la consulta
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Ocurrió un error al cerrar la conexión: " + e.getMessage());
            }
        } // Fin finally
        return false;
    }

    // Modificar estudiante
    public boolean modificarEstudiante(Estudiante estudiante) {
        // Creamos algunos objetos que son necesarios para comunicarnos con la base de datos
        PreparedStatement ps; // Envia querys a la base de datos
        // Creamos un objeto de tipo conexion
        Connection con = getConnection();
        String sql = "UPDATE estudiantes2022 SET nombre = ?, apellido = ? , telefono = ? , email = ? WHERE idestudiantes2022 = ?;";
        try {
            ps = con.prepareStatement(sql); // Enviamos la consulta sql a la conexión
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.setInt(5, estudiante.getIdEstudiante());

            ps.execute(); // Ejecutamos, no es necesario guardar resultados
            return true;
        } catch (Exception e) {
            System.out.println("Ocurrió un error al modificar un estudiante: " + e.getMessage());
        } finally {
            // Cerramos la conexión al terminar la consulta
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Ocurrió un error al cerrar la conexión: " + e.getMessage());
            }
        } // Fin finally
        return false;
    }

    // Eliminar estudiante
    public boolean eliminarEstudiante(Estudiante estudiante) {
        // Creamos algunos objetos que son necesarios para comunicarnos con la base de datos
        PreparedStatement ps; // Envia querys a la base de datos
        // Creamos un objeto de tipo conexion
        Connection con = getConnection();
        String sql = "DELETE FROM estudiantes2022 WHERE idestudiantes2022 = ?;";
        try {
            ps = con.prepareStatement(sql); // Enviamos la consulta sql a la conexión
            ps.setInt(1, estudiante.getIdEstudiante());
            ps.execute(); // Ejecutamos, no es necesario guardar resultados
            return true;
        } catch (Exception e) {
            System.out.println("Ocurrió un error al eliminar un estudiante: " + e.getMessage());
        } finally {
            // Cerramos la conexión al terminar la consulta
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Ocurrió un error al cerrar la conexión: " + e.getMessage());
            }
        } // Fin finally

        return false;

    }

    // Creamos un main para test
    public static void main(String[] args) {
        // Listar los estudiantes
        EstudianteDAO estudianteDAO = new EstudianteDAO();
        System.out.println("Listado de estudiantes: ");
        List<Estudiante> estudiantes = estudianteDAO.listar();
        //estudiantes.forEach(estudiante -> System.out.println(estudiante));
        // Función lambda para imprimir
        estudiantes.forEach(System.out::println);

        System.out.println("Buscamos por id: ");
        Estudiante estudiante1 = new Estudiante(3);
        Boolean resultado = estudianteDAO.buscarPorId(estudiante1);
        if (resultado) {
            System.out.println("Estudiante encontrado: ");
            System.out.println(estudiante1);
        } else {
            System.out.println("Estudiante no encontrado. Id: " + estudiante1.getIdEstudiante());
        }

//        // Eliminamos un estudiante
//        Estudiante estudiante4 = new Estudiante(4);
//        resultado = estudianteDAO.eliminarEstudiante(estudiante4);
//        if (resultado) {
//            System.out.println("Estudiante eliminado con éxito");
//        } else {
//            System.out.println("No se eliminó el estudiante");
//        }

        // Modificamos un estudiante
//        Estudiante estudiante3 = new Estudiante(2, "Vale","Alvarez","2913338882","vale@alvarez.com");
//        resultado = estudianteDAO.modificarEstudiante(estudiante3);
//        if (resultado) {
//            System.out.println("Se modificó el estudiante.");
//        }
        // Agregamos un estudiante
//        Estudiante estudiante2 = new Estudiante("Jacinto", "Perez", "299345654","jperez@mail.com");
//        resultado = estudianteDAO.agregarEstudiante(estudiante2);
//        if (resultado) {
//            System.out.println("Se agregó el estudiante:");
//        }
    } // Fin clase main

} // Fin clase EstudianteDAO