#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <algorithm>

namespace fs = std::filesystem;

int main() {
    std::string source_dir = "/media/ngoc/a normal usb/ngoc/train-active-labeling/";
    std::string image_dest_dir = "/media/ngoc/a normal usb/ngoc/train-active-labeling/100th/images";
    std::string label_dest_dir = "/media/ngoc/a normal usb/ngoc/train-active-labeling/100th/labels";

    // Create destination directories if they don't exist
    fs::create_directories(image_dest_dir);
    fs::create_directories(label_dest_dir);

    // Iterate over files in the source directory
    for (const auto &entry : fs::directory_iterator(source_dir)) {
        std::string filename = entry.path().filename().string();
        std::string filepath = source_dir + filename;

        // Process text files
        if (filename != "classes.txt" && filename.find(".txt") != std::string::npos) {
            std::ifstream file(filepath);
            std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
            content.erase(std::remove(content.begin(), content.end(), '\n'), content.end());
            
            // Only copy text files with content
            if (!content.empty()) {
                std::string label_dest_path = label_dest_dir + filename;
                fs::copy(filepath, label_dest_path);
            }
        }
        // Process image files
        else if (filename.find(".jpg") != std::string::npos) {
            std::string text_filename = filename;
            text_filename.replace(text_filename.find(".jpg"), 4, ".txt");
            std::string text_filepath = source_dir + text_filename;
            if (fs::exists(text_filepath)) {
                std::ifstream text_file(text_filepath);
                std::string text_content((std::istreambuf_iterator<char>(text_file)), std::istreambuf_iterator<char>());
                text_content.erase(std::remove(text_content.begin(), text_content.end(), '\n'), text_content.end());
                if (!text_content.empty()) {
                    std::string image_dest_path = image_dest_dir + filename;
                    fs::copy(filepath, image_dest_path);
                }
            }
        }
    }

    // Move 'classes.txt' file if exists
    std::string classes_txt_path = source_dir + "classes.txt";
    if (fs::exists(classes_txt_path)) {
        fs::rename(classes_txt_path, "/media/ngoc/a normal usb/ngoc/train-active-labeling/100th/classes.txt");
    }

    // Verify that each .txt label file has its own .jpg image file and vice versa
    for (const auto &entry : fs::directory_iterator(label_dest_dir)) {
        std::string filename = entry.path().filename().string();
        filename.replace(filename.find(".txt"), 4, ".jpg");
        if (!fs::exists(image_dest_dir + filename)) {
            fs::remove(label_dest_dir + entry.path().filename().string());
        }
    }
    for (const auto &entry : fs::directory_iterator(image_dest_dir)) {
        std::string filename = entry.path().filename().string();
        filename.replace(filename.find(".jpg"), 4, ".txt");
        if (!fs::exists(label_dest_dir + filename)) {
            fs::remove(image_dest_dir + entry.path().filename().string());
        }
    }

    return 0;
}