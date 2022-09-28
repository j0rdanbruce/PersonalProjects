package com.externalapi.externalapi.model;

import java.util.List;

public class User {
    private String username;
    private String password;
    private List<Film> favoriteFilms;

    //public User(){}
    
    public User(String username, String password, List<Film> favoriteFilms){
        this.username = username;
        this.password = password;
        this.favoriteFilms = favoriteFilms;
    }
    private String getUsername(){
        return username;
    }
    private String getPassword(){
        return password;
    }
    private List<Film> getFavoriteFilms(){
        return favoriteFilms;
    }
    private void setUsername(String username){
        this.username = username;
    }
    private void setPassword(String password){
        this.password = password;
    }
    private void setFavoriteFilms(List<Film> newList){
        this.favoriteFilms = newList;
    }
    //add film to your favorite list
    private void addFilmToFavoriteList(Film film){
        favoriteFilms.add(film);
    }
    
}
