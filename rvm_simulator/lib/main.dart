import 'dart:async';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:flutter_libserialport/flutter_libserialport.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

void main() {
  runApp(ProviderScope(child: MyApp())); // Wrap with ProviderScope for Riverpod
}

// --------------------------- RIVERPOD PROVIDERS ---------------------------
final currentStatusProvider = StateProvider<String>(
  (ref) => "Waiting for connection...",
);
final processStatusProvider = StateProvider<String>(
  (ref) => "Waiting for connection...",
);

final supWeightProvider = StateProvider<double>((ref) => 0);
final ecobrickProgressProvider = StateProvider<double>(
  (ref) => 0,
); // For ecobrick status
final isEcobrickCompletedProvider = StateProvider<bool>((ref) => false);

class MyApp extends ConsumerStatefulWidget {
  const MyApp({super.key});

  @override
  ConsumerState<MyApp> createState() => _MyAppState();
}

class _MyAppState extends ConsumerState<MyApp> {
  SerialPort? port;
  List<String> availablePorts = SerialPort.availablePorts;
  StreamSubscription<Uint8List>? subscription;

  Future<void> connectToRaspberryPi() async {
    final processStatusNotifier = ref.read(processStatusProvider.notifier);
    final currentStatusNotifier = ref.read(currentStatusProvider.notifier);

    if (availablePorts.isEmpty) {
      processStatusNotifier.state = "No serial ports found";
      return;
    }

    port = SerialPort("COM13"); // Fixed port
    print("Connecting to ${port!.name}");

    if (port!.openReadWrite()) {
      SerialPortConfig config =
          SerialPortConfig()
            ..baudRate = 9600
            ..bits = 8
            ..stopBits = 1
            ..parity = SerialPortParity.none;

      port!.config = config;
      processStatusNotifier.state = "Connected to Raspberry Pi";
      currentStatusNotifier.state = "Connected to RasPI";

      await Future.delayed(Duration(seconds: 2)); // Short delay

      currentStatusNotifier.state = "Waiting for command...";

      // Wait for "SW" before proceeding
      await waitForCommand();

      // await Future.delayed(Duration(seconds: 2)); // Short delay

      // currentStatusNotifier.state = "Ready to send SUP weight";
    } else {
      processStatusNotifier.state = "Failed to connect to Raspberry Pi";
      currentStatusNotifier.state = "Failed to connect to RasPI";
    }
  }

  Future<void> waitForCommand() async {
    if (port == null || !port!.isOpen) return;

    Completer<void> completer = Completer<void>(); // Used to pause execution

    Future.delayed(Duration.zero, () async {
      port!.flush(); // Clear buffer
      while (!completer.isCompleted) {
        if (port == null || !port!.isOpen) return; // Stop if port is closed

        Uint8List data = port!.read(2); // Read 2 bytes
        String message = String.fromCharCodes(data).trim(); // Convert to string

        print("Received: $message");

        if (message == "SW") {
          ref.read(currentStatusProvider.notifier).state = "Received: $message";

          await Future.delayed(Duration(seconds: 2)); // Short delay
          ref.read(currentStatusProvider.notifier).state =
              "Ready to send SUP weight";
          completer.complete(); // Unblock execution
        } else if (message == "CE") {
          ref.read(currentStatusProvider.notifier).state = "Received: $message";

          await Future.delayed(Duration(seconds: 2)); // Short delay
          ref.read(currentStatusProvider.notifier).state =
              "Ready to create ecobrick";
          completer.complete(); // Unblock execution
        } else if (message == "SF") {
          ref.read(currentStatusProvider.notifier).state = "Received: $message";

          await Future.delayed(Duration(seconds: 2)); // Short delay
          ref.read(currentStatusProvider.notifier).state = "SUP Full";

          await Future.delayed(Duration(seconds: 2)); // Short delay

          ref.read(currentStatusProvider.notifier).state =
              "Waiting for PET Bottle/create ecobrick";

          // Arduino will wait until bottle is inserted
          while (true) {
            Uint8List data = port!.read(2); // Read 2 bytes
            String message =
                String.fromCharCodes(data).trim(); // Convert to string

            print("Received: $message");

            if (message == "CE") {
              ref.read(currentStatusProvider.notifier).state =
                  "Received: $message";

              Future.delayed(Duration(seconds: 2)); // Short delay

              ref.read(currentStatusProvider.notifier).state =
                  "Ready to create ecobrick";
              break;
            }
            await Future.delayed(
              Duration(milliseconds: 50),
            ); // Small delay to prevent freezing
          }
          completer.complete(); // Unblock execution
        }

        await Future.delayed(
          Duration(milliseconds: 50),
        ); // Small delay to prevent freezing
      }
    });

    return completer.future; // Wait asynchronously
  }

