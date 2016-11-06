package ksiegarnia;

import com.google.firebase.FirebaseOptions;
import com.google.firebase.FirebaseApp;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileInputStream;


public class KsiegarniaServer  {
  public static void main(String[] args) {

    File file = new File("mojprojekt3-2a7954b9a35c.json");
    FileInputStream fis = null;
    try {
      fis = new FileInputStream(file);
      FirebaseOptions options = new FirebaseOptions.Builder()
		  .setServiceAccount(fis)
		  .setDatabaseUrl("https://mojprojekt3.firebaseio.com/")
		  .build();
		FirebaseApp.initializeApp(options);
		System.out.println("Firebase app was initialized");
		} catch (IOException e) {
			e.printStackTrace();
			System.out.println("Can not initialize Firebase app");
		} finally {
			try {
				if (fis != null)
					fis.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
  }
}
