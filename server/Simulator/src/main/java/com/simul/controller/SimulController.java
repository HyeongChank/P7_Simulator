package com.simul.controller;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.simul.domain.Simulator;
import com.simul.service.SimulService;


@RestController
@RequestMapping("/api/truckData")
public class SimulController {

	@Autowired
	SimulService ssv;
//	@GetMapping
//    public List<Simulator> getTruckData() {
//		Simulator sm1 = new Simulator((long) 1, "out", 1000, true);
//		Simulator sm2 = new Simulator((long) 2, "in", 2000, true);
//		Simulator sm3 = new Simulator((long) 3, "out", 3000, true);
//		Simulator sm4 = new Simulator((long) 4, "in_out", 4000, true);
//		Simulator sm5 = new Simulator((long) 5, "in_out", 5000, true);
//		Simulator sm6 = new Simulator((long) 6, "in", 6000, true);
//		Simulator sm7 = new Simulator((long) 7, "out", 7000, true);
//		Simulator sm8 = new Simulator((long) 8, "in_out", 8000, true);
//		
//		List<Simulator> ls = new ArrayList<>();
//		ls.add(sm1);
//		ls.add(sm2);
//		ls.add(sm3);
//		ls.add(sm4);
//		ls.add(sm5);
//		ls.add(sm6);
//		ls.add(sm7);
//		ls.add(sm8);
//		System.out.println(ls);
//        return	ls; 
//    }
	@GetMapping
	public List<Simulator> truck_csv_data() throws IOException {
		List<Simulator>sm = ssv.readCsvFile();
		return sm;

	}	
}
