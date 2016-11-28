package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.app.ProgressDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ListView;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.adapters.AuthorsAdapterView;
import com.projekt.ksiegarniadroid.adapters.BooksAdapterView;
import com.projekt.ksiegarniadroid.connectivity.RESTClient;
import com.projekt.ksiegarniadroid.connectivity.RESTClientAdapter;
import com.projekt.ksiegarniadroid.exceptions.RESTClientException;
import com.projekt.ksiegarniadroid.objects.Author;
import com.projekt.ksiegarniadroid.objects.Book;

import java.util.ArrayList;
import java.util.Arrays;

public class BooksListActivity extends Activity implements Runnable {

    private ArrayList<Book> books = new ArrayList<>();
    private BooksAdapterView adapter;
    private ListView lvBooks;
    private ProgressDialog progressDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_books_list);
        setControls();
        getBooks();
        setListViewAdapter();
        setEvents();
    }

    private void setControls() {
        lvBooks = (ListView) findViewById(R.id.lvBooks);
    }

    private void setEvents() {

    }

    private void setListViewAdapter() {
        adapter = new BooksAdapterView(books, this);
        lvBooks.setAdapter(adapter);

    }

    private void getBooks() {
        Thread _thread = new Thread(this);
        _thread.start();
    }

    @Override
    public void run() {
        try {
            books = RESTClientAdapter.getAllBooks();
        } catch (RESTClientException e) {
            e.printStackTrace();
        } finally {
            adapter.notifyDataSetChanged();
            setListViewAdapter();
        }
    }
}
