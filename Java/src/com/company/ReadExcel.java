package com.company;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;

public class ReadExcel {

    public static HashMap<Integer, List<String>> readExcel(String inputFile, int sheetNum) throws IOException {
        HashMap<Integer, List<String>> result = new HashMap<>();

        File myFile = new File(inputFile);
        FileInputStream fis = new FileInputStream(myFile);

        // Finds the workbook instance for XLSX file
        XSSFWorkbook myWorkBook = new XSSFWorkbook(fis);

        // Return first sheet from the XLSX workbook
        XSSFSheet mySheet = myWorkBook.getSheetAt(sheetNum);

        // Get iterator to all the rows in current sheet
        Iterator<Row> rowIterator = mySheet.iterator();

        // Traversing over each row of XLSX file
        int rowId = 0;
        while (rowIterator.hasNext()) {
            List<String> data = new ArrayList<>();
            Row row = rowIterator.next();
            rowId++;
            // For each row, iterate through each columns
            Iterator<Cell> cellIterator = row.cellIterator();
            while (cellIterator.hasNext()) {
                Cell cell = cellIterator.next();
                switch (cell.getCellTypeEnum()) {
                    case STRING:
                        data.add(cell.getStringCellValue());
                        break;
                    case NUMERIC:
                        data.add(String.valueOf(cell.getNumericCellValue()));
                        break;
                    case BOOLEAN:
                        data.add(String.valueOf(cell.getBooleanCellValue()));
                        break;
                    case BLANK:
                        data.add("BLANK");
                    default:
                }
            }
            result.put(rowId, data);
        }
        return result;
    }

}
