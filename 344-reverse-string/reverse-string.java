class Solution {
    public void reverseString(char[] s) {
        int j = s.length-1;
        int i = 0;
        while (i<j){
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i++;
            j--;

        }

    }
    
}