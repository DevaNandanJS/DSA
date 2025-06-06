class Solution {
    public String sortSentence(String s) {
        String[] w = s.split(" ");
        String[] r = new String[w.length];

        for (String x:w){
            int p = x.charAt(x.length()-1) -'1';
            String q = x.substring(0,x.length()-1);
            r[p] =q;

        }
        String c = String.join(" ",r);
        return c;
    }
}