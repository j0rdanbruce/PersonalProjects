package com.externalapi.externalapi.controller;

import java.util.List;
import java.util.Map;

import com.externalapi.externalapi.model.Film;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.externalapi.externalapi.service.FilmService;

@RequestMapping("/")
@Controller
public class FilmController {
    
    @Autowired
    private FilmService filmService;

    @GetMapping("/index")
    public String homePage(Model model){
        return "homePage";
    }

    @GetMapping("/complete")
    public Object[] getAllFilmsComplete(){
        return filmService.findAllFilmsComplete();
    }

    @GetMapping("/")
    public Film[] getAllFilms(){
        return filmService.findAllFilms();
    }

    @GetMapping("/title")
    public List<Film> getlFilmsByTitle(@RequestParam("q") String title){
        return filmService.findFilmsByTitle(title); 
    }

    @GetMapping("/producer")
    public List<Film> getFilmsByProducer(@RequestParam("q") String producer){
        return filmService.findFilmsByProducer(producer);
    }

    @GetMapping("/specificProducer")
    //get name of specific producer from user...eventually return a web page of all movies made by certain producer
    public String getSpecificProducer(@RequestParam("producer") String producer, Model model){
        producer = producer.substring(0, 1).toUpperCase() + producer.substring(1);
        List<Film> filmProducerList = filmService.findFilmsByProducer(producer);
        model.addAttribute("films", filmProducerList);
        model.addAttribute("producer", producer);
        //model.addAttribute("film1", filmProducerList.get(0));
        return "filmsByProducer";
    }

    @GetMapping("/directors")
    public Map<Integer, String> getDirectors(){
        return filmService.findDirectors();
    }


}
