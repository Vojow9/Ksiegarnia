package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.app.ProgressDialog;
import android.os.AsyncTask;
import android.os.Bundle;
import android.widget.ListView;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.adapters.BooksAdapterView;
import com.projekt.ksiegarniadroid.connectivity.RESTClientAdapter;
import com.projekt.ksiegarniadroid.exceptions.RESTClientException;
import com.projekt.ksiegarniadroid.objects.Book;

import java.util.ArrayList;

public class BooksListActivity extends Activity {

    private ArrayList<Book> books = new ArrayList<>();
    private BooksAdapterView adapter;
    private ListView lvBooks;

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
        new BooksAsync().execute();
    }


    class BooksAsync extends AsyncTask<Void, Void, Void> {

        @Override
        protected Void doInBackground(Void... voids) {
            try {
                books = RESTClientAdapter.getAllBooks();
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
            adapter.notifyDataSetChanged();
            setListViewAdapter();
        }
    }
}
