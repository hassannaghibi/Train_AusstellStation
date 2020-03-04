package com.company;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;

public class GenerateJson {

    private Gson gson;
    private Object object;

    public GenerateJson(String file, Object object) {
        try (Writer writer = new FileWriter(file)) {
            this.gson = new GsonBuilder().setPrettyPrinting().create();
            this.gson.toJson(object, writer);
            this.object = object;
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void printGenerateJson() {
        this.gson.toJson(object, System.out);
    }
}
