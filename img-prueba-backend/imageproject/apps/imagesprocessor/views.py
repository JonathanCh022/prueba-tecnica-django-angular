from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ImagenSerializer
from .models import Imagen
from PIL import Image
from django.conf import settings
import os


class ImageProcessor(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = ImagenSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            w, h, o = self.processing_image(file_serializer.data)
            Imagen.objects.all().delete()
            #return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            return Response({"width": w, "height": h, "orient": o}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def processing_image(self, image_obj):
        """ Retorna las dimensiones y  la orientacion recomendada para la imagen cargada.
        """

        image = Image.open(os.path.normpath(settings.BASE_DIR) + image_obj["file"])
        width = image.size[0]
        height = image.size[1]
        a4_width, a4_height = 796, 1123
        orient = "vert"

        if width == height:
            if width > a4_width:
                n_width, n_heigth = self.resize_image_width(width, height)
            else:
                n_width, n_heigth = width, height
        elif height > width:
            if height > a4_height:
                n_width, n_heigth = self.resize_image_height(width, height)
                if n_width > a4_width:
                    n_width, n_heigth = self.resize_image_width(n_width, n_heigth)
            else:

                n_width, n_heigth = width, height

        else:
            if width > a4_height:
                orient = "horiz"
                n_width, n_heigth = self.resize_image_height(height, width)
                if n_width > a4_width:
                    n_width, n_heigth = self.resize_image_width(n_width, n_heigth)

            else:
                n_width, n_heigth = width, height

        return n_width, n_heigth, orient

    def resize_image_width(self, w, h):
        base_width = 796
        w_percent = (base_width / float(w))
        hsize = int((float(h) * float(w_percent)))
        return base_width, hsize

    def resize_image_height(self, w, h):
        base_height = 1123
        h_percent = (base_height / float(h))
        wsize = int((float(w) * float(h_percent)))
        return wsize, base_height
