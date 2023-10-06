package com.cs5351.course.project5.api.controllers;

import com.cs5351.course.project5.api.entities.Form;
import com.cs5351.course.project5.api.services.FormService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
public class FormController {

    public FormService formService;
    
    public FormController(FormService formService) {
        this.formService = formService;
    }

    @PostMapping("/forms")
    public ResponseEntity<Form> createForm(@RequestBody Form form){
        Form formcreated = formService.create(form);
        return new ResponseEntity<>(formcreated, HttpStatus.CREATED);
    }

    @GetMapping("/forms")
    public ResponseEntity<List<Form>> allForms(){
        List<Form> forms = formService.findAll();
        return new ResponseEntity<>(forms, HttpStatus.OK);
    }

    @GetMapping("/forms/{id}")
    public ResponseEntity<Form> oneTask(@PathVariable int id) {
        Optional<Form> optionalForm = formService.findById(id);

        if (optionalForm.isPresent()) {
            return new ResponseEntity<>(optionalForm.get(), HttpStatus.OK);
        }

        return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    @PatchMapping("/forms/{id}")
    public ResponseEntity<Form> updateTask(@PathVariable int id, @RequestBody Form form) {
        Optional<Form> optionalForm = formService.findById(id);
        
        if (!optionalForm.isPresent()) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }

        Form formToUpdate = optionalForm.get();

        formToUpdate.setName(form.getName());
        formToUpdate.setEmail(form.getEmail());
        formToUpdate.setMessage(form.getMessage());

        Form formUpdated = formService.update(formToUpdate);

        return new ResponseEntity<>(formUpdated, HttpStatus.OK);
    }

    @DeleteMapping("/forms/{id}")
    public ResponseEntity<Void> deleteTask(@PathVariable int id) {
        formService.delete(id);

        return ResponseEntity.noContent().build();
    }
    
}