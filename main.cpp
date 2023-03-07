#include <iostream>

#include "sqlite3.h"
#include "SQLiteCPP/SQLiteCpp.h"

int main()
{
    std::string_view var = std::string();
    SQLite::Database m_db("bd_name");
    sqlite3 *db;
    sqlite3_open("file name", &db);
    std::cout << "Hello world!";
}