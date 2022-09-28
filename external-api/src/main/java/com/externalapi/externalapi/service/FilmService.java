package com.externalapi.externalapi.service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.externalapi.externalapi.model.Film;

@Service
public class FilmService {
    
    @Autowired
    private RestTemplate template = new RestTemplate();

    public Object[] findAllFilmsComplete(){
        return template.getForObject("https://ghibliapi.herokuapp.com/films", Object[].class);
    }
    public Film[] findAllFilms(){
        return template.getForObject("https://ghibliapi.herokuapp.com/films", Film[].class);
    }
    public List<Film> findFilmsByTitle(String title){
        List<Film> filmList = new ArrayList<>();
        Film[] forObject = template.getForObject("https://ghibliapi.herokuapp.com/films", Film[].class);
        for (Film film : forObject){
            if (film.getTitle().toLowerCase().contains(title) || film.getOriginalTitle().toLowerCase().contains(title)){
                filmList.add(film);
            }
        }
        return filmList;
    }
    public List<Film> findFilmsByProducer(String producer){
        List<Film> filmList = new ArrayList<>();
        Film[] forObject = template.getForObject("https://ghibliapi.herokuapp.com/films", Film[].class);
        for (int i = 0; i < forObject.length; i++){
            Film film = forObject[i];
            if (film.getProducer().toLowerCase().contains(producer)){
                filmList.add(film);
            }
        }
        return filmList;
    }
    public Map<Integer, String> findDirectors(){
        Map<Integer, String> map = new HashMap<>();
        Film[] filmList = template.getForObject("https://ghibliapi.herokuapp.com/films", Film[].class);
        int mapKey = 1;
        for (Film film : filmList){
            if (!map.containsValue(film.getDirector())){
                map.put(mapKey, film.getDirector());
                mapKey++;
            }
        }
        return map;
    }

}
