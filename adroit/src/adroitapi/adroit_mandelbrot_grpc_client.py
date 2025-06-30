import asyncio
import logging
import multiprocessing

from adroit_coding_challenge.server.adroit_grpc_server import AdroitServer
from adroit_coding_challenge.protos import Mandelbrot_pb2
from my_adroit_client import MyAdroitClient


def compute_mandelbrot_point_example(
    client: MyAdroitClient | None = None,
    real: float = 0.0,
    imaginary: float = 0.0,
    max_iterations: int = 20,
) -> Mandelbrot_pb2.MandelbrotPoint:
    """
    Driver function to compute a single Mandelbrot point.

    This function prepares a request to calculate the number of iterations for
    a single complex point, then forwards it to the client’s gRPC call, and returns
    the resulting MandelbrotPoint.
    """
    if client is None:
        client = MyAdroitClient("localhost", port=50051)

    result = client.compute_mandelbrot_point(real, imaginary, max_iterations)
    assert isinstance(result, Mandelbrot_pb2.MandelbrotPoint)
    assert result.value.real is not None, "real component missing"
    assert result.value.imaginary is not None, "imaginary component missing"
    assert result.iterations >= 0, "iterations should be non-negative"

    return result


def generate_mandelbrot_example(
    client: MyAdroitClient | None = None,
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
    """
    Driver function to generate a Mandelbrot fractal over a defined area.

    This function sets up a bounding box and resolution describing the fractal
    area, forwards the request to the client, and returns the calculated
    Mandelbrot results.
    """
    if client is None:
        client = MyAdroitClient("localhost", port=50051)

    result = client.generate_mandelbrot(
        width,
        height,
        corner1_real,
        corner1_imaginary,
        corner2_real,
        corner2_imaginary,
        max_iterations,
    )
    assert isinstance(result, Mandelbrot_pb2.MandelbrotResults)
    assert result.resolution.x == width, "resolution x mismatch"
    assert result.resolution.y == height, "resolution y mismatch"

    return result


def generate_mandelbrot_stream_example(
    client: MyAdroitClient | None = None,
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
    """
    Driver function to generate Mandelbrot fractal pixel data using a stream.

    This function requests a Mandelbrot stream from the server for the specified
    bounding box and resolution, collects the streamed MandelbrotPixel messages
    into a list, and returns them.
    """
    if client is None:
        client = MyAdroitClient("localhost", port=50051)

    pixels = client.generate_mandelbrot_stream(
        width,
        height,
        corner1_real,
        corner1_imaginary,
        corner2_real,
        corner2_imaginary,
        max_iterations,
    )
    assert isinstance(pixels, list), "pixels should be a list"

    if pixels:
        assert isinstance(
            pixels[0], Mandelbrot_pb2.MandelbrotPixel
        ), "first pixel is not MandelbrotPixel"
        assert pixels[0].position.x >= 0, "invalid pixel x coordinate"

    return pixels


async def run_examples():
    """
    Convenience coroutine to run all example driver functions sequentially.

    This function demonstrates how to invoke the driver methods for:
    - computing a single Mandelbrot point
    - generating a Mandelbrot image
    - streaming Mandelbrot pixels
    """
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
    logging.getLogger().info("Server initialization starting.")
    server_process = multiprocessing.Process(target=run_server)
    server_process.start()

    asyncio.run(run_examples())

    server_process.join()
