import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:mobile_scanner/mobile_scanner.dart';
import '../services/jwt_services.dart';
import '../widgets/jwt_dialog.dart';

// Stateful -> change over time, mutable
class ScannerView extends StatefulWidget {
  const ScannerView({super.key});

  @override
  State<ScannerView> createState() => _ScannerViewState();
}

class _ScannerViewState extends State<ScannerView> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: MobileScanner(
        controller: MobileScannerController(
          detectionSpeed: DetectionSpeed.noDuplicates,
          returnImage: true,
        ),
        onDetect: (capture) {
          final List<Barcode> barcodes = capture.barcodes;
          final Uint8List? image = capture.image;

          for (final barcode in barcodes) {
            final String? raw_value = barcode.rawValue;
            if (raw_value != null) {
              //Decode JWT
              final payload = JWTService.decodeJWT(raw_value);

              // Show the dialog
              showDialog(
                context: context,
                builder: (context) => JWDialog(payload:  payload, image: image),
              );
            } 
          }
        },
      ),
    );
  }
}