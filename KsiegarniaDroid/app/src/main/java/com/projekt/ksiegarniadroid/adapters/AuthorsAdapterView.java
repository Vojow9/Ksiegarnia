package com.projekt.ksiegarniadroid.adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import com.projekt.ksiegarniadroid.R;
import com.projekt.ksiegarniadroid.objects.Author;

import java.util.ArrayList;

public class AuthorsAdapterView extends BaseAdapter {
    private final ArrayList<Author> _entries;
    private final Context _context;

    public AuthorsAdapterView(ArrayList<Author> _entries, Context _context) {
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
        Author entry = _entries.get(position);
        if (convertView == null) {
            LayoutInflater inflater = (LayoutInflater) _context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.author_list_item, null);
        }

        TextView tv = (TextView) convertView.findViewById(R.id.tvAuthorName);
        tv.setText(entry.getName());
        tv = (TextView) convertView.findViewById(R.id.tvDescription);
        tv.setText(entry.getDescription());
        return convertView;
    }
}

