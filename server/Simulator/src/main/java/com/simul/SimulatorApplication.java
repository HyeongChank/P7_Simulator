package com.simul;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Import;

import com.simul.domain.CorsConfig;

@SpringBootApplication
@Import(CorsConfig.class)
public class SimulatorApplication {

	public static void main(String[] args) {
		SpringApplication.run(SimulatorApplication.class, args);
	}

}
