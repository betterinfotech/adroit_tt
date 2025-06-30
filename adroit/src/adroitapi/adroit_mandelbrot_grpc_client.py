import asyncio
import logging
import multiprocessing

from adroit_coding_challenge.server.adroit_grpc_server import AdroitServer
from adroit_coding_challenge.client.adroit_grpc_client import AdroitClient
from adroit_coding_challenge.protos import Mandelbrot_pb2
from adroit_coding_challenge.protos import Mandelbrot_pb2_grpc


# TODO
#  Define a derived class of AdroitClient which implements the following gRPC endpoint:
#  - ComputeMandelbrotPoint
#  - GenerateMandelbrot
#  - GenerateMandelbrotStream


def compute_mandelbrot_point_example(
    client: AdroitClient = None,
    real: float = 0.0,
    imaginary: float = 0.0,
    max_iterations: int = 20,
) -> Mandelbrot_pb2.MandelbrotPoint:
    # TODO
    #  Implement a method which acts as a driver method for client.compute_mandelbrot_point
    #  This function should:
    #  - Handle the request formation
    #  - Return the response data
    raise NotImplementedError


def generate_mandelbrot_example(
    client: AdroitClient = None,
    width: int = 40,  # corresponds to resolution.x
    height: int = 20,  # corresponds to resolution.y
    # first corner for a bounding box
    corner1_real: float = -0.25,
    corner1_imaginary: float = -0.25,
    # second corner for a bounding box
    corner2_real: float = 0.25,
    corner2_imaginary: float = 0.25,
    max_iterations: int = 20,
) -> Mandelbrot_pb2.MandelbrotResults:
    # TODO
    #  Implement a method which acts as a driver method for client.generate_mandelbrot
    #  This function should:
    #  - Handle the request formation
    #  - Return the response data
    raise NotImplementedError


def generate_mandelbrot_stream_example(
    client: AdroitClient = None,
    width: int = 40,  # corresponds to resolution.x
    height: int = 20,  # corresponds to resolution.y
    # first corner for a bounding box
    corner1_real: float = -0.25,
    corner1_imaginary: float = -0.25,
    # second corner for a bounding box
    corner2_real: float = 0.25,
    corner2_imaginary: float = 0.25,
    max_iterations: int = 20,
) -> list[Mandelbrot_pb2.MandelbrotPixel]:
    # TODO
    #  Implement a method which acts as a driver method for client.generate_mandelbrot_stream
    #  This function should:
    #  - Handle the request formation
    #  - Queue handling
    #  - Return all of the data from the queue
    #  Reminder: You may define and use a helper function, if necessary.
    raise NotImplementedError


async def run_examples():
    compute_mandelbrot_point_example()
    generate_mandelbrot_example()
    generate_mandelbrot_stream_example()


# Nothing below here requires modification to complete this assessment.
def run_server(stop_after_seconds: int = 5):
    loop = asyncio.get_event_loop()
    server = AdroitServer("Example", port=50051, max_workers=10)
    loop.call_later(stop_after_seconds, server.stop)
    loop.run_until_complete(server.serve())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.getLogger().info(f"Server initialization starting.")
    server_process = multiprocessing.Process(target=run_server)
    server_process.start()

    run_examples()

    server_process.join()
