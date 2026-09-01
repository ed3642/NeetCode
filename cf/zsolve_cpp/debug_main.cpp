#include <cstdio>

#define main app_main
#include "main.cpp"
#undef main

int main() {
    freopen("input", "r", stdin);
    return app_main();
}