package com.cs5351.course.project5.api.services;

import com.cs5351.course.project5.api.entities.Form;
import com.cs5351.course.project5.api.repositories.FormRepository;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import org.springframework.stereotype.Service;

@Service
public class FormService {

    private final FormRepository formRepository;

    public FormService (FormRepository formRepository){
        this.formRepository = formRepository;
    }

    public Form create(Form form){
        return formRepository.save(form);
    }

    public List<Form> findAll(){
        List<Form> forms = new ArrayList<>();
        formRepository.findAll().forEach(forms::add);
        return forms;
    }

    public Optional<Form> findById(int id) {
        return formRepository.findById(id);
    }

    public Form update(Form formToUpdate) {
        return formRepository.save(formToUpdate);
    }

    public void delete(int id) {
        formRepository.deleteById(id);
    }
    
}