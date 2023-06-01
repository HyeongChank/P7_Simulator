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
import java.util.Map;

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
		 // HttpHeaders 객체 생성 및 Content-Type 설정
        HttpHeaders headers = new HttpHeaders();
        headers.set(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE);
        // ResponseEntity 는 헤더와 데이터가 같이 있어서 데이터를 분리해서 봐야 함
        // HttpEntity 객체 생성 및 요청 데이터와 헤더 설정
        HttpEntity<List<Simulator>> entity = new HttpEntity<>(smlist, headers);



//        // RestTemplate을 사용하여 플라스크로 POST 요청 전송
        ResponseEntity<String> response = restTemplate.exchange(flaskApiUrl, HttpMethod.POST, entity, String.class);
        ResponseEntity<Simulator> response2 = restTemplate.exchange(flaskApiUrl, HttpMethod.POST, entity, new ParameterizedTypeReference<Simulator>() {});
        Simulator sm = response2.getBody();
//		for(int i=0 ; i< simulatorList.size(); i++) {
//	        System.out.println(simulatorList);			
//		}

        return ssv.insertSimul(response);
	}

	@PostMapping("/api/cnn_predict")
	public ResponseEntity<?> cnnPrediction(@RequestBody Map<String, List<String>> data) {
	    List<String> timeGroup = data.get("time");
	    List<String> predictGroup = data.get("predict_group");
	    List<String> actualGroup = data.get("actual_group");
	    System.out.println("pass");
	    String flaskApiUrl = "http://10.125.121.220:5001/api/cnn_time_predict";
//        // RestTemplate을 사용하여 플라스크로 POST 요청 전송
        RestTemplate restTemplate = new RestTemplate();
        String ls = "post";
        //		
//		 // HttpHeaders 객체 생성 및 Content-Type 설정
        HttpHeaders headers = new HttpHeaders();
        headers.set(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE);
//        // ResponseEntity 는 헤더와 데이터가 같이 있어서 데이터를 분리해서 봐야 함
//        // HttpEntity 객체 생성 및 요청 데이터와 헤더 설정
        HttpEntity<String> entity = new HttpEntity<>(ls, headers);
//
//
//
////        // RestTemplate을 사용하여 플라스크로 POST 요청 전송
        ResponseEntity<String> response = restTemplate.exchange(flaskApiUrl, HttpMethod.POST, entity, String.class);
    	System.out.println(response);
////		for(int i=0 ; i< simulatorList.size(); i++) {
////	        System.out.println(simulatorList);			
////		}
//
//	    // 데이터 처리 로직

	    return ResponseEntity.ok().body("success");
	}


}
