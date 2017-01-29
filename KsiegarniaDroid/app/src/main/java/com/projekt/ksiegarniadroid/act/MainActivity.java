package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.projekt.ksiegarniadroid.R;

public class MainActivity extends Activity {

    private Button btnGetAuthors;
    private Button btnGetBooks;
    private Button btnBought;
    private Button btnBasket;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setControls();
        setEvents();
    }

    private void setControls() {
        btnGetAuthors = (Button) findViewById(R.id.btnAuthors);
        btnGetBooks = (Button) findViewById(R.id.btnBook);
        btnBought = (Button) findViewById(R.id.btnBought);
        btnBasket = (Button) findViewById(R.id.btnBasket);
    }

    private void setEvents() {
        btnGetAuthors.setTransformationMethod(null);
        btnGetAuthors.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(MainActivity.this, AuthorsListActivity.class);
                startActivity(i);
            }
        });

        btnGetBooks.setTransformationMethod(null);
        btnGetBooks.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(MainActivity.this, BooksListActivity.class);
                startActivity(i);
            }
        });

        btnBought.setTransformationMethod(null);
        btnBought.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(MainActivity.this, BooksListActivity.class);
                startActivity(i);
            }
        });

        btnGetBooks.setTransformationMethod(null);
        btnGetBooks.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(MainActivity.this, BooksListActivity.class);
                startActivity(i);
            }
        });
    }
}
