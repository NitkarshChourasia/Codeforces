// #include <iostream>
// #include <string>

// int watermelon;
// int way_too_long_words(const std::string &word);

// int main()
// {
//     int way_too_long_words();
// }

// // Study about compilers and C++ versions (do we put periods in programming language comments or not?)
// // same for js

// int way_too_long_words(const std::string &word)
// {

//     const int maxLength = 10;
//     int concatDigit = word.length() - 2;

//     if (word.length() > maxLength)
//     {
//         std::string result = word.substr(0, 1) + std::to_string(concatDigit) + word.back();

//         std::cout << result << std::endl;
//     }
//     else
//     {
//         // Print the original word if it's not too long.

//         std::cout << word << std::endl;
//     }
// }

// int watermelon()
// {
//     int w;
//     std::cin >> w;

//     // Check if possible to divide the watermelon

//     if (w % 2 == 0 && w > 2)
//     {
//         std::cout << "YES" << std::endl;
//     }
//     else
//     {
//         std::cout << "NO" << std::endl;
//     }
//     return 0;
// }


#include <iostream>
#include <string>

int main() {
    std::string user_input;
    std::cin >> user_input;

    std::string ones = "1111111";
    std::string zeros = "0000000";

    if (user_input.find(ones) != std::string::npos || user_input.find(zeros) != std::string::npos) {
        std::cout << "YES" << std::endl;
    } else {
        std::cout << "NO" << std::endl;
    }

    return 0;
}
