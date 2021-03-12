import java.util.Base64;

public class resolve {

	public static void main(String[] args) {
		String flag = "MOCSCTF{RE_enc0ded_5tr1ng}";
		byte[] bytes = flag.getBytes();
		String encoded = Base64.getEncoder().encodeToString(bytes);
		System.out.println(encoded);
	    String encodedStr = Encode(encoded, encoded.length());
		System.out.println(encodedStr);
		Decode(encodedStr);
	}

    public static String Encode(String str, int k) {
        String string = "";
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c >= 'a' && c <= 'z') {
                c = (char) ((k % 26) + c);
                if (c < 'a') {
                    c = (char) (c + 26);
                }
                if (c > 'z') {
                    c = (char) (c - 26);
                }
            } else if (c >= 'A' && c <= 'Z') {
            	c = (char) ((k % 26) + c);
                if (c < 'A') {
                    c = (char) (c + 26);
                }
                if (c > 'Z') {
                    c = (char) (c - 26);
                }
            }
            string = string + c;
        }
        byte[] bytes = string.getBytes();
		String encoded = Base64.getEncoder().encodeToString(bytes);
        return string;
    }

    public static void Decode(String str) {
        
        for (int offset = 0; offset < 27; offset++){
        	String string = "";
	        for (int i = 0; i < str.length(); i++) {
	            char c = str.charAt(i);
	            if (c >= 'a' && c <= 'z') {
	                c = (char) (c - (offset % 26));
	                if (c > 'a') {
	                    c = (char) (c - 26);
	                }
	                if (c < 'z') {
	                    c = (char) (c + 26);
	                }
	            } else if (c >= 'A' && c <= 'Z') {
	            	c = (char) (c - (offset % 26));
	                if (c > 'A') {
	                    c = (char) (c - 26);
	                }
	                if (c < 'Z') {
	                    c = (char) (c + 26);
	                }
	            }
	            string = string + c;
	        }
	        try{
	        	byte[] decodedbytes = Base64.getDecoder().decode(string);
		        String res = new String(decodedbytes);
		        System.out.println(res);
	        }catch(Exception e) {
			  	System.out.println("error");
			}
	        
        }
    }
}