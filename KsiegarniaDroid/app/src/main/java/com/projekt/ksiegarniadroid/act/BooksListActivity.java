package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
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
        setEvents();
    }

    @Override
    protected void onStart() {
        super.onStart();
        getBooks();
        setListViewAdapter();
    }

    private void setControls() {
        lvBooks = (ListView) findViewById(R.id.lvBooks);
    }

    private void setEvents() {
        lvBooks.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                Intent intent = new Intent(getApplicationContext(), BookDetailsInfo.class);
                intent.putExtra("Book", books.get(i));
                startActivity(intent);
            }
        });
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
                String authorId = getIntent().getStringExtra("AuthorId");
                if (authorId != null && !authorId.equals("")) {
                    books = RESTClientAdapter.getAuthorBooks(authorId);
                } else
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
