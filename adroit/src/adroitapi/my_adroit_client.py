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

    def compute_mandelbrot_point(
        self, real: float, imaginary: float, max_iterations: int = 20
    ) -> Mandelbrot_pb2.MandelbrotPoint:
        request = Mandelbrot_pb2.ComputeMandelbrotPointRequest(
            point=Mandelbrot_pb2.ComplexNumber(
                real=str(real), imaginary=str(imaginary)
            ),
            max_iterations=max_iterations,
        )
        return self.stub.ComputeMandelbrotPoint(request)

    def generate_mandelbrot(
        self,
        width: int,
        height: int,
        corner1_real: float,
        corner1_imaginary: float,
        corner2_real: float,
        corner2_imaginary: float,
        max_iterations: int = 20,
    ) -> Mandelbrot_pb2.MandelbrotResults:
        resolution = Mandelbrot_pb2.IntegerOrderedPair(x=width, y=height)

        bounding_box = Mandelbrot_pb2.BoundingBox(
            corner1=Mandelbrot_pb2.ComplexNumber(
                real=str(corner1_real), imaginary=str(corner1_imaginary)
            ),
            corner2=Mandelbrot_pb2.ComplexNumber(
                real=str(corner2_real), imaginary=str(corner2_imaginary)
            ),
        )

        bounds = Mandelbrot_pb2.BoundsDescriptor(bounding_box=bounding_box)

        request = Mandelbrot_pb2.GenerateMandelbrotRequest(
            resolution=resolution, bounds=bounds, max_iterations=max_iterations
        )

        return self.stub.GenerateMandelbrot(request)

    def generate_mandelbrot_stream(
        self,
        width: int,
        height: int,
        corner1_real: float,
        corner1_imaginary: float,
        corner2_real: float,
        corner2_imaginary: float,
        max_iterations: int = 20,
    ) -> list[Mandelbrot_pb2.MandelbrotPixel]:
        resolution = Mandelbrot_pb2.IntegerOrderedPair(x=width, y=height)

        bounding_box = Mandelbrot_pb2.BoundingBox(
            corner1=Mandelbrot_pb2.ComplexNumber(
                real=str(corner1_real), imaginary=str(corner1_imaginary)
            ),
            corner2=Mandelbrot_pb2.ComplexNumber(
                real=str(corner2_real), imaginary=str(corner2_imaginary)
            ),
        )

        bounds = Mandelbrot_pb2.BoundsDescriptor(bounding_box=bounding_box)

        request = Mandelbrot_pb2.GenerateMandelbrotRequest(
            resolution=resolution, bounds=bounds, max_iterations=max_iterations
        )

        pixels: list[Mandelbrot_pb2.MandelbrotPixel] = []
        for pixel in self.stub.GenerateMandelbrotStream(request):
            pixels.append(pixel)

        return pixels
