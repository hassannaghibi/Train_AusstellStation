package com.company;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import sun.reflect.generics.tree.Tree;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) throws Exception {

        //read from Mysql database
        MySQLAccess dao = new MySQLAccess("localhost:3306/", "test", "root", "");
        dao.readDataBase();
    }

    static void createExcel(ArrayList<InputData> data, String path, String sheetTitle) {
        try {
            Workbook workbook = new XSSFWorkbook();
            Sheet sheet = workbook.createSheet(sheetTitle);
            Row headerRow = sheet.createRow(0);

            String[] columnsHeader = {"Gate_Evt", "Visit ID", "EQ Type", "EQ Len", "Date", "Load_Empty", "Lane NR", "Express Status CD", "ONLINE ID", "ONLINE Destination", "OFFLINE Destination ID", "OFFLINE Destination", "EQ_INIT", "EQ_NR", "Route", "Lot"};
            for (int f = 0; f < columnsHeader.length; f++) {
                Cell cell = headerRow.createCell(f);
                cell.setCellValue(columnsHeader[f]);
            }

            for (int t = 0; t < data.size(); t++) {
                Row row = sheet.createRow(t + 1);
                String[] columns = {data.get(t).getGate(), data.get(t).getVisitId(), data.get(t).getEqType(), data.get(t).getEqLen(), data.get(t).getDate(), data.get(t).getTime(), data.get(t).getEmptyLoaded(), data.get(t).getLaneNr(), data.get(t).getExpressStatusCD(), data.get(t).getOnlineDestinationId(), data.get(t).getOnlineDestinationName(), data.get(t).offlineDestinationId, data.get(t).offlineDestinationName, data.get(t).getEqInit(), data.get(t).getEqNr(), data.get(t).getRoute(), data.get(t).getLot()};
                for (int f = 0; f < columns.length; f++) {
                    Cell cell = row.createCell(f);
                    cell.setCellValue(columns[f]);
                }
            }

            FileOutputStream fileOutputStream = new FileOutputStream(path);
            workbook.write(fileOutputStream);

            fileOutputStream.close();

            workbook.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static void writeTextFile() {
        try {
            PrintWriter outputFile = new PrintWriter(
                    new BufferedWriter(
                            new FileWriter("words.txt")));
            // (true is used to append data to the file)

            // outputFile.print();
            outputFile.println("This is a test");
            outputFile.println("For a file I have created");
            outputFile.println("on the past :)");

            // Closing the output stream enabling the reading of the file
            outputFile.close();
        } catch (IOException e) {
            System.err.println("Some IOException Happened: " + e.getMessage());
        }
    }

    public static String readTextFile() {
        String fileContent = "";
        BufferedReader br = null;
        ;
        try {
            br = new BufferedReader(new FileReader("TextFile.txt"));
            StringBuilder sb = new StringBuilder();
            String fileLine = "";
            while ((fileLine = br.readLine()) != null) {
                System.out.println(fileLine);
                sb.append(fileLine);
                sb.append(System.lineSeparator());
            }
            fileContent = sb.toString();
            br.close();
        } catch (IOException ioe) {
            ioe.getMessage();
        }
        return fileContent;
    }

}
