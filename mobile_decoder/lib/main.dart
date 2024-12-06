import 'package:flutter/material.dart';
import 'screens/scanner_screen.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';


Future<void> main() async {
  // WidgetsFlutterBinding.ensureInitialized();
  await dotenv.load(fileName: ".env");
  runApp(const MyApp());
}

// Stateless means it doens't change
class MyApp extends StatelessWidget { // Constructor 
    const MyApp({super.key});


    @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'QR Code Scanner',
        theme: ThemeData(
            colorScheme: ColorScheme.fromSeed(seedColor: Colors.blueGrey),
            useMaterial3: true,
        ),
        home: const ScannerScreen() // Scanner View is the main interface of scanning QR
    );
  }
}