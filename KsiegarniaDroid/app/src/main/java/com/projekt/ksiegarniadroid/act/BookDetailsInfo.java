package com.projekt.ksiegarniadroid.act;

import android.app.Activity;
import android.content.Intent;
import android.graphics.BitmapFactory;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.objects.Book;
import com.projekt.ksiegarniadroid.utils.SharedPreferencesAdapter;

import java.util.ArrayList;

public class BookDetailsInfo extends Activity {
    private Button btnAddBookToBasket;
    private Button btnGoToBasket;
    private Book book;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_book_details_info);
        book = (Book) getIntent().getSerializableExtra("Book");
        setControls();
        setEvents();
    }

    private void setControls() {
        btnAddBookToBasket = (Button) findViewById(R.id.btnAddBookToBasket);
        ArrayList<String> basket = SharedPreferencesAdapter.Instance().getBasket();
        if(basket.contains(book.getId()) && book.getEbook()){
            btnAddBookToBasket.setEnabled(false);
        } else if(basket.contains(book.getId())){
            int countBookInBasket = 0;
            for (int i=0; i<basket.size(); i++){
                if(basket.get(i).equals(book.getId()))
                    countBookInBasket++;
            }
            if(countBookInBasket>=book.getAvailability())
                btnAddBookToBasket.setEnabled(false);
        }
        btnGoToBasket = (Button) findViewById(R.id.btnGoToBasket);
        if(basket.size()>0)
            btnGoToBasket.setVisibility(View.VISIBLE);
        TextView tv = (TextView) findViewById(R.id.tvBookTitle);
        tv.setText(book.getTitle());
        tv = (TextView) findViewById(R.id.tvDescription);
        tv.setText(book.getDescription());
        tv = (TextView) findViewById(R.id.tvPrice);
        tv.setText(book.getPrice() + getString(R.string.tv_currency));
        tv = (TextView) findViewById(R.id.tvAvailability);
        if (!book.getEbook())
            tv.setText(String.valueOf(book.getAvailability()));
        else {
            tv.setVisibility(View.GONE);
            findViewById(R.id.tvCAvailability).setVisibility(View.GONE);
        }
        tv = (TextView) findViewById(R.id.tvVersion);
        if (book.getEbook())
            tv.setText(R.string.tv_ebook);
        else tv.setText(R.string.tv_book);
        ImageView iv = (ImageView) findViewById(R.id.ivBookPicture);
        if (book.getBookCover() != null)
            iv.setImageBitmap(BitmapFactory.decodeByteArray(book.getBookCover(), 0, book.getBookCover().length));
    }

    private void setEvents() {
        btnAddBookToBasket.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ArrayList<String> basket = SharedPreferencesAdapter.Instance().getBasket();
                if (!book.getEbook() && book.getAvailability() > 0) {
                    basket.add(book.getId());
                    Toast.makeText(getApplicationContext(), "Dodano książkę do koszyka!",Toast.LENGTH_SHORT).show();
                    SharedPreferencesAdapter.Instance().setBasket(basket);
                    book.setAvailability(book.getAvailability()-1);
                } else if(book.getEbook()){
                    basket.add(book.getId());
                    Toast.makeText(getApplicationContext(), "Dodano ebook do koszyka!",Toast.LENGTH_SHORT).show();
                    SharedPreferencesAdapter.Instance().setBasket(basket);
                    btnAddBookToBasket.setEnabled(false);
                } else {
                    Toast.makeText(getApplicationContext(), "Nie można dodać więcej książek!",Toast.LENGTH_SHORT).show();
                    btnAddBookToBasket.setEnabled(false);
                }
                if(basket.size()>0)
                    btnGoToBasket.setVisibility(View.VISIBLE);
            }
        });
    }

}
