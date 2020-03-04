package com.company;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.TimerTask;
import java.util.stream.Stream;

class ReadDirectory2 extends TimerTask {
    public static String directoryPath = "";

    public void run() {
        new ReadDirectory2().listAllFiles(directoryPath);
    }

    // Uses Files.walk method
    private void listAllFiles(String path) {
        try (Stream<Path> paths = Files.walk(Paths.get(path))) {
            paths.forEach(filePath -> {
                if (Files.isRegularFile(filePath)) {
                    if (filePath.toString().endsWith(".json"))
                        if (!filePath.getFileName().toString().contains("_finished"))
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
        String newPath = filePath.toString().replace("_checked.json", "_finished.json");
        File newFile = new File(newPath);
        oldFile.renameTo(newFile);

        // do any thing ...
        System.out.println(readFile(newFile.getPath()));

    }

    private static String readFile(String path) throws IOException {
        FileInputStream stream = new FileInputStream(new File(path));
        try {
            FileChannel fc = stream.getChannel();
            MappedByteBuffer bb = fc.map(FileChannel.MapMode.READ_ONLY, 0, fc.size());
            /* Instead of using default, pass in a decoder. */
            return Charset.defaultCharset().decode(bb).toString();
        }
        finally {
            stream.close();
        }
    }
}
