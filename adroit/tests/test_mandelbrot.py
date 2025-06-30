import asyncio
from multiprocessing import Process
from adroit_coding_challenge.server.adroit_grpc_server import AdroitServer
from adroitapi.my_adroit_client import MyAdroitClient
from adroit_coding_challenge.protos import Mandelbrot_pb2


def run_server():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    server = AdroitServer("TestServer", port=50051)
    loop.run_until_complete(server.serve())


def test_compute_mandelbrot_point_basic():
    p = Process(target=run_server)
    p.start()

    client = MyAdroitClient("localhost", port=50051)

    result = client.compute_mandelbrot_point(
        real=0.0,
        imaginary=0.0,
        max_iterations=20
    )

    assert isinstance(result, Mandelbrot_pb2.MandelbrotPoint)
    assert result.value.real == "0.0"
    assert result.value.imaginary == "0.0"

    p.terminate()
    p.join()


def test_generate_mandelbrot_basic():
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
        max_iterations=20
    )

    assert isinstance(result, Mandelbrot_pb2.MandelbrotResults)
    assert result.resolution.x == 40
    assert result.resolution.y == 20

    p.terminate()
    p.join()


def test_generate_mandelbrot_stream():
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
        max_iterations=20
    )

    assert isinstance(pixels, list)

    if pixels:
        assert isinstance(pixels[0], Mandelbrot_pb2.MandelbrotPixel)

    p.terminate()
    p.join()
