#pragma once
#include <Arduino.h>

class ISerial
{
public:
    ISerial(){};

    virtual String read_line(void) { return String("0"); };
    virtual void write_line(String){};
};

class SerialMock : public ISerial
{
public:
    SerialMock(){};

    String read_line(void) override { return input_buffer.substring(0, input_buffer.indexOf(0x0A)); };
    void write_line(String) override{};

    void set_input(String input);

private:
    String input_buffer;
};

class SerialAdapter : public ISerial
{
public:
    SerialAdapter(HardwareSerial &serial_) : serial(serial_) { serial = serial_; };

    String read_line(void) override { return serial.readStringUntil(0x0A); }
    void write_line(String string) override { serial.println(string); }

private:
    Stream &serial;
};