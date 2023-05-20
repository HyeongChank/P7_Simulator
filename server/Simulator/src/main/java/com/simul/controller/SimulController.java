package com.simul.controller;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.simul.domain.Simulator;


@RestController
@RequestMapping("/api/truckData")
public class SimulController {


	@GetMapping
    public List<Simulator> getTruckData() {
		Simulator sm1 = new Simulator((long) 1, "out", 1000, true);
		Simulator sm2 = new Simulator((long) 2, "in", 2000, true);
		Simulator sm3 = new Simulator((long) 3, "out", 3000, true);
		Simulator sm4 = new Simulator((long) 4, "in_out", 4000, true);
		Simulator sm5 = new Simulator((long) 5, "in_out", 5000, true);
		
		List<Simulator> ls = new ArrayList<>();
		ls.add(sm1);
		ls.add(sm2);
		ls.add(sm3);
		ls.add(sm4);
		ls.add(sm5);
		System.out.println(ls);
        return	ls; 
    }	
}
