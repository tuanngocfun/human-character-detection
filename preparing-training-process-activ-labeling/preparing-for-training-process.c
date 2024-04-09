#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

#define SOURCE_DIR "/media/ngoc/a normal usb/ngoc/train-active-labeling/"
#define IMAGE_DEST_DIR "/media/ngoc/a normal usb/ngoc/train-active-labeling/100th/images"
#define LABEL_DEST_DIR "/media/ngoc/a normal usb/ngoc/train-active-labeling/100th/labels"
#define MAX_PATH_LENGTH 2048 // Define a suitable length

// Function to create directories if they don't exist
void create_directory(const char *path) {
    struct stat st = {0};
    if (stat(path, &st) == -1) {
        mkdir(path, 0700);
    }
}

// Function to copy files
void copy_file(const char *src, const char *dest) {
    FILE *srcFile, *destFile;
    char ch;

    srcFile = fopen(src, "r");
    destFile = fopen(dest, "w");

    if (srcFile == NULL || destFile == NULL) {
        printf("File copy failed for src: %s, dest: %s\n", src, dest);
        if (srcFile) fclose(srcFile);
        if (destFile) fclose(destFile);
        return;
    }

    ch = fgetc(srcFile);
    while (ch != EOF) {
        fputc(ch, destFile);
        ch = fgetc(srcFile);
    }

    fclose(srcFile);
    fclose(destFile);
}

int main() {
    // Create destination directories if they don't exist
    create_directory(IMAGE_DEST_DIR);
    create_directory(LABEL_DEST_DIR);

    DIR *dir;
    struct dirent *entry;
    char filepath[MAX_PATH_LENGTH], label_dest_path[MAX_PATH_LENGTH], image_dest_path[MAX_PATH_LENGTH];
    char image_filename[MAX_PATH_LENGTH], text_filename[MAX_PATH_LENGTH];
    dir = opendir(SOURCE_DIR);

    if (dir == NULL) {
        printf("Directory cannot be opened\n");
        return 1;
    }

    // Iterate over files in the source directory
    while ((entry = readdir(dir)) != NULL) {
        struct stat file_stat;
        snprintf(filepath, sizeof(filepath), "%s%s", SOURCE_DIR, entry->d_name);
        if (stat(filepath, &file_stat) == 0 && S_ISREG(file_stat.st_mode)) {
            snprintf(filepath, sizeof(filepath), "%s%s", SOURCE_DIR, entry->d_name);
            // Process text files
            if (strstr(entry->d_name, ".txt") != NULL && strcmp(entry->d_name, "classes.txt") != 0) {
                FILE *file = fopen(filepath, "r");
                if (file == NULL) {
                    printf("Failed to open file: %s\n", filepath);
                    continue;
                }

                // Check if the file is empty
                fseek(file, 0, SEEK_END);
                long filesize = ftell(file);
                rewind(file);
                // printf("File size: %ld\n", filesize); // Print the file size

                if (filesize != 0) {
                    char *content = malloc(filesize + 1);
                    fread(content, 1, filesize, file);
                    content[filesize] = '\0';

                    // Only copy text files with content
                    if (strlen(content) > 0) {
                        snprintf(label_dest_path, sizeof(label_dest_path), "%s%s", LABEL_DEST_DIR, entry->d_name);
                        copy_file(filepath, label_dest_path);
                    }
                    free(content);
                }

                fclose(file);
            }
            // Process image files
            else if (strstr(entry->d_name, ".jpg") != NULL) {
                snprintf(text_filename, sizeof(text_filename), "%s.txt", entry->d_name);
                char text_filepath[1024];
                snprintf(text_filepath, sizeof(text_filepath), "%s%s", SOURCE_DIR, text_filename);
                FILE *text_file = fopen(text_filepath, "r");

                if (text_file != NULL) {
                    fseek(text_file, 0, SEEK_END);
                    long text_filesize = ftell(text_file);
                    if (text_filesize > 0) {
                        snprintf(image_dest_path, sizeof(image_dest_path), "%s%s", IMAGE_DEST_DIR, entry->d_name);
                        copy_file(filepath, image_dest_path);
                    }
                    fclose(text_file);
                }
            }
        }
    }
    // Move 'classes.txt' file if exists
    char classes_txt_path[1024];
    snprintf(classes_txt_path, sizeof(classes_txt_path), "%s%s", SOURCE_DIR, "classes.txt");
    FILE *classes_txt_file = fopen(classes_txt_path, "r");
    if (classes_txt_file != NULL) {
        fclose(classes_txt_file);
        char dest_classes_txt_path[1024];
        snprintf(dest_classes_txt_path, sizeof(dest_classes_txt_path), "%s%s", "/media/ngoc/a normal usb/ngoc/train-active-labeling/100th/", "classes.txt");
        rename(classes_txt_path, dest_classes_txt_path);
    }

    // Verify that each .txt label file has its own .jpg image file and vice versa
    DIR *label_dir, *image_dir;
    label_dir = opendir(LABEL_DEST_DIR);
    image_dir = opendir(IMAGE_DEST_DIR);
    struct dirent *label_entry, *image_entry;

    // Remove .txt files without corresponding .jpg files
    while ((label_entry = readdir(label_dir)) != NULL) {
        if (strstr(label_entry->d_name, ".txt") != NULL) {
            snprintf(text_filename, sizeof(text_filename), "%s.jpg", label_entry->d_name);
            snprintf(image_filename, sizeof(image_filename), "%s%s", IMAGE_DEST_DIR, text_filename);
            if (!fopen(image_filename, "r")) {
                snprintf(filepath, sizeof(filepath), "%s%s", LABEL_DEST_DIR, label_entry->d_name);
                remove(filepath);
            }
        }
    }

    // Remove .jpg files without corresponding .txt files
    while ((image_entry = readdir(image_dir)) != NULL) {
        if (strstr(image_entry->d_name, ".jpg") != NULL) {
            snprintf(text_filename, sizeof(text_filename), "%s.txt", image_entry->d_name);
            snprintf(label_dest_path, sizeof(label_dest_path), "%s%s", LABEL_DEST_DIR, text_filename);
            if (!fopen(label_dest_path, "r")) {
                snprintf(filepath, sizeof(filepath), "%s%s", IMAGE_DEST_DIR, image_entry->d_name);
                remove(filepath);
            }
        }
    }

    // Close directories
    closedir(dir);
    closedir(label_dir);
    closedir(image_dir);

    return 0;
}
