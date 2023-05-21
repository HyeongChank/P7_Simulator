package com.simul;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Import;
import org.springframework.boot.CommandLineRunner;
import com.simul.domain.CorsConfig;
import com.simul.service.SimulService;

@SpringBootApplication
@Import(CorsConfig.class)
public class SimulatorApplication{
	

	public static void main(String[] args) {
		SpringApplication.run(SimulatorApplication.class, args);
	}

}
