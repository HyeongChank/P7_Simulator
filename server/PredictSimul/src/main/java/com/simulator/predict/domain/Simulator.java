package com.simulator.predict.domain;

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
    private int work_time;
    private String op;
    private int unload_count;
    private int load_count;
    private String unload_block;
    private String load_block;
    private int entry_count;
    private int exit_count;
    
    private int spot_wait_time;
    
    private int container_status;
    private int container_size;
    private int in_yard_count;
    private float prediction;
    private int realdata;
    
    
    
     
    private int entry_to_unload;
    private int entry_to_load;
    private int arrive_to_complete_unload;
    private int arrive_to_complete_load;
    private int complete_to_exit_unload;
    private int complete_to_exit_load;
    private int unload_to_load;
    private int unload_wait_time;
    private int load_wait_time;
    private int unload_progress_truck_count;
    private int load_progress_truck_count;

    private boolean visible;

    public Simulator() {
    	
    }

	public Simulator(Long number, String code, int entryTime, int arrive_unload_spot, int start_unload_work,
			int complete_unload_work, int arrive_load_spot, int start_load_work, int complete_load_work, int out_time,
			int work_time, String op, int unload_count, int load_count, String unload_block, String load_block,
			int entry_count, int exit_count, int spot_wait_time, int container_status, int container_size,
			int in_yard_count, float prediction, int realdata, int entry_to_unload, int entry_to_load,
			int arrive_to_complete_unload, int arrive_to_complete_load, int complete_to_exit_unload,
			int complete_to_exit_load, int unload_to_load, int unload_wait_time, int load_wait_time,
			int unload_progress_truck_count, int load_progress_truck_count, boolean visible) {
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
		this.work_time = work_time;
		this.op = op;
		this.unload_count = unload_count;
		this.load_count = load_count;
		this.unload_block = unload_block;
		this.load_block = load_block;
		this.entry_count = entry_count;
		this.exit_count = exit_count;
		this.spot_wait_time = spot_wait_time;
		this.container_status = container_status;
		this.container_size = container_size;
		this.in_yard_count = in_yard_count;
		this.prediction = prediction;
		this.realdata = realdata;
		this.entry_to_unload = entry_to_unload;
		this.entry_to_load = entry_to_load;
		this.arrive_to_complete_unload = arrive_to_complete_unload;
		this.arrive_to_complete_load = arrive_to_complete_load;
		this.complete_to_exit_unload = complete_to_exit_unload;
		this.complete_to_exit_load = complete_to_exit_load;
		this.unload_to_load = unload_to_load;
		this.unload_wait_time = unload_wait_time;
		this.load_wait_time = load_wait_time;
		this.unload_progress_truck_count = unload_progress_truck_count;
		this.load_progress_truck_count = load_progress_truck_count;
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

	public int getWork_time() {
		return work_time;
	}

	public void setWork_time(int work_time) {
		this.work_time = work_time;
	}

	public String getOp() {
		return op;
	}

	public void setOp(String op) {
		this.op = op;
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

	public int getEntry_count() {
		return entry_count;
	}

	public void setEntry_count(int entry_count) {
		this.entry_count = entry_count;
	}

	public int getExit_count() {
		return exit_count;
	}

	public void setExit_count(int exit_count) {
		this.exit_count = exit_count;
	}

	public int getSpot_wait_time() {
		return spot_wait_time;
	}

	public void setSpot_wait_time(int spot_wait_time) {
		this.spot_wait_time = spot_wait_time;
	}

	public int getContainer_status() {
		return container_status;
	}

	public void setContainer_status(int container_status) {
		this.container_status = container_status;
	}

	public int getContainer_size() {
		return container_size;
	}

	public void setContainer_size(int container_size) {
		this.container_size = container_size;
	}

	public int getIn_yard_count() {
		return in_yard_count;
	}

	public void setIn_yard_count(int in_yard_count) {
		this.in_yard_count = in_yard_count;
	}

	public float getPrediction() {
		return prediction;
	}

	public void setPrediction(float prediction) {
		this.prediction = prediction;
	}

	public int getRealdata() {
		return realdata;
	}

	public void setRealdata(int realdata) {
		this.realdata = realdata;
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

	public int getUnload_progress_truck_count() {
		return unload_progress_truck_count;
	}

	public void setUnload_progress_truck_count(int unload_progress_truck_count) {
		this.unload_progress_truck_count = unload_progress_truck_count;
	}

	public int getLoad_progress_truck_count() {
		return load_progress_truck_count;
	}

	public void setLoad_progress_truck_count(int load_progress_truck_count) {
		this.load_progress_truck_count = load_progress_truck_count;
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
				+ start_load_work + ", complete_load_work=" + complete_load_work + ", out_time=" + out_time
				+ ", work_time=" + work_time + ", op=" + op + ", unload_count=" + unload_count + ", load_count="
				+ load_count + ", unload_block=" + unload_block + ", load_block=" + load_block + ", entry_count="
				+ entry_count + ", exit_count=" + exit_count + ", spot_wait_time=" + spot_wait_time
				+ ", container_status=" + container_status + ", container_size=" + container_size + ", in_yard_count="
				+ in_yard_count + ", prediction=" + prediction + ", realdata=" + realdata + ", entry_to_unload="
				+ entry_to_unload + ", entry_to_load=" + entry_to_load + ", arrive_to_complete_unload="
				+ arrive_to_complete_unload + ", arrive_to_complete_load=" + arrive_to_complete_load
				+ ", complete_to_exit_unload=" + complete_to_exit_unload + ", complete_to_exit_load="
				+ complete_to_exit_load + ", unload_to_load=" + unload_to_load + ", unload_wait_time="
				+ unload_wait_time + ", load_wait_time=" + load_wait_time + ", unload_progress_truck_count="
				+ unload_progress_truck_count + ", load_progress_truck_count=" + load_progress_truck_count
				+ ", visible=" + visible + "]";
	}



}