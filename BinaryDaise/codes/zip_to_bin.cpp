#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>
#include <filesystem>

namespace fs = std::filesystem;

void fileToBinary(const std::string& filename, const std::string& outputFilename) {
    std::ifstream file(filename, std::ios::binary);
    std::ofstream outputFile(outputFilename, std::ios::binary);

    if (!file || !outputFile) {
        std::cerr << "Failed to open files." << std::endl;
        return;
    }

    char byte;
    while (file.get(byte)) {
        std::bitset<8> bits(byte);
        outputFile << bits;
    }

    file.close();
    outputFile.close();
}

int main() {
    std::string inputFolder = "C:\\Users\\PRITHWISH\\Desktop\\CODE\\BinaryDaise\\zippy";   // Replace with your input folder path
    std::string outputFolder = "C:\\Users\\PRITHWISH\\Desktop\\CODE\\BinaryDaise\\output"; // Replace with your output folder path

    for (const auto& entry : fs::directory_iterator(inputFolder)) {
        if (entry.is_regular_file() && entry.path().extension() == ".zip") {
            std::string inputFilePath = entry.path().string();
            std::string outputFilePath = outputFolder + "/" + entry.path().stem().string() + ".txt";
            fileToBinary(inputFilePath, outputFilePath);
            std::cout << "Converted " << inputFilePath << " to " << outputFilePath << std::endl;
        }
    }

    return 0;
}
