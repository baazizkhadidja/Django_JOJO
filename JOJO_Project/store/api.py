from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


from store.models import Gateau, Album, Contact, Booking
from store.serializer import GatSerializer



@api_view(['GET',])
def api_all_gat(request):
    all_gat = Gateau.objects.all()
    data = GatSerializer(all_gat, many=True).data
    return Response(data)


@api_view(['GET',])
def api_detail_gat(request, id):

    try:
        gat = Gateau.objects.get(id=id)
    except Gateau.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = GatSerializer(gat)
        return Response(serializer.data)



@api_view(['PUT',])
def api_update_gat(request, id):

    try:
        gat = Gateau.objects.get(id=id)
    except Gateau.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = GatSerializer(gat, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['DELETE',])
def api_delete_gat(request, id):

    try:
        gat = Gateau.objects.get(id=id)
    except Gateau.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = gat.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)





@api_view(['POST',])
def api_create_gat(request, id):

    try:
        gat = Gateau.objects.get(id=id)
    except Gateau.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        operation = gat.save()
        data = {}
        if operation:
            data["success"] = "post succeful"
        else:
            data["failure"] = "post failed"
        return Response(data=data)




class GateauAdd(generics.ListCreateAPIView):
    queryset = Gateau.objects.all()
    serializer_class = GatSerializer