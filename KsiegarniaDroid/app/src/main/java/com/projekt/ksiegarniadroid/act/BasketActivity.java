package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.adapters.BasketAdapterView;
import com.projekt.ksiegarniadroid.adapters.BooksAdapterView;
import com.projekt.ksiegarniadroid.connectivity.RESTClientAdapter;
import com.projekt.ksiegarniadroid.exceptions.RESTClientException;
import com.projekt.ksiegarniadroid.objects.Book;
import com.projekt.ksiegarniadroid.utils.SharedPreferencesAdapter;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class BasketActivity extends Activity {

    private ArrayList<Book> books = new ArrayList<>();
    private BasketAdapterView adapter;
    private ListView lvBooks;
    private Button btnSummary;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_basket);
        setControls();
        setEvents();
    }

    @Override
    protected void onStart() {
        super.onStart();
        setBooks();
        setListViewAdapter();
    }

    private void setControls() {
        lvBooks = (ListView) findViewById(R.id.lvBooksBasket);
        btnSummary = (Button) findViewById(R.id.btnSummary);
    }

    private void setEvents() {
        lvBooks.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
            @Override
            public boolean onItemLongClick(AdapterView<?> adapterView, View view, final int i, long l) {
                new AlertDialog.Builder(BasketActivity.this)
                        .setTitle("Usuń")
                        .setMessage("Czy jesteś pewien, że chcesz usunąć wybraną pozycje z koszyka?")
                        .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int which) {
                                books.remove(i);
                                adapter.notifyDataSetChanged();
                                SharedPreferencesAdapter.Instance().setBasket(books);
                            }
                        })
                        .setNegativeButton(android.R.string.no, new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int which) {
                                // do nothing
                            }
                        }).show();
                return true;
            }
        });

        btnSummary.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (books.size() > 0) {
                    Intent intent = new Intent(getApplicationContext(), SummaryActivity.class);
                    startActivity(intent);
                } else
                    Toast.makeText(getApplicationContext(), "Brak książek w koszyku", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void setListViewAdapter() {
        adapter = new BasketAdapterView(books, this);
        lvBooks.setAdapter(adapter);

    }

    private void setBooks() {
        books = SharedPreferencesAdapter.Instance().getBasket();
    }


}