  Future<void> sendSUPWeight(int command) async {
    if (port != null && port!.isOpen) {
      String data = "$command\n";
      port!.write(Uint8List.fromList(data.codeUnits));
      port!.flush();
      print("Sent: $command");
      ref.read(currentStatusProvider.notifier).state = "Sent $command";

      await Future.delayed(Duration(seconds: 2)); // Short delay

      ref.read(currentStatusProvider.notifier).state = "Waiting for command...";

      await Future.delayed(Duration(seconds: 2)); // Short delay

      // Wait for insertion command
      while (true) {
        Uint8List data = port!.read(2); // Read 2 bytes
        String message = String.fromCharCodes(data).trim(); // Convert to string

        print("Received: $message");

        if (message == "SW") {
          ref.read(currentStatusProvider.notifier).state = "Received: $message";

          await Future.delayed(Duration(seconds: 2)); // Short delay
          ref.read(currentStatusProvider.notifier).state =
              "Ready to send SUP weight";
          break;
        } else if (message == "CE") // If bottle is inserted first
        {
          ref.read(currentStatusProvider.notifier).state = "Received: $message";

          await Future.delayed(Duration(seconds: 2)); // Short delay
          ref.read(currentStatusProvider.notifier).state =
              "Ready to create ecobrick";
          break;
        } else if (message == "SF") // If SUP becomes full first
        {
          ref.read(currentStatusProvider.notifier).state = "Received: $message";

          await Future.delayed(Duration(seconds: 2)); // Short delay
          ref.read(currentStatusProvider.notifier).state = "SUP Full";

          await Future.delayed(Duration(seconds: 2)); // Short delay

          ref.read(currentStatusProvider.notifier).state =
              "Waiting for PET Bottle/create ecobrick";

          // Arduino will wait until bottle is inserted
          while (true) {
            Uint8List data = port!.read(2); // Read 2 bytes
            String message =
                String.fromCharCodes(data).trim(); // Convert to string

            print("Received: $message");

            if (message == "CE") {
              ref.read(currentStatusProvider.notifier).state =
                  "Received: $message";

              Future.delayed(Duration(seconds: 2)); // Short delay

              ref.read(currentStatusProvider.notifier).state =
                  "Ready to create ecobrick";
              break;
            }
            await Future.delayed(
              Duration(milliseconds: 50),
            ); // Small delay to prevent freezing
          }
          break;
        }
        await Future.delayed(
          Duration(milliseconds: 50),
        ); // Small delay to prevent freezing
      }
    } else {
      print("Serial port not open!");
      ref.read(currentStatusProvider.notifier).state = "Serial port not open!";
    }
  }

  Future<void> sendEcobrickCompleted(int command) async {
    // This should replicate levels/progress bar of the ecobrick
    // Can also send only a true or false value to indicate completion

    if (port != null && port!.isOpen) {
      // Uint8List data = Uint8List(1);
      // data[0] = command ? 1 : 0;
      // port!.write(data);
      // port!.flush();
      // print("Sent: (True)ECOBRICK_COMPLETED");
      // ref.read(currentStatusProvider.notifier).state =
      //     "Sent Ecobrick Completed";

      String data = "$command\n";
      port!.write(Uint8List.fromList(data.codeUnits));
      port!.flush();
      print("Sent: $command");
      ref.read(currentStatusProvider.notifier).state = "Ecobrick completed";

      await Future.delayed(Duration(seconds: 2)); // Short delay

      ref.read(currentStatusProvider.notifier).state = "Waiting for command...";
      // Wait again for command
      waitForCommand();
    } else {
      print("Serial port not open!");
      ref.read(currentStatusProvider.notifier).state = "Serial port not open!";
    }
  }

  @override
  void dispose() {
    subscription?.cancel();
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

              Consumer(
                builder: (context, ref, child) {
                  final processStatus = ref.watch(processStatusProvider);
                  return ElevatedButton(
                    onPressed: connectToRaspberryPi,
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
                  );
                },
              ),
              SizedBox(height: 40),

              Text("Current Status", style: TextStyle(fontSize: 20)),
              SizedBox(height: 10),

              Consumer(
                builder: (context, ref, child) {
                  final currentStatus = ref.watch(currentStatusProvider);
                  return Container(
                    width: 700,
                    padding: EdgeInsets.all(20),
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(30),
                      color: Colors.grey[200],
                    ),
                    child: Center(
                      child: Text(
                        currentStatus,
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 50,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  );
                },
              ),
              SizedBox(height: 20),
              // --------------------------- SUP WEIGHT --------------------------------------------------------------
              Consumer(
                builder: (context, ref, child) {
                  final supValue = ref.watch(supWeightProvider);
                  return Column(
                    children: [
                      Container(
                        width: 300,
                        padding: EdgeInsets.all(20),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(20),
                          color: Color.fromARGB(255, 122, 233, 255),
                        ),
                        child: Column(
                          children: [
                            Text(
                              "Enter weight of SUP",
                              style: TextStyle(
                                fontSize: 18,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                            SizedBox(height: 10),
                            Text(
                              "SUP Weight: ${supValue.toInt()}g",
                              style: TextStyle(fontSize: 12),
                            ),
                            Slider(
                              value: supValue,
                              max: 500,
                              onChanged:
                                  (value) =>
                                      ref
                                          .read(supWeightProvider.notifier)
                                          .state = value,
                              activeColor: Colors.black,
                              inactiveColor: const Color.fromARGB(
                                255,
                                0,
                                191,
                                255,
                              ),
                            ),
                            SizedBox(height: 10),

                            ElevatedButton(
                              onPressed:
                                  ref.watch(currentStatusProvider) ==
                                          "Ready to send SUP weight"
                                      ? () => sendSUPWeight(supValue.toInt())
                                      : null,
                              style: ButtonStyle(
                                fixedSize: WidgetStateProperty.all(
                                  Size(80, 20),
                                ),
                                padding: WidgetStateProperty.all(
                                  EdgeInsets.all(0),
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
                      // --------------------------- ECOBRICK PROGRESS --------------------------------------------------------------
                      SizedBox(height: 20),
                      ElevatedButton(
                        onPressed:
                            ref.watch(currentStatusProvider.notifier).state ==
                                    "Ready to create ecobrick"
                                ? () => sendEcobrickCompleted(
                                  1,
                                ) // 1 is true, 0 is false
                                : null,
                        style: ButtonStyle(
                          backgroundColor: WidgetStateProperty.all(
                            Color.fromARGB(255, 2, 255, 40),
                          ),
                          fixedSize: WidgetStateProperty.all(Size(250, 40)),
                          shadowColor: WidgetStateProperty.all(Colors.black),
                          elevation: WidgetStateProperty.all(3),
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
                    ],
                  );
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}
