package ksiegarnia;

import com.google.firebase.FirebaseOptions;
import com.google.firebase.FirebaseApp;
//import com.google.firebase.FirebaseDatabase;
//import com.google.*;
import com.google.firebase.database.*;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileInputStream;

import java.util.HashMap;
import java.util.Map;


public class KsiegarniaServer  {

  private final static String JSON_FIREBASE_FILE = "file.json";
  private final static String DATABASE_URL = "https://aaaa-536df.firebaseio.com";
  private static DatabaseReference database;

  private static FirebaseOptions getFirebaseOptions() throws IOException {
    File file = new File(KsiegarniaServer.JSON_FIREBASE_FILE);
    FileInputStream fis = null;
      fis = new FileInputStream(file);
      FirebaseOptions options = new FirebaseOptions.Builder()
		  .setServiceAccount(fis)
		  .setDatabaseUrl(KsiegarniaServer.DATABASE_URL)
		  .build();
  		FirebaseApp.initializeApp(options);
			fis.close();
      return options;
  }


  public static void createEventListener(DatabaseReference ref){
    ref.addChildEventListener(new ChildEventListener() {
        @Override
        public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
            User u = dataSnapshot.getValue(User.class);
            System.out.println("username: " + u.username);
            System.out.println("email: " + u.email);
        }

        @Override
        public void onChildChanged(DataSnapshot dataSnapshot, String prevChildKey) {}

        @Override
        public void onChildRemoved(DataSnapshot dataSnapshot) {}

        @Override
        public void onChildMoved(DataSnapshot dataSnapshot, String prevChildKey) {}

        @Override
        public void onCancelled(DatabaseError databaseError) {}
    });

  }

  public static void main(String[] args) {
    try {
      FirebaseOptions foptions = getFirebaseOptions();
      System.out.println("Firebase app was initialized");
    } catch (Exception e){
      e.printStackTrace();
			System.out.println("Can not initialize Firebase app- Firebase JSON FILE MISSING");
      System.exit(1);
    }



      DatabaseReference ref = FirebaseDatabase.getInstance().getReference("server/users");

      createEventListener(ref);


	  //DatabaseReference ref = FirebaseDatabase.getInstance().getReference("server");
    //DatabaseReference usersRef = ref.child("users");



    Map<String, User> users = new HashMap<String, User>();
    users.put("aaa", new User("dasdas", "aafsd@wp.pl"));
    users.put("bbb", new User("dsfsdf", "gsdgsd@gmail.com"));
    users.put("ccc", new User("Fsdsdf", "gfdgdf@gdf"));
    users.put("ddd", new User("afff","fdfd@wp.pl"));

    ref.setValue(users);
    System.out.println(ref);

  }
}
