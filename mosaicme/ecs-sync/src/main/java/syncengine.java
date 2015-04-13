/**
 * Created by salemm4 on 4/8/2015.
 */
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class syncengine {
    public static void main(String[] args) throws Exception {

        System.out.println(" Welcome to Mosaic-ECS Sync Engine");
        System.out.println("");
        System.out.println("1- Start EMC World Downloader Only.");
        System.out.println("2- Start MosaicMe Downloader Only.");
        System.out.println("3- Start MosaicMe Uploader Only.");
        System.out.println("4- Start All");
        System.out.println("5- Exit");

        while(true)
        {
            System.out.print("Enter Option Number: ");
            String key = new BufferedReader(new InputStreamReader(System.in)).readLine();
            if (key == "1" || key == "2" || key == "3" || key == "4" || key == "5") {
                int n = Integer.parseInt(key);

                switch (n) {
                    case 1: {

                        emcWorldDownloader downloader = new emcWorldDownloader();
                        downloader.run();
                        break;
                    }

                    case 2: {
                        mosaicMeDownloader getter = new mosaicMeDownloader();
                        getter.run();
                        break;
                    }

                    case 3: {
                        mosaicMeUploader uploader = new mosaicMeUploader();
                        uploader.run();
                        break;
                    }

                    case 4: {
                        (new Thread(new emcWorldDownloader())).start();
                        (new Thread(new mosaicMeDownloader())).start();
                        (new Thread(new mosaicMeUploader())).start();
                        break;
                    }

                    case 5: {
                        System.exit(0);
                    }

                    default: {

                        System.out.println("Please Choice number 1-4 Only.");

                        break;
                    }


                }
            } else {
                System.out.println("Please Choice number 1-4 Only.");

            }
        }


    }


}