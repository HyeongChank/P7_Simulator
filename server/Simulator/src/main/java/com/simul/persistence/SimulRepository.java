package com.simul.persistence;

import org.springframework.data.repository.CrudRepository;

import com.simul.domain.Simulator;
import java.util.List;
public interface SimulRepository extends CrudRepository<Simulator, Long> {
	List<Simulator> findAll();
}
