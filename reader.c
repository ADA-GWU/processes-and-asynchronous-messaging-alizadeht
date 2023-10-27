#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <libpq-fe.h>
#include <sys/time.h>

// Read database configurations from a JSON file
json_t* read_db_config(const char* filename) {
    json_error_t error;
    json_t* root = json_load_file(filename, 0, &error);
    if (!root) {
        fprintf(stderr, "Error reading JSON file: %s\n", error.text);
        return NULL;
    }
    return root;
}

// Structuring for database configurations
typedef struct {
    char* database;
    char* user;
    char* password;
    char* host;
    int port;
} DBConfig;

// Structuring for a message
typedef struct {
    char sender_name[100];
    char message_text[100];
    time_t sent_time;
    time_t received_time;
} Message;

