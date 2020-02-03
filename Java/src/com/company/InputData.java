package com.company;

public class InputData {
    String gate;
    String visitId;
    String eqType;
    String eqLen;
    String date;
    String time;
    String emptyLoaded;
    String laneNr;
    String expressStatusCD;
    String onlineDestinationId;
    String onlineDestinationName;
    String offlineDestinationId;
    String offlineDestinationName;
    String eqInit;
    String eqNr;
    String route;
    String lot;

    public InputData(){}

    public InputData(String gate, String visitId, String eqType, String eqLen, String date, String time, String emptyLoaded, String laneNr, String expressStatusCD, String onlineDestinationId, String onlineDestinationName, String offlineDestinationId, String offlineDestinationName, String eqInit, String eqNr, String route, String lot) {
        this.gate = gate;
        this.visitId = visitId;
        this.eqType = eqType;
        this.eqLen = eqLen;
        this.date = date;
        this.time = time;
        this.emptyLoaded = emptyLoaded;
        this.laneNr = laneNr;
        this.expressStatusCD = expressStatusCD;
        this.onlineDestinationId = onlineDestinationId;
        this.onlineDestinationName = onlineDestinationName;
        this.offlineDestinationId = offlineDestinationId;
        this.offlineDestinationName = offlineDestinationName;
        this.eqInit = eqInit;
        this.eqNr = eqNr;
        this.route = route;
        this.lot = lot;
    }

    public String getLot() {
        return lot;
    }

    public void setLot(String lot) {
        this.lot = lot;
    }

    public String getGate() {
        return gate;
    }

    public void setGate(String gate) {
        this.gate = gate;
    }

    public String getVisitId() {
        return visitId;
    }

    public void setVisitId(String visitId) {
        this.visitId = visitId;
    }

    public String getEqType() {
        return eqType;
    }

    public void setEqType(String eqType) {
        this.eqType = eqType;
    }

    public String getEqLen() {
        return eqLen;
    }

    public void setEqLen(String eqLen) {
        this.eqLen = eqLen;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String getEmptyLoaded() {
        return emptyLoaded;
    }

    public void setEmptyLoaded(String emptyLoaded) {
        this.emptyLoaded = emptyLoaded;
    }

    public String getLaneNr() {
        return laneNr;
    }

    public void setLaneNr(String laneNr) {
        this.laneNr = laneNr;
    }

    public String getExpressStatusCD() {
        return expressStatusCD;
    }

    public void setExpressStatusCD(String expressStatusCD) {
        this.expressStatusCD = expressStatusCD;
    }

    public String getOnlineDestinationId() {
        return onlineDestinationId;
    }

    public void setOnlineDestinationId(String onlineDestinationId) {
        this.onlineDestinationId = onlineDestinationId;
    }

    public String getOnlineDestinationName() {
        return onlineDestinationName;
    }

    public void setOnlineDestinationName(String onlineDestinationName) {
        this.onlineDestinationName = onlineDestinationName;
    }

    public String getOfflineDestinationId() {
        return offlineDestinationId;
    }

    public void setOfflineDestinationId(String offlineDestinationId) {
        this.offlineDestinationId = offlineDestinationId;
    }

    public String getOfflineDestinationName() {
        return offlineDestinationName;
    }

    public void setOfflineDestinationName(String offlineDestinationName) {
        this.offlineDestinationName = offlineDestinationName;
    }

    public String getEqInit() {
        return eqInit;
    }

    public void setEqInit(String eqInit) {
        this.eqInit = eqInit;
    }

    public String getEqNr() {
        return eqNr;
    }

    public void setEqNr(String eqNr) {
        this.eqNr = eqNr;
    }

    public String getRoute() {
        return route;
    }

    public void setRoute(String route) {
        this.route = route;
    }
}
