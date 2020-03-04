package com.company;

import java.util.Timer;

public class ReadJsonFile2 {

    public static void main(String[] args) throws Exception {

//        //First Employee
//        JSONObject employeeDetails = new JSONObject();
//        employeeDetails.put("firstName", "Lokesh");
//        employeeDetails.put("lastName", "Gupta");
//        employeeDetails.put("website", "howtodoinjava.com");
//
//        JSONObject employeeObject = new JSONObject();
//        employeeObject.put("employee", employeeDetails);
//
//        //Second Employee
//        JSONObject employeeDetails2 = new JSONObject();
//        employeeDetails2.put("firstName", "Brian");
//        employeeDetails2.put("lastName", "Schultz");
//        employeeDetails2.put("website", "example.com");
//
//        JSONObject employeeObject2 = new JSONObject();
//        employeeObject2.put("employee", employeeDetails2);
//
//        //Add employees to list
//        JSONArray employeeList = new JSONArray();
//        employeeList.put(employeeObject);
//        employeeList.put(employeeObject2);
//
//        new GenerateJson("C:\\Users\\Hassan\\Desktop\\test\\export.json", employeeList);

        Timer timer = new Timer();
        ReadDirectory2.directoryPath = "C:\\Users\\Hassan\\Desktop\\test";
        timer.schedule(new ReadDirectory(), 2000, 5000);
    }
}