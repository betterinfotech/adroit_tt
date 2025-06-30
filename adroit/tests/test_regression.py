"""
Regression tests for the Mandelbrot gRPC server implementation.
These tests verify that existing endpoints continue to function correctly
and that backward compatibility is preserved while extending functionality.
"""

from multiprocessing import Process
import asyncio
from adroit_coding_challenge.server.adroit_grpc_server import AdroitServer
from adroitapi.my_adroit_client import MyAdroitClient
from adroit_coding_challenge.protos import Mandelbrot_pb2


def run_server():
    """
    Used to launch the gRPC server in a separate process.
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    server = AdroitServer("TestServer", port=50051)
    loop.run_until_complete(server.serve())


def test_basic_mandelbrot():
    """
    Regression test for compute_mandelbrot_point functionality.
    Starts the server, sends a request to compute a Mandelbrot point,
    and validates that the response structure is correct.
    """
    p = Process(target=run_server)
    p.start()

    # client = AdroitClient("localhost", port=50051)
    client = MyAdroitClient("localhost", port=50051)
    result = client.compute_mandelbrot_point(0.0, 0.0, 20)

    assert isinstance(result, Mandelbrot_pb2.MandelbrotPoint)
    assert float(result.value.real) == 0.0
    assert float(result.value.imaginary) == 0.0

    p.terminate()
    p.join()
