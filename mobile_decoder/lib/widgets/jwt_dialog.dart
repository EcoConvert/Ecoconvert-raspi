import 'dart:typed_data';
import 'package:flutter/material.dart';

class JWDialog extends StatelessWidget {
  final String payload;
  final Uint8List? image;

  const JWDialog({
    super.key,
    required this.payload,
    this.image,
  });

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: const Text('Decoded JWT Payload'),
      content: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Text(
            payload,
            style: const TextStyle(fontSize: 16),
          ),
          if (image != null) 
            Padding(
              padding: const EdgeInsets.only(top: 8.0),
              child: Image(image:  MemoryImage(image!)),
            ),
        ],
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context),
          child: const Text('Close',)
        )
      ],
    );
  }
}