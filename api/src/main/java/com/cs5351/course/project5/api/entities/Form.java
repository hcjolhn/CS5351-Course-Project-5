package com.cs5351.course.project5.api.entities;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import javax.persistence.*;
import java.util.Date;

@Table(name="form")
@Entity
public class Form {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(nullable = false)
    private Integer id;

    private String name;

    private String email;

    private String message;

    @CreationTimestamp
    @Column(updatable = false, name = "create_dt")
    private Date createdDt;

    @UpdateTimestamp
    @Column(name = "updated_dt")
    private Date updatedDt;

    public Integer getId(){
        return id;
    }

    public String getName(){
        return name;
    }

    public String getEmail(){
        return email;
    }

    public String getMessage(){
        return message;
    }

    public Date getCreateDt(){
        return createdDt;
    }

    public Date getUpdateDt(){
        return updatedDt;
    }

    public void setId(Integer id){
        this.id = id;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public void setMessage(String message){
        this.message = message;
    }

    public void setCreateDt(Date createdDt){
        this.createdDt = createdDt;
    }

    public void setUpdateDt(Date updatedDt){
        this.updatedDt = updatedDt;
    }
}