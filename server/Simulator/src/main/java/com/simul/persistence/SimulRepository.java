package com.simul.persistence;

import org.springframework.data.repository.CrudRepository;

import com.simul.domain.Simulator;

public interface SimulRepository extends CrudRepository<Simulator, Long> {

}
