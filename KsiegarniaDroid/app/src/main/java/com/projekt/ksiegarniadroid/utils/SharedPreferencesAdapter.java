package com.projekt.ksiegarniadroid.utils;

import android.content.Context;
import android.content.SharedPreferences;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.projekt.ksiegarniadroid.objects.Book;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Created by Sebo on 2017-01-29.
 */

public final class SharedPreferencesAdapter {

    private static final String C_CONFIG_NAME = "BookStoreAndroidConfig";
    private static final String C_LOGIN = "SETTINGS_login";
    private static final String C_LOGIN_PASSWORD = "SETTINGS_loginPassword";
    private static final String C_BASKET = "APPVAR_basket";

    private static SharedPreferencesAdapter _instance;

    private static SharedPreferences _sharedPreferences;

    public static SharedPreferencesAdapter Instance() {

        if (_instance == null) {
            _instance = new SharedPreferencesAdapter();
        }

        return _instance;
    }

    public static void setContext(Context context) {
        _sharedPreferences = context.getSharedPreferences(C_CONFIG_NAME, Context.MODE_PRIVATE);
    }

    public Object clone() throws CloneNotSupportedException {
        throw new CloneNotSupportedException();
    }

    public String getLogin() {
        return _sharedPreferences.getString(C_LOGIN, "");
    }

    public void setLogin(String login) {
        _sharedPreferences.edit().putString(C_LOGIN, login).apply();
    }

    public String getLoginPassword() {
        return _sharedPreferences.getString(C_LOGIN_PASSWORD, "");
    }

    public void setLoginPassword(String password) {
        _sharedPreferences.edit().putString(C_LOGIN_PASSWORD, password).apply();
    }

    public void setBasket(ArrayList<Book> basketList) {
        String basketStr = new Gson().toJson(basketList);
        _sharedPreferences.edit().putString(C_BASKET, basketStr).apply();
    }

    public ArrayList<Book> getBasket() {
        String str = _sharedPreferences.getString(C_BASKET, null);

        Type type = new TypeToken<ArrayList<Book>>() {
        }.getType();
        ArrayList<Book> restoreData = new Gson().fromJson(str, type);
        if (restoreData != null)
            return restoreData;
        else return new ArrayList<>();
    }
}