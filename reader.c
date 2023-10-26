#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <time.h>

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

