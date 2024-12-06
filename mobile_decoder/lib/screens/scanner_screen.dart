import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:mobile_scanner/mobile_scanner.dart';
import '../services/jwt_services.dart';
import '../widgets/jwt_dialog.dart';

// Stateful -> change over time, mutable
class ScannerScreen extends StatefulWidget {
  const ScannerScreen({super.key});

  @override
  State<ScannerScreen> createState() => _ScannerScreenState();
}

//TODO: Implement Pause after Scanning
//TODO: Toggle on and off of camera

class _ScannerScreenState extends State<ScannerScreen> {
  final MobileScannerController _cameraController = MobileScannerController(
    // The scan qr will return to us
    detectionSpeed: DetectionSpeed.noDuplicates,
    returnImage: true,
  );

  final Set<String> _scannedQRCodes = {}; // Set to avoid duplicates
  bool _isCameraActive =
      true; // Default is true, meaning at the start the camera is active

  // Function that will toggle camera in the app bar
  void _toggleCamera() {
    setState(() {
      if (_isCameraActive) {
        // Stop the camera -> either already scan a qr or manually stop
        _cameraController.stop();
      } else {
        // Camera is false -> off
        _cameraController.start();
      }
      // If the camera is true -> set to opposite
      _isCameraActive = !_isCameraActive;
    });
  }

  // Dispose the controller when the widget is destroyed
  @override
  void dispose() {
    _cameraController.dispose();
    super.dispose();
  }

  // Actual logic for handling scanned qr code
  void _handleQRCode(BuildContext context, BarcodeCapture capture) {
    final List<Barcode> barcodes = capture.barcodes;
    final Uint8List? image = capture.image;

    // Loop through detected QR
    for (final barcode in barcodes) {
      // Check the QR string value
      final String? rawValue = barcode.rawValue;

      // Check if the QR Code is repeated or not
      if (rawValue != null && !_scannedQRCodes.contains(rawValue)) {
        // Append the qr code
        _scannedQRCodes.add(rawValue);

        // Decode the QR Code
        final payload = JWTService.decodeJWT(rawValue);

        // Show the dialog
        showDialog(
          context: context,
          builder: (context) => JWDialog(
            payload: payload,
            image: image,
          ),
        );

        // After showing the dialog, paused the camera
        _cameraController.stop();
        // call the wdidget to change
        setState(() {
          // Turn of the camera
          _isCameraActive = false;
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("QR Code Scanner"),
          actions: [
            IconButton(
              icon: Icon(_isCameraActive ? Icons.pause : Icons.play_arrow),
              onPressed: _toggleCamera,
            ),
          ],
        ),
        body: Stack(
          // Overlapping widget
          children: [
            MobileScanner(
              controller: _cameraController,
              onDetect: (capture) => _handleQRCode(context, capture),
            ),
            if (!_isCameraActive)
              Center(
                child: Container(
                    color: Colors.black.withOpacity(0.7),
                    child: const Text(
                      "Camera Paused",
                      style: TextStyle(color: Colors.white, fontSize: 24),
                    )),
              )
          ],
        ));
  }
}
