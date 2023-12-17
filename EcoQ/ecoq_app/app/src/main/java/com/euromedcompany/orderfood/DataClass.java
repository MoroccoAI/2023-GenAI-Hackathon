package com.euromedcompany.orderfood;

public class DataClass {
    private String title, type, desc, imageURL;

    public DataClass(){

    }
    public DataClass(String imageURL, String title, String type, String desc) {
        this.imageURL = imageURL;
        this.title = title;
        this.type = type;
        this.desc = desc;
    }
    public String getImageURL() {
        return imageURL;
    }
    public void setImageURL(String imageURL) {
        this.imageURL = imageURL;
    }

    public String getTitle() {
        return title;
    }
    public void setTitle(String title) {
        this.title = title;
    }

    public String getType() {
        return type;
    }
    public void setType(String type) {
        this.type = type;
    }

    public String getDesc() {
        return desc;
    }
    public void setDesc(String desc) {
        this.desc = desc;
    }
}