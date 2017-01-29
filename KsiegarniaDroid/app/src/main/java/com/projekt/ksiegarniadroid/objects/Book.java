package com.projekt.ksiegarniadroid.objects;

/**
 * Created by Sebo on 2016-11-27.
 */

public class Book
{
    private String id;

    private String[] authors;

    private String title;

    private String price;

    private String ISBN;

    private String description;

    private String[] tableOfContents;

    private String isEbook;

    private String availability;

    private byte[] bookCover;

    public String getId ()
    {
        return id;
    }

    public void setId (String id)
    {
        this.id = id;
    }

    public String[] getAuthors ()
    {
        return authors;
    }

    public void setAuthors (String[] authors)
    {
        this.authors = authors;
    }

    public String getTitle ()
    {
        return title;
    }

    public void setTitle (String title)
    {
        this.title = title;
    }

    public String getPrice ()
    {
        return price;
    }

    public void setPrice (String price)
    {
        this.price = price;
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

    public String getIsEbook ()
    {
        return isEbook;
    }

    public void setIsEbook (String isEbook)
    {
        this.isEbook = isEbook;
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
        return "ClassPojo [id = "+id+", authors = "+authors+", title = "+title+", price = "+price+", ISBN = "+ISBN+", description = "+description+", tableOfContents = "+tableOfContents+", isEbook = "+isEbook+", availability = "+availability+"]";
    }

    public byte[] getBookCover() {
        return bookCover;
    }

    public void setBookCover(byte[] bookCover) {
        this.bookCover = bookCover;
    }
}