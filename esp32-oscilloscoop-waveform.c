#include <math.h>

const int DAC_PIN = 25;  // Gebruik DAC1 (GPIO 25) voor de uitgang

const int samplingFreq = 1000; // Samplefrequentie voor de sinusgolf (1 kHz)
const float pi = 3.14159265;
const int amplitude = 127; // Maximale amplitude voor 8-bit DAC
const int offset = 128;    // Offset zodat de golf tussen 0-255 ligt
const int blockPeriod = 500; // Periode van de blokgolf in milliseconden

void setup() {
  pinMode(DAC_PIN, OUTPUT);
}

void loop() {
  generateSineWave();
  delay(1000); // Pauze van 1 seconde
  generateSquareWave();
  delay(1000); // Pauze van 1 seconde
}

void generateSineWave() {
  for (int i = 0; i < samplingFreq; i++) {
    // Bereken de sinuswaarde en converteer naar een DAC-signaal (0-255)
    int sineValue = amplitude * sin(2 * pi * i / samplingFreq) + offset;
    dacWrite(DAC_PIN, sineValue);
    delayMicroseconds(1000);  // 1 ms wachttijd voor elke sample
  }
}

void generateSquareWave() {
  for (int i = 0; i < blockPeriod; i++) {
    // Schakel tussen hoge en lage waarde voor de blokgolf
    dacWrite(DAC_PIN, 255);  // Hoog
    delay(blockPeriod / 2);   // Helpt met de pulsduur
    dacWrite(DAC_PIN, 0);    // Laag
    delay(blockPeriod / 2);   // Helpt met de pulsduur
  }
}
