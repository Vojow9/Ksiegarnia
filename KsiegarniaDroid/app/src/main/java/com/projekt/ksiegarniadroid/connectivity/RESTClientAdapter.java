package com.projekt.ksiegarniadroid.connectivity;

import com.projekt.ksiegarniadroid.exceptions.RESTClientException;
import com.projekt.ksiegarniadroid.objects.Author;
import com.projekt.ksiegarniadroid.objects.Book;
import com.projekt.ksiegarniadroid.objects.Customer;
import com.projekt.ksiegarniadroid.utils.SharedPreferencesAdapter;

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

    public static ArrayList<Book> getAuthorBooks(String authorId) throws RESTClientException {
        return new ArrayList<>(Arrays.asList(RESTClient.doGet(URL, "books/author/" + authorId , Book[].class)));
    }
    public static byte[] getBookCover(String bookId) throws RESTClientException {
        return RESTClient.doGetPicture(URL, "bookcovers/" + bookId);
    }

    public static Customer login(String userName, String password) throws RESTClientException {
        return RESTClient.doGet(URL,"customers/"+ userName, userName, password, Customer.class);
    }

    public static void register(Customer newUser) throws RESTClientException {
        RESTClient.doPost(URL, "customers", "", "", newUser);
    }

    public static void buy(ArrayList<String> books) throws RESTClientException {
        RESTClient.doPost(URL, "customers/availablebooks/" + SharedPreferencesAdapter.Instance().getLogin(), SharedPreferencesAdapter.Instance().getLogin(), SharedPreferencesAdapter.Instance().getLoginPassword(), books);
    }

    public static ArrayList<Book> getBoughtBooks() throws RESTClientException {
        return new ArrayList<>(Arrays.asList(RESTClient.doGet(URL,"customers/availablebooks/"+ SharedPreferencesAdapter.Instance().getLogin(), SharedPreferencesAdapter.Instance().getLogin(), SharedPreferencesAdapter.Instance().getLoginPassword(), Book[].class)));
    }

    public static Book getBook(String bookId) throws RESTClientException {
        return RESTClient.doGet(URL, "books/" + bookId, Book.class);
    }
}
