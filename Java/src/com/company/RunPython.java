package com.company;

import org.python.util.PythonInterpreter;
import org.python.core.*;

public class RunPython {
    // instantiate a fresh interpreter
    PythonInterpreter interp = new PythonInterpreter();

    // a 'do nothing' constructor
    public RunPython() { }

    // use this contructor if no variables to be passed
    // in and you want to run a Jython program (saves a line)
    public RunPython(String filename) {
        run(filename);
    }

    // run the named Jython program
    public void run(String filename){
        interp.execfile(filename);
    }

    // gets an integer return value
    public int getInt(String name) {
        return ((PyInteger) interp.get(name)).getValue();
    }

    // sets an input integer value
    public void setInt(String name, int value){
        interp.set(name, new PyInteger(value));
    }

    // gets a double return value (Python floats are doubles)
    public double getDouble(String name) {
        return ((PyFloat) interp.get(name)).getValue();
    }

    // sets an input double value (Python floats are doubles)
    public void setDouble(String name, double value){
        interp.set(name, new PyFloat(value));
    }

    // gets a string return value
    public String getStr(String name) {
        return ((PyString) interp.get(name)).toString();
    }

    // sets an input string value
    public void setStr(String name, String value){
        interp.set(name, new PyString(value));
    }

    // can add more getters and setters for complex,
    // list, dictionary, tuple, etc.   ...someday.
}
