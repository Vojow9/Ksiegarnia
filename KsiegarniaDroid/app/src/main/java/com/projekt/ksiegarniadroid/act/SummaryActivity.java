package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.connectivity.RESTClient;
import com.projekt.ksiegarniadroid.connectivity.RESTClientAdapter;
import com.projekt.ksiegarniadroid.exceptions.RESTClientException;
import com.projekt.ksiegarniadroid.objects.Book;
import com.projekt.ksiegarniadroid.utils.SharedPreferencesAdapter;

import java.util.ArrayList;

public class SummaryActivity extends Activity {

    private Button btnBuy;
    private TextView tvUsername;
    private TextView tvBooksQuantity;
    private TextView tvPrice;
    private ArrayList<Book> books = new ArrayList<>();
    private ArrayList<String> bookIds;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_summary);
        books = SharedPreferencesAdapter.Instance().getBasket();
        setControls();
        setEvents();
    }

    private void setControls(){
        btnBuy = (Button) findViewById(R.id.btnBuy);
        tvUsername = (TextView) findViewById(R.id.tvUsername);
        tvUsername.setText(SharedPreferencesAdapter.Instance().getLogin());
        tvBooksQuantity = (TextView) findViewById(R.id.tvBooksQuantity);
        tvBooksQuantity.setText(String.valueOf(books.size()));
        tvPrice = (TextView) findViewById(R.id.tvPrice);
        double price =0;
        bookIds = new ArrayList<>();
        for(Book book : books){
            price += Double.valueOf(book.getPrice());
            bookIds.add(book.getId());
        }
        tvPrice.setText(String.valueOf(price)+ getString(R.string.tv_currency));
    }

    private void setEvents(){
        btnBuy.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                buy();
            }
        });
    }

    private void buy() {
        class BuyAsync extends AsyncTask<Void, Void, Void> {

            @Override
            protected Void doInBackground(Void... voids) {
                try {
                    RESTClientAdapter.buy(bookIds);
                } catch (RESTClientException e) {
                    e.printStackTrace();
                }
                return null;
            }

            @Override
            protected void onPostExecute(Void aVoid) {
                if (RESTClient.resCode == 201) {
                    SharedPreferencesAdapter.Instance().setBasket(new ArrayList<Book>());
                    Intent returnIntent = new Intent();
                    setResult(Activity.RESULT_OK, returnIntent);
                    Toast.makeText(SummaryActivity.this, "Kupno zakończyło się pomyślnie!", Toast.LENGTH_SHORT).show();
                    finish();
                } else if (RESTClient.resCode == 403)
                    Toast.makeText(SummaryActivity.this, "Nie mozna wypożyczyć więcej niż jednego ebooka!", Toast.LENGTH_SHORT).show();
                else
                    Toast.makeText(SummaryActivity.this, "Transakcja sie nie powiodła", Toast.LENGTH_SHORT).show();
            }
        }
        new BuyAsync().execute();
    }
}
