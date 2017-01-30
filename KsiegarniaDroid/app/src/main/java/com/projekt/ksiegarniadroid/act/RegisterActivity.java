package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.connectivity.RESTClient;
import com.projekt.ksiegarniadroid.connectivity.RESTClientAdapter;
import com.projekt.ksiegarniadroid.exceptions.RESTClientException;
import com.projekt.ksiegarniadroid.objects.Customer;
import com.projekt.ksiegarniadroid.utils.SharedPreferencesAdapter;

public class RegisterActivity extends Activity {

    private EditText etLogin;
    private EditText etName;
    private EditText etLastName;
    private EditText etAddress;
    private EditText etEmail;
    private EditText etPassword;
    private EditText etRepeatPassword;
    private Button btnRegister;
    private RadioGroup radioSexGroup;
    private RadioButton radioSexButton;
    private Customer newUser;
    private RadioButton rbFemale;
    private RadioButton rbMale;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        setControls();
        setEvents();
    }

    private void setControls() {
        etLogin = (EditText) findViewById(R.id.etLogin);
        etName = (EditText) findViewById(R.id.etName);
        etLastName = (EditText) findViewById(R.id.etLastName);
        etAddress = (EditText) findViewById(R.id.etAddress);
        etEmail = (EditText) findViewById(R.id.etEmail);
        etPassword = (EditText) findViewById(R.id.etPassword);
        etRepeatPassword = (EditText) findViewById(R.id.etRepeatPassword);
        btnRegister = (Button) findViewById(R.id.btnRegister);
        radioSexGroup = (RadioGroup) findViewById(R.id.rgSex);
        rbFemale = ((RadioButton) findViewById(R.id.rbFemale));
        rbMale = ((RadioButton) findViewById(R.id.rbMale));
        newUser = new Customer();
    }

    public void onRadioButtonClicked() {
        // Is the button now checked?
        radioSexButton = (RadioButton) findViewById(radioSexGroup.getCheckedRadioButtonId());
        boolean checked = radioSexButton.isChecked();

        // Check which radio button was clicked
        switch (radioSexButton.getId()) {
            case R.id.rbMale:
                if (checked)
                    newUser.setGender("Male");
                break;
            case R.id.rbFemale:
                if (checked)
                    newUser.setGender("Female");
                break;
        }
    }

    private void setEvents() {
        rbFemale.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });
        rbMale.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });
        btnRegister.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                onRadioButtonClicked();
                if (etLogin.getText().toString().equals("") || etName.getText().toString().equals("") || etLastName.getText().toString().equals("")
                        || etAddress.getText().toString().equals("") || etEmail.getText().toString().equals("") || etPassword.getText().toString().equals("")
                        || etRepeatPassword.getText().toString().equals("")) {
                    Toast.makeText(getApplicationContext(), "Należy wypełnić wszystkie pola!", Toast.LENGTH_SHORT).show();
                } else if (!etPassword.getText().toString().equals(etRepeatPassword.getText().toString())) {
                    Toast.makeText(getApplicationContext(), "Hasła muszą się zgadzać!", Toast.LENGTH_SHORT).show();
                } else {
                    newUser.setUsername(etLogin.getText().toString());
                    newUser.setFirst_name(etName.getText().toString());
                    newUser.setLast_name(etLastName.getText().toString());
                    newUser.setAddress(etAddress.getText().toString());
                    newUser.setEmail(etEmail.getText().toString());
                    newUser.setPassword(etPassword.getText().toString());
                    register();
                }
            }
        });
    }

    private void register() {
        class RegisterAsync extends AsyncTask<Void, Void, Void> {

            @Override
            protected Void doInBackground(Void... voids) {
                try {
                    RESTClientAdapter.register(newUser);
                } catch (RESTClientException e) {
                    e.printStackTrace();
                }
                return null;
            }

            @Override
            protected void onPostExecute(Void aVoid) {
                if (RESTClient.resCode == 201) {
                    SharedPreferencesAdapter.Instance().setLogin(newUser.getUsername());
                    SharedPreferencesAdapter.Instance().setLoginPassword(newUser.getPassword());
                    Intent returnIntent = new Intent();
                    setResult(Activity.RESULT_OK, returnIntent);
                    Toast.makeText(RegisterActivity.this, "Zalogowano pomyślnie!", Toast.LENGTH_SHORT).show();
                    finish();
                } else if (RESTClient.resCode == 409)
                    Toast.makeText(RegisterActivity.this, "Podany login został już wykorzystany!", Toast.LENGTH_SHORT).show();
                else
                    Toast.makeText(RegisterActivity.this, "Dane rejestracji są niepoprawne!", Toast.LENGTH_SHORT).show();
            }
        }
        new RegisterAsync().execute();
    }
}
