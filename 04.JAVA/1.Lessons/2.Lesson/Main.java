//Логирование

// import java.util.logging.*;

// public class Main {
//    public static void main(String[] args) {
//        Logger logger = Logger.getLogger(Ex0043.class.getName());
//        logger.setLevel(Level.INFO);
//        ConsoleHandler ch = new ConsoleHandler();
//        logger.addHandler(ch);
//        //SimpleFormatter sFormat = new SimpleFormatter();
//        XMLFormatter xml = new XMLFormatter();
//        //ch.setFormatter(sFormat);
//        ch.setFormatter(xml);
//        logger.log(Level.WARNING, "Тестовое логирование");
//        logger.info("Тестовое логирование");
//    }
// }

// Работа с файлами

// import java.io.File;
// public class Main {
//    public static void main(String[] args) {
//        String pathProject = System.getProperty("user.dir");
//        String pathDir = pathProject.concat("/files");
//        File dir = new File(pathDir);
//        System.out.println(dir.getAbsolutePath());
//        if (dir.mkdir()) {
//            System.out.println("+");
//        } else {
//            System.out.println("-");
//        }
//        for (String fname : dir.list()) {
//            System.out.println(fname);
//        } } 
// }
