package com.company;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.TimerTask;
import java.util.stream.Stream;

class ReadDirectory extends TimerTask {
    public static String directoryPath = "";

    public void run() {
        new ReadDirectory().listAllFiles(directoryPath);
    }

    // Uses Files.walk method
    private void listAllFiles(String path) {
        try (Stream<Path> paths = Files.walk(Paths.get(path))) {
            paths.forEach(filePath -> {
                if (Files.isRegularFile(filePath)) {
                    if (filePath.toString().endsWith(".json"))
                        if (!filePath.getFileName().toString().contains("_finished"))
                            if (!filePath.getFileName().toString().contains("_checked"))
                                try {
                                    readContent(filePath);
                                } catch (Exception e) {
                                    // TODO Auto-generated catch block
                                    e.printStackTrace();
                                }
                }
            });
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    private void readContent(Path filePath) throws IOException {
        // add checked end of the file path
        File oldFile = new File(filePath.toString());
        String newPath = filePath.toString().replace(".json", "_checked.json");
        File newFile = new File(newPath);
        oldFile.renameTo(newFile);

        // do any thing ...
        List<String> fileList = Files.readAllLines(Paths.get(newPath));
        System.out.println("" + fileList);
    }
}
