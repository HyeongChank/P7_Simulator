package com.simulator.predict.persistence;

import org.springframework.data.repository.CrudRepository;

import com.simulator.predict.domain.Simulator;

public interface SimulRepository extends CrudRepository<Simulator, Long> {

}
