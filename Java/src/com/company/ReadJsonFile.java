package com.company;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.Timer;
import java.util.TimerTask;

public class ReadJsonFile {

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
        ReadDirectory.directoryPath = "C:\\Users\\Hassan\\Desktop\\test";
        timer.schedule(new ReadDirectory(), 1000, 1000);
    }
}