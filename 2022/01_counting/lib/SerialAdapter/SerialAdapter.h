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

    String read_line(void) override { return String("0"); };
    void write_line(String) override{};
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