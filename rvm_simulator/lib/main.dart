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
  double supValue = 0;

  void connectToRaspberryPi() {
    if (availablePorts.isEmpty) {
      setState(() {
        processStatus = "No serial ports found";
      });
      return;
    }

    // port = SerialPort(availablePorts[0]); // Use the first available port
    port = SerialPort("COM13"); // Use the first available port
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

      // Start listening for responses
      listenToSerial();
    } else {
      setState(() {
        processStatus = "Failed to connect to Raspberry Pi";
      });
    }
  }

  void sendCommand(String command) {
    if (port != null && port!.isOpen) {
      String message = command + "\n"; // Ensures Raspberry Pi reads a full line
      port!.write(Uint8List.fromList(message.codeUnits));
      port!.flush(); // Force send
      print("Sent: $command");
    } else {
      print("Serial port not open!");
    }
  }

  void listenToSerial() {
    SerialPortReader reader = SerialPortReader(port!);
    reader.stream.listen((data) {
      String received = String.fromCharCodes(data);
      print("Received from Raspberry Pi: $received");
    });
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
        appBar: AppBar(title: Text("Flutter Serial Communication")),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("Current Status", style: TextStyle(fontSize: 20)),
              SizedBox(height: 10),
              Container(
                width: 700,
                height: 100,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(10),
                  color: Colors.grey[200],
                ),
                child: Center(
                  child: Text(
                    "Process",
                    style: TextStyle(fontSize: 70, fontWeight: FontWeight.bold),
                  ),
                ),
              ),
              SizedBox(height: 20),
              Container(
                width: 300,
                height: 200,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(10),
                  color: Color.fromARGB(255, 122, 233, 255),
                ),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Text("Enter weight of SUP", style: TextStyle(fontSize: 18)),
                    SizedBox(height: 10),
                    Slider(
                      value: supValue,
                      onChanged: (value) => setState(() => supValue = value),
                      max: 500,
                      label: '${supValue.toInt()}',
                      divisions: 500,
                    ),
                    SizedBox(height: 10),
                    ElevatedButton(
                      onPressed: () => sendCommand("START_PROCESS"),
                      style: ButtonStyle(
                      shadowColor: Colors.black,
                      child: Text("Send"),
                    ),
                  ],
                ),
              ),
              // ElevatedButton(
              //   onPressed: connectToRaspberryPi,
              //   child: Text("Connect to Raspberry Pi"),
              // ),
              // SizedBox(height: 20),
              // ElevatedButton(
              //   onPressed: () => sendCommand("START_PROCESS"),
              //   child: Text("Start Process"),
              // ),
              // ElevatedButton(
              //   onPressed: () => sendCommand("STOP_PROCESS"),
              //   child: Text("Stop Process"),
              // ),
              // SizedBox(height: 20),
              // Text(processStatus),
            ],
          ),
        ),
      ),
    );
  }
}
