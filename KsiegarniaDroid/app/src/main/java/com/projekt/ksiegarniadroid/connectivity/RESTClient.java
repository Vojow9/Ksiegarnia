package com.projekt.ksiegarniadroid.connectivity;

/**
 * Created by Sebo on 2016-11-14.
 */

import android.util.Log;

import com.google.gson.Gson;
import com.projekt.ksiegarniadroid.exceptions.RESTClientException;


import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;

import org.apache.commons.io.IOUtils;

public class RESTClient {
    public static <T> T doPost(String baseAddress, String methodName,
                               Object inputObject, Class<T> outputClass)
            throws RESTClientException {
        if (baseAddress == null || baseAddress == "")
            throw new IllegalArgumentException(
                    "Argument 'baseAddress' is null or empty.");
        if (methodName == null || methodName == "")
            throw new IllegalArgumentException(
                    "Argument 'methodName' is null or empty.");
        if (inputObject == null)
            throw new IllegalArgumentException(
                    "Argument 'inputObject' is null.");
        if (outputClass == null)
            throw new IllegalArgumentException(
                    "Argument 'outputClass' is null.");
        try {
            URL url = new URL(buildURL(baseAddress, methodName));
            HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
            httpURLConnection.setDoOutput(true);
            httpURLConnection.setDoInput(true);
            httpURLConnection.setRequestMethod("POST");
            httpURLConnection.setRequestProperty("Content-Type", "application/json");

            httpURLConnection.connect();
            DataOutputStream wr = new DataOutputStream(httpURLConnection.getOutputStream());
            wr.write(buildStringEntity(inputObject).getBytes());
            wr.flush();
            wr.close();
            InputStream is = httpURLConnection.getInputStream();
            BufferedReader br = new BufferedReader(new InputStreamReader(is));
            String line;
            StringBuilder responseOutput = new StringBuilder();
            while ((line = br.readLine()) != null) {
                responseOutput.append(line);
            }
            br.close();
            is.close();
            httpURLConnection.disconnect();
            return new Gson().fromJson(responseOutput.toString(), outputClass);
        } catch (Exception e) {
            throw new RESTClientException(e);
        }
    }

    public static  <T> T doGet(String baseAddress, String methodName, Class <T> outputClass)
            throws RESTClientException {
        if (baseAddress == null || baseAddress == "")
            throw new IllegalArgumentException(
                    "Argument 'baseAddress' is null or empty.");
        if (methodName == null || methodName == "")
            throw new IllegalArgumentException(
                    "Argument 'methodName' is null or empty.");
        if (outputClass == null)
            throw new IllegalArgumentException(
                    "Argument 'outputClass' is null.");
        try {
            URL url = new URL(buildURL(baseAddress, methodName));
            HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
            httpURLConnection.setRequestMethod("GET");
            httpURLConnection.setRequestProperty("Content-Type", "application/json");
            httpURLConnection.setConnectTimeout(20000);
            int responseCode = httpURLConnection.getResponseCode();
            Log.d("POST_GET","Sending 'GET' request to URL : " + url);
            Log.d("POST_GET","Response Code : " + responseCode);
            BufferedReader in = new BufferedReader(new InputStreamReader(httpURLConnection.getInputStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
            Log.d("HTTP_GET","Respose = " + response.toString());
            return new Gson().fromJson(response.toString(), outputClass);
        } catch (Exception e) {
            throw new RESTClientException(e);
        }
    }

    public static  byte[] doGetPicture(String baseAddress, String methodName)
            throws RESTClientException {
        if (baseAddress == null || baseAddress == "")
            throw new IllegalArgumentException(
                    "Argument 'baseAddress' is null or empty.");
        if (methodName == null || methodName == "")
            throw new IllegalArgumentException(
                    "Argument 'methodName' is null or empty.");
        try {
            URL url = new URL(buildURL(baseAddress, methodName));
            URLConnection conn = url.openConnection();
            conn.setConnectTimeout(5000);
            conn.setReadTimeout(5000);
            conn.connect();

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            IOUtils.copy(conn.getInputStream(), baos);

            return baos.toByteArray();


        } catch (Exception e) {
            throw new RESTClientException(e);
        }
    }

    private static String buildURL(String baseAddress, String methodName) {
        if (baseAddress.endsWith("/"))
            return baseAddress + methodName;
        else
            return baseAddress + "/" + methodName;
    }

    private static String buildStringEntity(Object inputObject)
            throws UnsupportedEncodingException {
        Gson gson = new Gson();
        return gson.toJson(inputObject, inputObject.getClass());
    }
}