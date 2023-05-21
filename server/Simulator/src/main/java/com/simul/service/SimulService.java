package com.simul.service;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.ResourceUtils;

import com.simul.controller.SimulController;
import com.simul.domain.Simulator;

@Service
public class SimulService {
	
//	@Autowired
//	SimulController sc;
	
	private List<Simulator> sm = new ArrayList<>();
	
    public List<String[]> readCsvFile(String filePath) throws IOException {
    	
        List<String[]> records = new ArrayList<>();
        BufferedReader reader = null;
        boolean isFirstLine = true;
        try {
        	
            reader = new BufferedReader(new FileReader(ResourceUtils.getFile(filePath)));
            String line;
            while ((line = reader.readLine()) != null) {
            	if(isFirstLine) {
            		isFirstLine = false;
            		continue;
            	}
            	
                String[] fields = line.split(","); // CSV 파일의 필드 구분자에 맞게 수정
//            	String number_before=  fields[0];
//            	Long number = Long.parseLong(number_before);
//            	String code =fields[1];
//            	String entryTime_before = fields[2];
//            	int entryTime = Integer.parseInt(entryTime_before);
//            	boolean visible = true;
//            	Simulator smr = new Simulator(number, code, entryTime, visible);
//            	sm.add(smr);
                records.add(fields);
            }
        } finally {
            if (reader != null) {
                reader.close();
            }
        }
 
        return records;
    }
//    public List<Simulator> get_truck_data(){
//    	return sm;
//    }

}
