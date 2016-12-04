package com.projekt.ksiegarniadroid.adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.objects.Book;

import java.util.ArrayList;

/**
 * Created by Sebo on 2016-11-27.
 */

public class BooksAdapterView extends BaseAdapter {

    private final ArrayList<Book> _entries;
    private final Context _context;

    public BooksAdapterView(ArrayList<Book> _entries, Context _context) {
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
            convertView = inflater.inflate(R.layout.book_list_item, null);
        }

        TextView tv = (TextView) convertView.findViewById(R.id.tvBookTitle);
        tv.setText(entry.getTitle());
        tv = (TextView) convertView.findViewById(R.id.tvDescription);
        tv.setText(entry.getDescription());
        tv = (TextView) convertView.findViewById(R.id.tvPrice);
        tv.setText(Double.toString(entry.getPrice()));
        tv = (TextView) convertView.findViewById(R.id.tvAvailability);
        if(entry.getAvailability()!=null)
        tv.setText(entry.getAvailability());
        else tv.setText("Brak");
        tv = (TextView) convertView.findViewById(R.id.tvIsEbook);
        tv.setText(entry.getIsEbook().toString());
        return convertView;
    }
}