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
  String processStatus = "Waiting for data...";

  void connectToPython() {
    print(availablePorts);
    if (availablePorts.isEmpty) {
      setState(() {
        processStatus = "No serial ports found";
      });
      return;
    }

    String targetPort = "COM6"; // Make sure this matches Python

    try {
      port = SerialPort(targetPort);
      print("Connecting to $targetPort");

      if (port!.openReadWrite()) {
        SerialPortConfig config =
            SerialPortConfig()
              ..baudRate = 9600
              ..bits = 8
              ..stopBits = 1
              ..parity = SerialPortParity.none;

        port!.config = config;
        setState(() {
          processStatus = "Connected to Python on $targetPort";
        });
      } else {
        throw Exception("Failed to open the port");
      }
    } catch (e) {
      setState(() {
        processStatus = "Error: $e";
      });
      print("Connection error: $e");
    }
  }

  void sendCommand(String command) {
    if (port != null && port!.isOpen) {
      String message = command + "\n"; // Ensures Python receives a full line
      port!.write(Uint8List.fromList(message.codeUnits));
      port!.flush(); // Forces the message to send immediately
      print("Sent: $command");
    } else {
      print("Serial port not open!");
    }
  }

  // void listenToSerial() {
  //   SerialPortReader reader = SerialPortReader(port!);
  //   reader.stream.listen((data) {
  //     String received = String.fromCharCodes(data);
  //     print("Received from Python: $received");
  //   });
  // }

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
                onPressed: connectToPython,
                child: Text("Connect to Python"),
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
