# Prototype QR Code Scanner

An application that decodes JWT tokens embedded within QR Codes. It displays the decoded payload in a dialog. The project is designed with modular architecture for maintanibility and scalability.

### Folder Structure
```
lib/
├── constants/         # For global constants (currently unused).
├── screens/           # Contains app screens.
│   └── scanner_screen.dart
├── services/          # Encapsulates reusable logic.
│   └── jwt_service.dart
├── utils/             # Helper functions (currently unused).
├── widgets/           # Reusable UI components.
│   └── jwt_dialog.dart
├── main.dart          # App entry point.
├── .env               # Environment variables (e.g., secret key).
```
Reference: https://dev.to/yatendra2001/a-comprehensive-guide-to-creating-a-scalable-folder-structure-for-flutter-apps-1o5i

### Prerequisites
Before installing and running the application, follow this:
https://docs.flutter.dev/get-started/install


### Installation Guide
1. Clone the repository
2. Install Dependencies: `flutter pub get`
3. Set Up Secret key
4. Run the application `flutter run`

### Dependencies
- `mobile_scanner`
- `dart_jsonwebtoken`
- `flutter_dotenv`