#include <Stack.h>

Stack::~Stack()
{
    while (_top)
    {
        pop();
    }
};

void Stack::push(char cargo)
{
    Box *box = new Box;
    box->below = _top;
    box->cargo = cargo;
    _top = box;
}

char Stack::pop()
{
    if (empty())
    {
        return 0x00;
    }
    Box *remove = _top;
    _top = remove->below;
    char value = remove->cargo;
    delete remove;
    return value;
}

char Stack::get()
{
    if (empty())
    {
        return 0x00;
    }
    return _top->cargo;
}

bool Stack::empty()
{
    return !_top;
}
