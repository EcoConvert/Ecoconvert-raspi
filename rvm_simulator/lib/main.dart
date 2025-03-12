import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:flutter_libserialport/flutter_libserialport.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  SerialPort? port;
  List<String> availablePorts = SerialPort.availablePorts;
  String processStatus = "Waiting for connection...";

  void connectToRaspberryPi() {
    print("Available ports: $availablePorts");
    if (availablePorts.isEmpty) {
      setState(() {
        processStatus = "No serial ports found";
      });
      return;
    }

    // Pick the correct port (Adjust if needed)
    // port = SerialPort(availablePorts[0]); // Adjust if needed
    port = SerialPort("COM5"); // Adjust if needed
    print("Connecting to ${port!.name}");

    if (port!.openReadWrite()) {
      SerialPortConfig config =
          SerialPortConfig()
            ..baudRate = 9600
            ..bits = 8
            ..stopBits = 1
            ..parity = SerialPortParity.none;

      port!.config = config;

      setState(() {
        processStatus = "Connected to Raspberry Pi";
      });
    } else {
      setState(() {
        processStatus = "Failed to connect to Raspberry Pi";
      });
    }
  }

  void sendCommand(String command) {
    if (port != null && port!.isOpen) {
      String message = command + "\n"; // Ensures a full line is sent
      port!.write(Uint8List.fromList(message.codeUnits));
      port!.flush(); // Ensure data is sent immediately
      print("Sent: $command");
    } else {
      print("Serial port not open!");
    }
  }

  @override
  void dispose() {
    port?.close();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text("Flutter Simulated Arduino")),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              ElevatedButton(
                onPressed: connectToRaspberryPi,
                child: Text("Connect to Raspberry Pi"),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () => sendCommand("START_PROCESS"),
                child: Text("Start Process"),
              ),
              ElevatedButton(
                onPressed: () => sendCommand("STOP_PROCESS"),
                child: Text("Stop Process"),
              ),
              SizedBox(height: 20),
              Text(processStatus),
            ],
          ),
        ),
      ),
    );
  }
}
