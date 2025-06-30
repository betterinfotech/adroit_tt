from adroit_coding_challenge.client.adroit_grpc_client import AdroitClient
from adroit_coding_challenge.protos import Mandelbrot_pb2
from adroit_coding_challenge.protos import Mandelbrot_pb2_grpc


class MyAdroitClient(AdroitClient):
    """
    Derived client with stubs for required methods
    """

    def __init__(self, host: str, port: int = 50051):
        super().__init__(host, port)
        self.stub = Mandelbrot_pb2_grpc.MandelbrotGeneratorStub(self.channel)

    def compute_mandelbrot_point(self, real: float, imaginary: float, max_iterations: int = 20) -> Mandelbrot_pb2.MandelbrotPoint:
        request = Mandelbrot_pb2.ComputeMandelbrotPointRequest(  # CORRECT
            point=Mandelbrot_pb2.ComplexNumber(real=str(real), imaginary=str(imaginary)),
            max_iterations=max_iterations
        )
        return self.stub.ComputeMandelbrotPoint(request)

    def generate_mandelbrot(self, width: int, height: int,
                            corner1_real: float, corner1_imaginary: float,
                            corner2_real: float, corner2_imaginary: float,
                            max_iterations: int = 20) -> Mandelbrot_pb2.MandelbrotResults:
        request = Mandelbrot_pb2.MandelbrotAreaRequest(
            resolution=Mandelbrot_pb2.Resolution(x=width, y=height),
            corner1=Mandelbrot_pb2.ComplexNumber(real=str(corner1_real), imaginary=str(corner1_imaginary)),
            corner2=Mandelbrot_pb2.ComplexNumber(real=str(corner2_real), imaginary=str(corner2_imaginary)),
            max_iterations=max_iterations
        )
        return self.stub.GenerateMandelbrot(request)

    def generate_mandelbrot_stream(self, width: int, height: int,
                                   corner1_real: float, corner1_imaginary: float,
                                   corner2_real: float, corner2_imaginary: float,
                                   max_iterations: int = 20) -> list[Mandelbrot_pb2.MandelbrotPixel]:
        # dummy implementation returning an empty list
        request = Mandelbrot_pb2.MandelbrotAreaRequest(
            resolution=Mandelbrot_pb2.Resolution(x=width, y=height),
            corner1=Mandelbrot_pb2.ComplexNumber(real=str(corner1_real), imaginary=str(corner1_imaginary)),
            corner2=Mandelbrot_pb2.ComplexNumber(real=str(corner2_real), imaginary=str(corner2_imaginary)),
            max_iterations=max_iterations
        )
        pixels = []
        for pixel in self.stub.GenerateMandelbrotStream(request):
            pixels.append(pixel)
        return pixels
