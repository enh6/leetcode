class Solution {
public:
    string intToRoman(int num) {
        string r;
        while (num >= 1000) {
            r += "M";
            num -= 1000;
        }
        if (num >= 900) {
            r += "CM";
            num -= 900;
        }
        if (num >= 500) {
            r += "D";
            num -= 500;
        }
        if (num >= 400) {
            r += "CD";
            num -= 400;
        }
        while (num >= 100) {
            r += "C";
            num -= 100;
        }
        if (num >= 90) {
            r += "XC";
            num -= 90;
        }
        if (num >= 50) {
            r += "L";
            num -= 50;
        }
        if (num >= 40) {
            r += "XL";
            num -= 40;
        }
        while (num >= 10) {
            r += "X";
            num -= 10;
        }
        if (num == 9) {
            r += "IX";
            num = 0;
        }
        if (num >= 5) {
            r += "V";
            num -= 5;
        }
        if (num == 4) {
            r += "IV";
            num = 0;
        }
        while (num > 0) {
            r += "I";
            num--;
        }
        return r;
    }
};