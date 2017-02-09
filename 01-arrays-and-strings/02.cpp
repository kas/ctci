// implement function void reverse(char* str) in c or c++ which reverses a null-terminated string

#include <iostream>

void reverse(char* str) {
    std::string rev_str = "";
    for (int i = (strlen(str) - 1); i >= 0; i--) {
        rev_str += str[i];
    }
    std::cout << rev_str << std::endl;
}

int main(int argc, const char * argv[]) {
    reverse("esrever");
    return 0;
}
