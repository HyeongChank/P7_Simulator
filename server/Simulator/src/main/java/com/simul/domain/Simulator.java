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
    private int arrive_unload_spot;
    private int start_unload_work;
    private int complete_unload_work;
    private int arrive_load_spot;
    private int start_load_work;
    private int complete_load_work;
    
    private int out_time;
    private String block;
    private int unload_count;
    private int load_count;
    private int yard_truck_count;
    private int unload_wait_time;
    private int load_wait_time;
    private int total_wait_time;
    
    private int entry_to_unload;
    private int entry_to_load;
    private int arrive_to_complete_unload;
    private int arrive_to_complete_load;
    private int complete_to_exit_unload;
    private int complete_to_exit_load;
    
    private int unload_to_load;
    
    private String unload_block;
    private String load_block;
    private boolean visible;

    public Simulator() {
    	
    }

	public Simulator(Long number, String code, int entryTime, int arrive_unload_spot, int start_unload_work,
			int complete_unload_work, int arrive_load_spot, int start_load_work, int complete_load_work, int out_time,
			String block, int unload_count, int load_count, int yard_truck_count, int unload_wait_time,
			int load_wait_time, int total_wait_time, int entry_to_unload, int entry_to_load,
			int arrive_to_complete_unload, int arrive_to_complete_load, int complete_to_exit_unload,
			int complete_to_exit_load, int unload_to_load, String unload_block, String load_block, boolean visible) {
		super();
		this.number = number;
		this.code = code;
		this.entryTime = entryTime;
		this.arrive_unload_spot = arrive_unload_spot;
		this.start_unload_work = start_unload_work;
		this.complete_unload_work = complete_unload_work;
		this.arrive_load_spot = arrive_load_spot;
		this.start_load_work = start_load_work;
		this.complete_load_work = complete_load_work;
		this.out_time = out_time;
		this.block = block;
		this.unload_count = unload_count;
		this.load_count = load_count;
		this.yard_truck_count = yard_truck_count;
		this.unload_wait_time = unload_wait_time;
		this.load_wait_time = load_wait_time;
		this.total_wait_time = total_wait_time;
		this.entry_to_unload = entry_to_unload;
		this.entry_to_load = entry_to_load;
		this.arrive_to_complete_unload = arrive_to_complete_unload;
		this.arrive_to_complete_load = arrive_to_complete_load;
		this.complete_to_exit_unload = complete_to_exit_unload;
		this.complete_to_exit_load = complete_to_exit_load;
		this.unload_to_load = unload_to_load;
		this.unload_block = unload_block;
		this.load_block = load_block;
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

	public int getArrive_unload_spot() {
		return arrive_unload_spot;
	}

	public void setArrive_unload_spot(int arrive_unload_spot) {
		this.arrive_unload_spot = arrive_unload_spot;
	}

	public int getStart_unload_work() {
		return start_unload_work;
	}

	public void setStart_unload_work(int start_unload_work) {
		this.start_unload_work = start_unload_work;
	}

	public int getComplete_unload_work() {
		return complete_unload_work;
	}

	public void setComplete_unload_work(int complete_unload_work) {
		this.complete_unload_work = complete_unload_work;
	}

	public int getArrive_load_spot() {
		return arrive_load_spot;
	}

	public void setArrive_load_spot(int arrive_load_spot) {
		this.arrive_load_spot = arrive_load_spot;
	}

	public int getStart_load_work() {
		return start_load_work;
	}

	public void setStart_load_work(int start_load_work) {
		this.start_load_work = start_load_work;
	}

	public int getComplete_load_work() {
		return complete_load_work;
	}

	public void setComplete_load_work(int complete_load_work) {
		this.complete_load_work = complete_load_work;
	}

	public int getOut_time() {
		return out_time;
	}

	public void setOut_time(int out_time) {
		this.out_time = out_time;
	}

	public String getBlock() {
		return block;
	}

	public void setBlock(String block) {
		this.block = block;
	}

	public int getUnload_count() {
		return unload_count;
	}

	public void setUnload_count(int unload_count) {
		this.unload_count = unload_count;
	}

	public int getLoad_count() {
		return load_count;
	}

	public void setLoad_count(int load_count) {
		this.load_count = load_count;
	}

	public int getYard_truck_count() {
		return yard_truck_count;
	}

	public void setYard_truck_count(int yard_truck_count) {
		this.yard_truck_count = yard_truck_count;
	}

	public int getUnload_wait_time() {
		return unload_wait_time;
	}

	public void setUnload_wait_time(int unload_wait_time) {
		this.unload_wait_time = unload_wait_time;
	}

	public int getLoad_wait_time() {
		return load_wait_time;
	}

	public void setLoad_wait_time(int load_wait_time) {
		this.load_wait_time = load_wait_time;
	}

	public int getTotal_wait_time() {
		return total_wait_time;
	}

	public void setTotal_wait_time(int total_wait_time) {
		this.total_wait_time = total_wait_time;
	}

	public int getEntry_to_unload() {
		return entry_to_unload;
	}

	public void setEntry_to_unload(int entry_to_unload) {
		this.entry_to_unload = entry_to_unload;
	}

	public int getEntry_to_load() {
		return entry_to_load;
	}

	public void setEntry_to_load(int entry_to_load) {
		this.entry_to_load = entry_to_load;
	}

	public int getArrive_to_complete_unload() {
		return arrive_to_complete_unload;
	}

	public void setArrive_to_complete_unload(int arrive_to_complete_unload) {
		this.arrive_to_complete_unload = arrive_to_complete_unload;
	}

	public int getArrive_to_complete_load() {
		return arrive_to_complete_load;
	}

	public void setArrive_to_complete_load(int arrive_to_complete_load) {
		this.arrive_to_complete_load = arrive_to_complete_load;
	}

	public int getComplete_to_exit_unload() {
		return complete_to_exit_unload;
	}

	public void setComplete_to_exit_unload(int complete_to_exit_unload) {
		this.complete_to_exit_unload = complete_to_exit_unload;
	}

	public int getComplete_to_exit_load() {
		return complete_to_exit_load;
	}

	public void setComplete_to_exit_load(int complete_to_exit_load) {
		this.complete_to_exit_load = complete_to_exit_load;
	}

	public int getUnload_to_load() {
		return unload_to_load;
	}

	public void setUnload_to_load(int unload_to_load) {
		this.unload_to_load = unload_to_load;
	}

	public String getUnload_block() {
		return unload_block;
	}

	public void setUnload_block(String unload_block) {
		this.unload_block = unload_block;
	}

	public String getLoad_block() {
		return load_block;
	}

	public void setLoad_block(String load_block) {
		this.load_block = load_block;
	}

	public boolean isVisible() {
		return visible;
	}

	public void setVisible(boolean visible) {
		this.visible = visible;
	}

	@Override
	public String toString() {
		return "Simulator [number=" + number + ", code=" + code + ", entryTime=" + entryTime + ", arrive_unload_spot="
				+ arrive_unload_spot + ", start_unload_work=" + start_unload_work + ", complete_unload_work="
				+ complete_unload_work + ", arrive_load_spot=" + arrive_load_spot + ", start_load_work="
				+ start_load_work + ", complete_load_work=" + complete_load_work + ", out_time=" + out_time + ", block="
				+ block + ", unload_count=" + unload_count + ", load_count=" + load_count + ", yard_truck_count="
				+ yard_truck_count + ", unload_wait_time=" + unload_wait_time + ", load_wait_time=" + load_wait_time
				+ ", total_wait_time=" + total_wait_time + ", entry_to_unload=" + entry_to_unload + ", entry_to_load="
				+ entry_to_load + ", arrive_to_complete_unload=" + arrive_to_complete_unload
				+ ", arrive_to_complete_load=" + arrive_to_complete_load + ", complete_to_exit_unload="
				+ complete_to_exit_unload + ", complete_to_exit_load=" + complete_to_exit_load + ", unload_to_load="
				+ unload_to_load + ", unload_block=" + unload_block + ", load_block=" + load_block + ", visible="
				+ visible + "]";
	}

	
}
