package com.cs5351.course.project5.api.repositories;

import com.cs5351.course.project5.api.entities.Form;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FormRepository extends CrudRepository<Form, Integer> {
    
}