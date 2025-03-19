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
  String currentStatus = "Waiting for connection...";
  SerialPort? port;
  List<String> availablePorts = SerialPort.availablePorts;
  String processStatus = "Waiting for connection...";

  // Data values from arduino
  double supValue = 0;
  bool isEcobrickCompleted = false;

  void connectToRaspberryPi() {
    if (availablePorts.isEmpty) {
      setState(() {
        processStatus = "No serial ports found";
      });
      return;
    }

    // port = SerialPort(availablePorts[0]); // Use the first available port
    port = SerialPort("COM13"); // Fixed port for raspi
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

  void sendStringCommand(String command) {
    if (port != null && port!.isOpen) {
      String message = command + "\n"; // Ensures Raspberry Pi reads a full line
      port!.write(Uint8List.fromList(message.codeUnits));
      port!.flush(); // Force send
      print("Sent: $command");
    } else {
      print("Serial port not open!");
    }
  }

  void sendSUPWeight(int command) {
    if (port != null && port!.isOpen) {
      String data =
          command.toString() + "\n"; // Ensures Raspberry Pi reads a full line
      port!.write(Uint8List.fromList(data.codeUnits));
      port!.flush(); // Force send
      print("Sent: $command");
      currentStatus = "Send $command";
    } else {
      print("Serial port not open!");
      currentStatus = "Serial port not open!";
    }
  }

  void sendEcobrickCompleted(bool command) {
    if (port != null && port!.isOpen) {
      Uint8List data = Uint8List(1); // Ensures Raspberry Pi reads a full line
      data[0] = command ? 1 : 0;
      port!.write(data);
      port!.flush(); // Force send
      print("Sent: ECOBRICK_COMPLETED");
      currentStatus = "Sent Ecobrick Completed";
    } else {
      print("Serial port not open!");
      currentStatus = "Serial port not open!";
    }
  }

  String listenToSerial() {
    String received = "";
    SerialPortReader reader = SerialPortReader(port!);
    reader.stream.listen((data) {
      String received = String.fromCharCodes(data);
      print("Received from Raspberry Pi: $received");
    });
    return received;
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
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                "Click to connect to Raspberry Pi",
                style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 5),
              ElevatedButton(
                onPressed:
                    () => setState(() {
                      connectToRaspberryPi();
                    }),
                style: ButtonStyle(
                  side: WidgetStateProperty.all(
                    BorderSide(color: Colors.black, width: 1),
                  ),
                ),
                child: Text(
                  processStatus,
                  style: TextStyle(
                    fontSize: 15,
                    color:
                        processStatus == "Connected to Raspberry Pi"
                            ? Colors.green
                            : Colors.red,
                  ),
                ),
              ),
              SizedBox(height: 40),
              Text("Current Status", style: TextStyle(fontSize: 20)),
              SizedBox(height: 10),
              // Status display------------------------------------------------
              Container(
                width: 700,
                padding: EdgeInsets.all(20),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(30),
                  color: Colors.grey[200],
                ),
                child: Center(
                  child: Text(
                    currentStatus,
                    style: TextStyle(fontSize: 50, fontWeight: FontWeight.bold),
                  ),
                ),
              ),
              SizedBox(height: 20),
              // Weight of SUP input------------------------------------------------
              Container(
                width: 300,
                padding: EdgeInsets.all(20),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  color: Color.fromARGB(255, 122, 233, 255),
                ),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Text(
                      "Enter weight of SUP",
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    SizedBox(height: 10),

                    Column(
                      children: [
                        Text("SUP Weight:", style: TextStyle(fontSize: 12)),
                        Text(
                          "${supValue.toInt()}g",
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                    Slider(
                      value: supValue,
                      max: 500,
                      onChanged: (value) => setState(() => supValue = value),
                      activeColor: Colors.black,
                      inactiveColor: const Color.fromARGB(255, 0, 191, 255),
                    ),
                    SizedBox(height: 10),
                    // Text('--status--'), // Tried to display data transfer status

                    // SUP Weight submit button------------------------------------------------
                    ElevatedButton(
                      onPressed:
                          () => setState(() {
                            sendSUPWeight(supValue.toInt());
                          }),
                      style: ButtonStyle(
                        fixedSize: WidgetStateProperty.all(Size(80, 20)),
                        padding: WidgetStateProperty.all(EdgeInsets.all(0)),
                        shadowColor: WidgetStateProperty.all(Colors.black),
                        elevation: WidgetStateProperty.all(3),
                        side: WidgetStateProperty.all(
                          BorderSide(color: Colors.black, width: 1.5),
                        ),
                      ),
                      child: Text(
                        "Submit",
                        style: TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.bold,
                          color: Colors.black,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed:
                    () => setState(() {
                      sendEcobrickCompleted(true);
                    }),
                style: ButtonStyle(
                  backgroundColor: WidgetStateProperty.all(
                    Color.fromARGB(255, 2, 255, 40),
                  ),
                  padding: WidgetStateProperty.all(EdgeInsets.all(10)),
                  fixedSize: WidgetStateProperty.all(Size(250, 40)),
                  shadowColor: WidgetStateProperty.all(Colors.black),
                  elevation: WidgetStateProperty.all(3),
                  side: WidgetStateProperty.all(
                    BorderSide(color: Colors.black, width: 1.5),
                  ),
                ),
                child: Text(
                  "Ecobrick Completed?",
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.bold,
                    color: Colors.black,
                  ),
                ),
              ),
              SizedBox(height: 20),
              Text("Received status value from RasPi:"),
              Text("--Some Value--"),
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
