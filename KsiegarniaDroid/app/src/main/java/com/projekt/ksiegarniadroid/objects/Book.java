package com.projekt.ksiegarniadroid.objects;

import android.content.Intent;

/**
 * Created by Sebo on 2016-11-27.
 */

public class Book
{
    private _id[] authors;

    private String cover;

    private String title;

    private Double price;

    private _id _id;

    private String ISBN;

    private String description;

    private String[] tableOfContents;

    private Integer lendPrice;

    private Boolean isEbook;

    private String availability;

    public _id[] getAuthors ()
    {
        return authors;
    }

    public void setAuthors (_id[] authors)
    {
        this.authors = authors;
    }

    public String getCover ()
    {
        return cover;
    }

    public void setCover (String cover)
    {
        this.cover = cover;
    }

    public String getTitle ()
    {
        return title;
    }

    public void setTitle (String title)
    {
        this.title = title;
    }

    public Double getPrice ()
    {
        return price;
    }

    public void setPrice (Double price)
    {
        this.price = price;
    }

    public _id get_id ()
    {
        return _id;
    }

    public void set_id (_id _id)
    {
        this._id = _id;
    }

    public String getISBN ()
    {
        return ISBN;
    }

    public void setISBN (String ISBN)
    {
        this.ISBN = ISBN;
    }

    public String getDescription ()
    {
        return description;
    }

    public void setDescription (String description)
    {
        this.description = description;
    }

    public String[] getTableOfContents ()
    {
        return tableOfContents;
    }

    public void setTableOfContents (String[] tableOfContents)
    {
        this.tableOfContents = tableOfContents;
    }

    public Integer getLendPrice ()
{
    return lendPrice;
}

    public void setLendPrice (Integer lendPrice)
    {
        this.lendPrice = lendPrice;
    }


    public String getAvailability ()
    {
        return availability;
    }

    public void setAvailability (String availability)
    {
        this.availability = availability;
    }

    @Override
    public String toString()
    {
        return "[authors = "+authors+", cover = "+cover+", title = "+title+", price = "+price+", _id = "+_id+", ISBN = "+ISBN+", description = "+description+", tableOfContents = "+tableOfContents+", lendPrice = "+lendPrice+", isEbook = "+isEbook+", availability = "+availability+"]";
    }

    public void setIsEbook(Boolean ebook) {
        isEbook = ebook;
    }

    public Boolean getIsEbook(){
        return isEbook;
    }
}
