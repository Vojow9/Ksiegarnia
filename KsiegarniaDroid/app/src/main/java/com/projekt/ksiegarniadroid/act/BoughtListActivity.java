package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.adapters.BooksAdapterView;
import com.projekt.ksiegarniadroid.adapters.BoughtBooksAdapterView;
import com.projekt.ksiegarniadroid.connectivity.RESTClientAdapter;
import com.projekt.ksiegarniadroid.exceptions.RESTClientException;
import com.projekt.ksiegarniadroid.objects.Book;

import java.util.ArrayList;

public class BoughtListActivity extends Activity {

    private ArrayList<Book> books = new ArrayList<>();
    private BoughtBooksAdapterView adapter;
    private ListView lvBooks;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bought);
        setControls();
        setEvents();
        getBoughtBooks();
        setListViewAdapter();
    }


    private void setControls() {
        lvBooks = (ListView) findViewById(R.id.lvBooks);
    }

    private void setEvents() {

    }

    private void setListViewAdapter() {
        adapter = new BoughtBooksAdapterView(books, this);
        lvBooks.setAdapter(adapter);

    }

    private void getBoughtBooks() {
        new BoughtBooksAsync().execute();
    }


    class BoughtBooksAsync extends AsyncTask<Void, Void, Void> {

        @Override
        protected Void doInBackground(Void... voids) {
            try {
                ArrayList<Book> boughtBooks = RESTClientAdapter.getBoughtBooks();
                for (int i=0; i<boughtBooks.size(); i++) {
                    books.add(RESTClientAdapter.getBook(boughtBooks.get(i).getBookid()));
                    books.get(i).setPurchasedate(boughtBooks.get(i).getPurchasedate());
                }
                for (int i = 0; i < books.size(); i++) {
                    books.get(i).setBookCover(RESTClientAdapter.getBookCover(books.get(i).getId()));
                }
            } catch (RESTClientException e) {
                e.printStackTrace();
            }
            return null;
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            setListViewAdapter();
        }
    }
}
