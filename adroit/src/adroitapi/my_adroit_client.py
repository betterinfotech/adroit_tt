from adroit_coding_challenge.client.adroit_grpc_client import AdroitClient
from adroit_coding_challenge.protos import Mandelbrot_pb2


class MyAdroitClient(AdroitClient):
    """
    Derived client with stubs for required methods
    """

    def compute_mandelbrot_point(self, real: float, imaginary: float, max_iterations: int = 20) -> Mandelbrot_pb2.MandelbrotPoint:
        # Dummy implementation so regression tests do not fail.
        return Mandelbrot_pb2.MandelbrotPoint(
            value=Mandelbrot_pb2.ComplexNumber(real=str(real), imaginary=str(imaginary)),
            iterations=max_iterations,
            diverges=Mandelbrot_pb2.MandelbrotPoint.FALSE
        )


    def generate_mandelbrot(self, width: int, height: int,
                            corner1_real: float, corner1_imaginary: float,
                            corner2_real: float, corner2_imaginary: float,
                            max_iterations: int = 20) -> Mandelbrot_pb2.MandelbrotResults:
        # dummy implementation
        return Mandelbrot_pb2.MandelbrotResults()

    def generate_mandelbrot_stream(self, width: int, height: int,
                                   corner1_real: float, corner1_imaginary: float,
                                   corner2_real: float, corner2_imaginary: float,
                                   max_iterations: int = 20) -> list[Mandelbrot_pb2.MandelbrotPixel]:
        # dummy implementation returning an empty list
        return []
