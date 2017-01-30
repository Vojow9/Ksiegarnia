package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.utils.SharedPreferencesAdapter;

public class MainActivity extends Activity {

    private Button btnGetAuthors;
    private Button btnGetBooks;
    private Button btnBought;
    private Button btnBasket;
    private Button btnLogin;
    private Button btnLogout;
    private TextView tvLoggedAs;
    private final int LOGIN_ACTIVITY_CODE = 100;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        SharedPreferencesAdapter.setContext(getApplicationContext());
        setControls();
        setEvents();
    }

    @Override
    protected void onStart() {
        super.onStart();
        String username = SharedPreferencesAdapter.Instance().getLogin();
        if(!username.equals("")) {
            tvLoggedAs.setText(getString(R.string.tv_loggedAs) + " " + username);
            btnLogout.setEnabled(true);
            btnLogin.setEnabled(false);
        } else {
            btnLogout.setEnabled(false);
            btnLogin.setEnabled(true);
        }
    }

    private void setControls() {
        btnGetAuthors = (Button) findViewById(R.id.btnAuthors);
        btnGetBooks = (Button) findViewById(R.id.btnBook);
        btnBought = (Button) findViewById(R.id.btnBought);
        btnBasket = (Button) findViewById(R.id.btnBasket);
        btnLogin = (Button) findViewById(R.id.btnLogin);
        btnLogout = (Button) findViewById(R.id.btnLogout);
        tvLoggedAs = (TextView) findViewById(R.id.tvLoggedAs);
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
                String username = SharedPreferencesAdapter.Instance().getLogin();
                if(!username.equals("")) {
                    Intent i = new Intent(MainActivity.this, BoughtListActivity.class);
                    startActivity(i);
                } else Toast.makeText(getApplicationContext(),"Należy się zalogować by zobaczyć listę zakupionych książek", Toast.LENGTH_LONG).show();
            }
        });

        btnBasket.setTransformationMethod(null);
        btnBasket.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(MainActivity.this, BasketActivity.class);
                startActivity(i);
            }
        });

        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), LoginActivity.class);
                startActivityForResult(intent, LOGIN_ACTIVITY_CODE);
            }
        });

        btnLogout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SharedPreferencesAdapter.Instance().setLogin("");
                SharedPreferencesAdapter.Instance().setLoginPassword("");
                tvLoggedAs.setText(getString(R.string.tv_notLoggedIn));
                btnLogout.setEnabled(false);
                btnLogin.setEnabled(true);
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if(requestCode == LOGIN_ACTIVITY_CODE && resultCode == RESULT_OK){
            String username = SharedPreferencesAdapter.Instance().getLogin();
            tvLoggedAs.setText(getString(R.string.tv_loggedAs) + " " +username);
        }
    }
}
