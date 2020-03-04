package com.company;

import ilog.concert.IloException;
import ilog.concert.IloLinearNumExpr;
import ilog.concert.IloNumVar;
import ilog.cplex.IloCplex;

public class MyCplexExample {

    public static void main(String[] args) {
        try {

            IloCplex cplex = new IloCplex();

            //variables
            IloNumVar x = cplex.numVar(0, Double.MAX_VALUE, "x");
            IloNumVar y = cplex.numVar(0, Double.MAX_VALUE, "y");

            //expressions
            IloLinearNumExpr objective = cplex.linearNumExpr();
            objective.addTerm(0.12, x);
            objective.addTerm(0.15, y);

            //define objective
            cplex.addMinimize(objective);

            //define constraints
            cplex.addGe(cplex.sum(cplex.prod(60, x), cplex.prod(60, y)), 300);
            cplex.addGe(cplex.sum(cplex.prod(12, x), cplex.prod(6, y)), 36);
            cplex.addGe(cplex.sum(cplex.prod(10, x), cplex.prod(30, y)), 90);

            //solve
            if (cplex.solve()) {
                System.out.println("obj = " + cplex.getObjValue());
                System.out.println("X = " + cplex.getValue(x));
                System.out.println("Y = " + cplex.getValue(y));
            } else
                System.out.println("Model Not Solved");

        } catch (IloException e) {
            e.printStackTrace();
        }
    }
}
