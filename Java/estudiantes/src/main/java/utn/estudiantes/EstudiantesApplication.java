package utn.estudiantes;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import utn.estudiantes.servicio.EstudianteServicio;

@SpringBootApplication
public class EstudiantesApplication implements CommandLineRunner { // CommandLIneRunner establece que es una aplicación por consola

    @Autowired
    private EstudianteServicio estudianteServicio;
    private static final Logger logger = LoggerFactory.getLogger(EstudiantesApplication.class); // Logger imprime información en pantalla

    String nl = System.lineSeparator(); // Devuelve el caracter de salto de linea en cualquier sistema operativo.

    public static void main(String[] args) {
        logger.info("Iniciando la aplicación...");
        // Inicia la fábrica de Spring
        SpringApplication.run(EstudiantesApplication.class, args);
        logger.info("Aplicación finalizada!");
    }

    @Override
    public void run(String... args) throws Exception {
        logger.info(nl+"Ejecutando el método run de Spring..."+nl);

    }
}
