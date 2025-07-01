# Architecture

The system is based on gRPC services with separate client and server modules:

- **Server**: Implements gRPC Mandelbrot services
- **Client**: Consumes the server’s endpoints via stubs
- **Drivers**: Provide examples of using the endpoints
- **Testing**: Uses pytest with local multiprocessing to validate functionality

A high-level flow:
1. Client forms a request
2. Request sent over gRPC
3. Server computes Mandelbrot results
4. Client handles and validates responses
