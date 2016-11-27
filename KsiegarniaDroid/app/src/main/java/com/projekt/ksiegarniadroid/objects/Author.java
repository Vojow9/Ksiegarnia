package com.projekt.ksiegarniadroid.objects;

/**
 * Created by Sebo on 2016-11-27.
 */

public class Author{

        private _id _id;

        private String description;

        private String name;

        public _id get_id ()
        {
            return _id;
        }

        public void set_id (_id _id)
        {
            this._id = _id;
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
            return "[_id = "+_id+", description = "+description+", name = "+name+"]";
        }
}
