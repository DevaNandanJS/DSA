class Solution {
    public String reverseWords(String s) {
        String[] p = s.trim().split("\\s+");
        String n = "";
        for (int i = p.length-1;i>=0;i--){
            n = n+ p[i];
            if (i!=0){
                n=n+" ";
            }
        }
        return n;

    }
}