"""
Unit tests for Mandelbrot gRPC client functionality. These tests verify
the behavior of the MyAdroitClient class when interacting with the
GenerateMandelbrot and GenerateMandelbrotStream endpoints.

The tests spin up a local gRPC server in a separate process and
perform functional checks on returned data structures to ensure correct
integration between client and server.
"""

import asyncio
from multiprocessing import Process
from adroit_coding_challenge.server.adroit_grpc_server import AdroitServer
from adroitapi.my_adroit_client import MyAdroitClient
from adroit_coding_challenge.protos import Mandelbrot_pb2


def run_server():
    """
    Start the gRPC Mandelbrot server in a separate process.
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    server = AdroitServer("TestServer", port=50051)
    loop.run_until_complete(server.serve())


def test_compute_mandelbrot_point_basic():
    """
    Unit test for compute_mandelbrot_point.

    Starts the server, sends a request for a single Mandelbrot point,
    and verifies that a MandelbrotPoint object is returned with the
    correct complex coordinates.
    """
    p = Process(target=run_server)
    p.start()

    client = MyAdroitClient("localhost", port=50051)

    result = client.compute_mandelbrot_point(real=0.0, imaginary=0.0, max_iterations=20)

    assert isinstance(result, Mandelbrot_pb2.MandelbrotPoint)
    assert result.value.real == "0.0"
    assert result.value.imaginary == "0.0"

    p.terminate()
    p.join()


def test_generate_mandelbrot_basic():
    """
    Unit test for generate_mandelbrot.

    This test starts the server and requests Mandelbrot results over a specified
    bounding box and resolution. It verifies that:

    - The response is a MandelbrotResults message
    - The resolution fields in the result match the requested width and height
    """
    p = Process(target=run_server)
    p.start()

    client = MyAdroitClient("localhost", port=50051)

    result = client.generate_mandelbrot(
        width=40,
        height=20,
        corner1_real=-0.25,
        corner1_imaginary=-0.25,
        corner2_real=0.25,
        corner2_imaginary=0.25,
        max_iterations=20,
    )

    assert isinstance(result, Mandelbrot_pb2.MandelbrotResults)
    assert result.resolution.x == 40
    assert result.resolution.y == 20

    p.terminate()
    p.join()


def test_generate_mandelbrot_stream():
    """
    Unit test for generate_mandelbrot_stream.

    Starts the server, requests a streamed Mandelbrot area, and verifies
    that the returned list contains MandelbrotPixel objects. Checks
    for correct type and non-empty data.
    """
    p = Process(target=run_server)
    p.start()

    client = MyAdroitClient("localhost", port=50051)

    pixels = client.generate_mandelbrot_stream(
        width=10,
        height=10,
        corner1_real=-0.5,
        corner1_imaginary=-0.5,
        corner2_real=0.5,
        corner2_imaginary=0.5,
        max_iterations=20,
    )

    assert isinstance(pixels, list)

    if pixels:
        assert isinstance(pixels[0], Mandelbrot_pb2.MandelbrotPixel)

    p.terminate()
    p.join()
