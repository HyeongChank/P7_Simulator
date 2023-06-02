package com.simul.controller;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
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

@CrossOrigin(origins = "http://localhost:3000")
@RestController
public class SimulController {

	@Autowired
	SimulService ssv;

//	@GetMapping("/api/truckData")
//	public List<Simulator> truckDataSend(){
//		
//		return ssv.outData();
//	}
	
	@GetMapping("/api/truckData")
	public List<Simulator> truck_csv_data() throws IOException {
		List<Simulator>sm = ssv.readCsvFile();
		return sm;
	}
	
	
//	{
//	    "json_output": [
//	        {
//	            "arrive_load_spot": "0",
//	            "arrive_unload_spot": "22",
//	            "code": "unload",
//	            "complete_load_work": "0",
//	            "complete_unload_work": "34",
//	            "entryTime": "17",
//	            "entry_count": "5",
//	            "exit_count": "1",
//	            "load_block": "X",
//	            "load_count": "0",
//	            "load_progress_truck_count": "0",
//	            "number": "5",
//	            "op": "unload",
//	            "out_time": "39",
//	            "spot_wait_time": "0",
//	            "start_load_work": "0",
//	            "start_unload_work": "22",
//	            "unload_block": "B",
//	            "unload_count": "0",
//	            "unload_progress_truck_count": "0",
//	            "visible": "True",
//	            "work_time": "22"
//	        }
//	    ]
//	}
	@PostMapping("/api/simul_predict")
	public ResponseEntity<?> insertSimul(@RequestBody Map<String, List<Simulator>> data){
		System.out.println("success");
		
		 // 플라스크 API 엔드포인트 설정
        String flaskApiUrl = "http://10.125.121.220:5003/api/simul_predict";
        RestTemplate restTemplate = new RestTemplate();
        Map<String, List<Simulator>> mapsimul = new HashMap<>();
        HttpHeaders headers = new HttpHeaders();
        headers.set(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE);

        HttpEntity<Map<String, List<Simulator>>> entity = new HttpEntity<>(mapsimul, headers);
        ResponseEntity<Map<String, List<Simulator>>> response = restTemplate.exchange(
        		flaskApiUrl,
        		HttpMethod.POST,
        		entity,
        		new ParameterizedTypeReference<Map<String, List<Simulator>>>() {});
        Map<String, List<Simulator>> simulBody = response.getBody();
        List<Simulator> simullist = simulBody.get("json_output");
        System.out.println(simullist.size());

        return ssv.insertSimul(simullist);
	}
	
	

	@PostMapping("/api/cnn_predict")
	public ResponseEntity<?> cnnPrediction(@RequestBody Map<String, List<String>> data) {
	    
	    System.out.println("pass");
	    String flaskApiUrl = "http://10.125.121.220:5001/api/cnn_time_predict";
//      RestTemplate을 사용하여 플라스크로 POST 요청 전송
        RestTemplate restTemplate = new RestTemplate();
        Map<String, List<String>> ls = new HashMap<>();
//		요청데이터 설정
//      HttpEntity 객체 생성 및 요청 데이터와 헤더 설정        
        HttpHeaders headers = new HttpHeaders();
        headers.set(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE);
        HttpEntity<Map<String, List<String>>> entity = new HttpEntity<>(ls, headers);

//      estTemplate을 사용하여 플라스크로 POST 요청 전송
        ResponseEntity<Map<String, List<String>>> response = restTemplate.exchange(
        		flaskApiUrl,
        		HttpMethod.POST,
        		entity,
        		new ParameterizedTypeReference<Map<String, List<String>>>() {});
    	Map<String, List<String>> responseBody = response.getBody();
    	List<String> timeGroup = responseBody.get("time");
	    List<String> predictGroup = responseBody.get("predict_group");
	    List<String> actualGroup = responseBody.get("actual_group");
	    System.out.println("pass2");
	    for(int i=0; i< timeGroup.size(); i++) {
	    	System.out.println(timeGroup.get(i) +" " + predictGroup.get(i) + " " +actualGroup.get(i));
	    }
//        if(response.getStatusCode() == HttpStatus.OK) {
//    
//        }
//        else {
//        	System.out.println("error");
//        }
     // ResponseEntity에서 응답 본문 가져오기
       // Map<String, List<String>> body = response.getBody();
	    return ResponseEntity.ok().body("success");
	}
	


}
