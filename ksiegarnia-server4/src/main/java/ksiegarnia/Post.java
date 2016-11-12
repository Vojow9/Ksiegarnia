package ksiegarnia;

import com.google.firebase.database.IgnoreExtraProperties;



@IgnoreExtraProperties
public  class Post {

    public String author;
    public String title;

    public Post() {
    // Default constructor required for calls to DataSnapshot.getValue(Post.class)
}

    public Post(String author, String title) {
        this.author = author;
        this.title = title;
    }
}
