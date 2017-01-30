package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.connectivity.RESTClient;
import com.projekt.ksiegarniadroid.connectivity.RESTClientAdapter;
import com.projekt.ksiegarniadroid.exceptions.RESTClientException;
import com.projekt.ksiegarniadroid.objects.Customer;
import com.projekt.ksiegarniadroid.utils.SharedPreferencesAdapter;

public class LoginActivity extends Activity {

    private Button btnLogin;
    private Button btnRegister;
    private EditText etUsername;
    private EditText etPassword;
    private Customer user;
    private final int REGISTER_ACTIVITY_CODE = 100;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        setControls();
        setEvents();

    }

    private void setControls() {
        btnLogin = (Button) findViewById(R.id.btnLogin);
        btnRegister = (Button) findViewById(R.id.btnRegister);
        etUsername = (EditText) findViewById(R.id.etLogin);
        etPassword = (EditText) findViewById(R.id.etPassword);
    }

    private void setEvents() {
        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(etUsername.getText().toString().equals("") || etPassword.getText().toString().equals(""))
                    Toast.makeText(getApplicationContext(), "Trzeba wypełnić wszystkie pola!", Toast.LENGTH_SHORT).show();
                else {
                    login(etUsername.getText().toString(), etPassword.getText().toString());
                }
            }
        });

        btnRegister.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(LoginActivity.this, RegisterActivity.class);
                startActivityForResult(intent, REGISTER_ACTIVITY_CODE);
                finish();
            }
        });
    }

    private void login(final String username, final String password){
        class LoginAsync extends AsyncTask<Void, Void, Void> {

            @Override
            protected Void doInBackground(Void... voids) {
                try {
                    user = RESTClientAdapter.login(username, password);
                } catch (RESTClientException e) {
                    e.printStackTrace();
                }
                return null;
            }

            @Override
            protected void onPostExecute(Void aVoid) {
                if(RESTClient.resCode==200) {
                    SharedPreferencesAdapter.Instance().setLogin(username);
                    SharedPreferencesAdapter.Instance().setLoginPassword(password);
                    Intent returnIntent = new Intent();
                    setResult(Activity.RESULT_OK, returnIntent);
                    Toast.makeText(LoginActivity.this, "Zalogowano pomyślnie!", Toast.LENGTH_SHORT).show();
                    finish();
                } else Toast.makeText(LoginActivity.this, "Dane logowania są niepoprawne!", Toast.LENGTH_SHORT).show();
            }
        }

        new LoginAsync().execute();
    }
}
