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
public class SimulatorApplication implements CommandLineRunner{
	
	@Autowired
	private SimulService ssv;
	public static void main(String[] args) {
		SpringApplication.run(SimulatorApplication.class, args);
	}
	
	@Override
	public void run(String... args) throws Exception{
		String filePath = "C:/git clone/P7_simulation/P7_Simulator/sorted_truck_simulation_results.csv"; // 실제 CSV 파일 경로로 수정
        List<String[]> records = ssv.readCsvFile(filePath);
        // 읽은 CSV 파일 데이터(records)를 원하는 방식으로 처리
        for (String[] fields : records) {
            // 각 필드에 대한 처리 로직 작성
            for (String field : fields) {
                System.out.print(field + " ");
            }
            System.out.println();
        }
	}

}
