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
