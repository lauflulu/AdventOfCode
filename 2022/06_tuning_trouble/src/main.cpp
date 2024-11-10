#include <Arduino.h>
#include <WiFi.h>

#include <StartMarker.h>

const char *SSID = "WLAN";
const char *PASSWORD = "password123";
const int PORT = 12345;

WiFiServer server{PORT};

void setup()
{
  Serial.begin(115200);
  WiFi.begin(SSID, PASSWORD);

  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP()); // Print the IP address assigned to ESP32

  server.begin();
}

void loop()
{
  WiFiClient client = server.available();
  if (client)
  {
    Serial.println("Client connected");
    while (client.connected())
    {
      if (client.available())
      {
        String data = client.readStringUntil('\n');
        uint32_t result_1 = find_packet_marker(data);
        uint32_t result_2 = find_message_marker(data);
        client.println(String("Result1: ") + result_1 + String(" Result2: ") + result_2);
      }
    }
    client.stop();
    Serial.println("Client disconnected");
  }
}