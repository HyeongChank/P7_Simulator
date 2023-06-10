package com.simulator.predict.domain;

public class Inputdata {
	private int trucknum;
    private int processtime;
    private int blocknum;
    
    public Inputdata() {
    	
    }
	public Inputdata(int trucknum, int processtime, int blocknum) {
		super();
		this.trucknum = trucknum;
		this.processtime = processtime;
		this.blocknum = blocknum;
	}
	public int getTrucknum() {
		return trucknum;
	}
	public void setTrucknum(int trucknum) {
		this.trucknum = trucknum;
	}
	public int getProcesstime() {
		return processtime;
	}
	public void setProcesstime(int processtime) {
		this.processtime = processtime;
	}
	public int getBlocknum() {
		return blocknum;
	}
	public void setBlocknum(int blocknum) {
		this.blocknum = blocknum;
	}
	@Override
	public String toString() {
		return "Inputdata [trucknum=" + trucknum + ", processtime=" + processtime + ", blocknum=" + blocknum + "]";
	}
    
    
}
