package com.projekt.ksiegarniadroid.exceptions;

/**
 * Created by Sebo on 2016-11-14.
 */

@SuppressWarnings("serial")
public class RESTClientException extends Exception {

    public RESTClientException() {
    }

    public RESTClientException(String detailMessage) {
        super(detailMessage);
    }

    public RESTClientException(Throwable throwable) {
        super(throwable);
    }

    public RESTClientException(String detailMessage, Throwable throwable) {
        super(detailMessage, throwable);
    }
}
