package com.projekt.ksiegarniadroid.adapters;

import android.content.Context;
import android.graphics.BitmapFactory;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.objects.Book;

import java.util.ArrayList;

/**
 * Created by Sebo on 2017-01-29.
 */

public class BasketAdapterView extends BaseAdapter {

    private final ArrayList<Book> _entries;
    private final Context _context;

    public BasketAdapterView(ArrayList<Book> _entries, Context _context) {
        this._entries = _entries;
        this._context = _context;
    }


    @Override
    public int getCount() {
        return _entries.size();
    }

    @Override
    public Object getItem(int position) {
        return _entries.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        Book entry = _entries.get(position);
        if (convertView == null) {
            LayoutInflater inflater = (LayoutInflater) _context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.basket_list_item, null);
        }

        TextView tv = (TextView) convertView.findViewById(R.id.tvBookTitle);
        tv.setText(entry.getTitle());
        tv = (TextView) convertView.findViewById(R.id.tvPrice);
        tv.setText(entry.getPrice() + _context.getString(R.string.tv_currency));
        tv = (TextView) convertView.findViewById(R.id.tvVersion);
        if (entry.getEbook())
            tv.setText(R.string.tv_ebook);
        else tv.setText(R.string.tv_book);
        ImageView iv = (ImageView) convertView.findViewById(R.id.ivBookPicture);
        if (entry.getBookCover() != null)
            iv.setImageBitmap(BitmapFactory.decodeByteArray(entry.getBookCover(), 0, entry.getBookCover().length));
        return convertView;
    }
}
