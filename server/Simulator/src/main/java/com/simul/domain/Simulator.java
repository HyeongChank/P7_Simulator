package com.simul.domain;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Simulator {
	
	@Id
    private Long number;
    private String code;
    private int entryTime;
    private boolean visible;
    public Simulator() {
    	
    }
	public Simulator(Long number, String code, int entryTime, boolean visible) {
		super();
		this.number = number;
		this.code = code;
		this.entryTime = entryTime;
		this.visible = visible;
	}
	public Long getNumber() {
		return number;
	}
	public void setNumber(Long number) {
		this.number = number;
	}
	public String getCode() {
		return code;
	}
	public void setCode(String code) {
		this.code = code;
	}
	public int getEntryTime() {
		return entryTime;
	}
	public void setEntryTime(int entryTime) {
		this.entryTime = entryTime;
	}
	public boolean isVisible() {
		return visible;
	}
	public void setVisible(boolean visible) {
		this.visible = visible;
	}
	@Override
	public String toString() {
		return "Simulator [number=" + number + ", code=" + code + ", entryTime=" + entryTime + ", visible=" + visible
				+ "]";
	}

}
