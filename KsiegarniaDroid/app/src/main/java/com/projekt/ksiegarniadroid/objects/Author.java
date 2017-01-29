package com.projekt.ksiegarniadroid.objects;

/**
 * Created by Sebo on 2016-11-27.
 */

public class Author
{
    private String id;

    private String description;

    private String name;

    public String getId ()
    {
        return id;
    }

    public void setId (String id)
    {
        this.id = id;
    }

    public String getDescription ()
    {
        return description;
    }

    public void setDescription (String description)
    {
        this.description = description;
    }

    public String getName ()
    {
        return name;
    }

    public void setName (String name)
    {
        this.name = name;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [id = "+id+", description = "+description+", name = "+name+"]";
    }
}
