package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.adapters.AuthorsAdapterView;
import com.projekt.ksiegarniadroid.connectivity.RESTClient;
import com.projekt.ksiegarniadroid.connectivity.RESTClientAdapter;
import com.projekt.ksiegarniadroid.exceptions.RESTClientException;
import com.projekt.ksiegarniadroid.objects.Author;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class AuthorsListActivity extends Activity {

    private ArrayList<Author> authors = new ArrayList<>();
    private AuthorsAdapterView adapter;
    private ListView lvAuthors;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_authors_list);
        setControls();
        getAuthors();
        setListViewAdapter();
        setEvents();
    }

    private void setControls() {
        lvAuthors = (ListView) findViewById(R.id.lvAuthors);
    }

    private void setEvents() {
        lvAuthors.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                Intent intent = new Intent(getApplicationContext(), BooksListActivity.class);
                intent.putExtra("AuthorId", authors.get(i).getId());
                startActivity(intent);
            }
        });
    }

    private void setListViewAdapter() {
        adapter = new AuthorsAdapterView(authors, this);
        lvAuthors.setAdapter(adapter);
    }

    private void getAuthors() {
        new AuthorsAsync().execute();
    }


    class AuthorsAsync extends AsyncTask<Void, Void, Void> {

        @Override
        protected Void doInBackground(Void... voids) {
            try {
                authors = RESTClientAdapter.getAllAuthors();
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
