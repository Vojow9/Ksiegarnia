package com.projekt.ksiegarniadroid.objects;

import java.io.Serializable;

/**
 * Created by Sebo on 2016-11-27.
 */

public class Book implements Serializable {
    private String id;

    private String bookid;

    private String[] authors;

    private String title;

    private String price;

    private String ISBN;

    private String description;

    private String[] tableOfContents;

    private boolean isEbook;

    private int availability;

    private String purchasedate;

    private byte[] bookCover;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String[] getAuthors() {
        return authors;
    }

    public void setAuthors(String[] authors) {
        this.authors = authors;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public String getISBN() {
        return ISBN;
    }

    public void setISBN(String ISBN) {
        this.ISBN = ISBN;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String[] getTableOfContents() {
        return tableOfContents;
    }

    public void setTableOfContents(String[] tableOfContents) {
        this.tableOfContents = tableOfContents;
    }

    public void setEbook(boolean ebook) {
        isEbook = ebook;
    }

    public boolean getEbook() {
        return isEbook;
    }

    public int getAvailability() {
        return availability;
    }

    public void setAvailability(int availability) {
        this.availability = availability;
    }

    public byte[] getBookCover() {
        return bookCover;
    }

    public void setBookCover(byte[] bookCover) {
        this.bookCover = bookCover;
    }

    public String getPurchasedate() {
        return purchasedate;
    }

    public void setPurchasedate(String purchasedate) {
        this.purchasedate = purchasedate;
    }

    public String getBookid() {
        return bookid;
    }

    public void setBookid(String bookid) {
        this.bookid = bookid;
    }
}