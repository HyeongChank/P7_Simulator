package com.simul.controller;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.simul.domain.Simulator;
import com.simul.service.SimulService;

import jakarta.annotation.PostConstruct;

@CrossOrigin(origins = "http://localhost:5001")
@RestController
public class SimulController {

	@Autowired
	SimulService ssv;

//	@GetMapping
//	public List<Simulator> truck_csv_data() throws IOException {
//		List<Simulator>sm = ssv.readCsvFile();
//		return sm;
//
//	}	
	@PostMapping("/api/simul_predict")
	public ResponseEntity<String> insertSimul(){
		System.out.println("success");
		
		 // 플라스크 API 엔드포인트 설정
        String flaskApiUrl = "http://10.125.121.220:5001/api/simul_predict";

        // RestTemplate을 사용하여 플라스크로 POST 요청 전송
        RestTemplate restTemplate = new RestTemplate();

		List<Simulator> smlist = new ArrayList<>();
//		for(int i=0; i<2L; i++) {
//			smlist.add(sm);
//		}
		
		
		 // HttpHeaders 객체 생성 및 Content-Type 설정
        HttpHeaders headers = new HttpHeaders();
        headers.set(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE);
        // ResponseEntity 는 헤더와 데이터가 같이 있어서 데이터를 분리해서 봐야 함
        // HttpEntity 객체 생성 및 요청 데이터와 헤더 설정
        HttpEntity<List<Simulator>> entity = new HttpEntity<>(smlist, headers);
//        ResponseEntity<List<Simulator>> response = restTemplate.exchange(flaskApiUrl, HttpMethod.POST, entity, new ParameterizedTypeReference<List<Simulator>>() {});
//        List<Simulator> simulatorList = response.getBody();

//        // RestTemplate을 사용하여 플라스크로 POST 요청 전송
        ResponseEntity<String> response = restTemplate.exchange(flaskApiUrl, HttpMethod.POST, entity, String.class);
//		for(int i=0 ; i< simulatorList.size(); i++) {
//	        System.out.println(simulatorList);			
//		}

        return ssv.insertSimul(response);
	}

	
//	@PostMapping("/simul_predict")
//	public String postSimulPrediction() {
//	    // API URL
//	    final String url = "http://localhost:5001/api/simul_predict";
//
//	    // RestTemplate 인스턴스 생성
//	    RestTemplate restTemplate = new RestTemplate();
//	    System.out.println("pass");
//	    // POST 메서드에 필요한 헤더 생성
//	    HttpHeaders headers = new HttpHeaders();
//	    headers.add("Content-Type", "application/json");
//	    headers.add("Accept", "*/*");
//
//	    // HttpEntity에 헤더와, 필요하다면 body 정보를 추가
//	    HttpEntity<String> entity = new HttpEntity<>(headers);
//
//	    // POST 요청을 보내고 결과를 받아옴
//	    ResponseEntity<String> result = restTemplate.exchange(url, HttpMethod.POST, entity, String.class);
//	    System.out.println(result);
//	    // 결과를 반환함
//	    return result.getBody();
//	}
}
