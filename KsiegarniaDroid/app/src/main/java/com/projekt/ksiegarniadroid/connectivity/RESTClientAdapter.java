package com.projekt.ksiegarniadroid.connectivity;

import com.projekt.ksiegarniadroid.exceptions.RESTClientException;
import com.projekt.ksiegarniadroid.objects.Author;
import com.projekt.ksiegarniadroid.objects.Book;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * Created by Sebo on 2016-11-14.
 */

public class RESTClientAdapter {

    private static final String URL = "http://10.0.2.2:8080";

    public static ArrayList<Author> getAllAuthors() throws RESTClientException {
        return new ArrayList<>(Arrays.asList(RESTClient.doGet(URL, "authors", Author[].class)));
    }

    public static ArrayList<Book> getAllBooks() throws RESTClientException {
        return new ArrayList<>(Arrays.asList(RESTClient.doGet(URL, "books", Book[].class)));
    }

}
