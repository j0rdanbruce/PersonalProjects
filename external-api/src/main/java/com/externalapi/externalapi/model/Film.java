package com.externalapi.externalapi.model;

public class Film {
    private String title;
    private String original_title;
    private String original_title_romanised;
    private String producer;
    private String director;

    public String getTitle(){
        return title;
    }
    public String getOriginalTitle(){
        return original_title;
    }    
    public String getOriginalTitleRomanised(){
        return original_title_romanised;
    }
    public String getProducer(){
        return producer;
    }
    public String getDirector(){
        return director;
    }
}
