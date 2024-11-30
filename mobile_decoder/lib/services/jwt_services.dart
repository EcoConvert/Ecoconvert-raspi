import 'package:dart_jsonwebtoken/dart_jsonwebtoken.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

class JWTService {
    // Decodes a JWT and return payload or a error message
    static String decodeJWT(String token) {
        final String? secretKey = dotenv.env['SECRET_KEY'];

        if (secretKey == null || secretKey.isEmpty) {
            return 'Error: SECRET_KEY is not found';
        }

        try {
            final jwt = JWT.verify(token, SecretKey(secretKey));
            return jwt.payload.toString(); // Convert payload to string
        } on JWTExpiredException {
            return 'Error: JWT Expried';
        } on JWTException catch (e) {
            return ' Error: ${e.message}';
        }
    }
}