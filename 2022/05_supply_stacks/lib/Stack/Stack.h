#pragma once

struct Box
{
    char cargo;
    Box *below;
};

class Stack
{
public:
    Stack() : _top(nullptr) {};
    ~Stack();

    bool empty();
    void push(char cargo);
    char pop();
    char get();

private:
    Box *_top;
};