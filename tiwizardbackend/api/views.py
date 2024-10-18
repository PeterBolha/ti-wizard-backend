from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .helpers import get_collection
from .serializers import SamlSpSerializer


# from helpers import get_collection


# Create your views here.
def index(request):
    return HttpResponse("Hello world!")


def oidc_op(request):
    return HttpResponse("Testing OIDC OP response")


def oidc_rp(request):
    return HttpResponse("Testing OIDC RP response")


def saml_idp(request):
    return HttpResponse("Testing SAML IdP response")


def saml_sp(request):
    return HttpResponse("Testing SAML SP response")


class SamlBaseEntity(APIView):

    def __init__(self, collection_name: str):
        super().__init__()
        self._collection_name = collection_name

    def get_object(self, entityid: str):
        collection = get_collection(self._collection_name)
        try:
            sp = collection.find_one({"entityid": entityid})
            if sp:
                sp["_id"] = str(sp["_id"])
            return sp
        except Exception:
            return None

    def get(self, request) -> Response:
        entityid = request.data.get("entityid")
        if not entityid:
            return Response(f"Required parameter 'entityid' is missing in the request. Actual content: {request.data}",
                            status=HTTPStatus.BAD_REQUEST)

        sp = self.get_object(entityid)
        return Response(sp) if sp else Response({"error": f"Item with entity ID: '{entityid}' not found"},
                                                status=HTTPStatus.NOT_FOUND)

    def post(self, request) -> Response:
        serializer = SamlSpSerializer(data=request.data)

        if serializer.is_valid():
            collection = get_collection(self._collection_name)

            result = collection.insert_one(serializer.validated_data)
            inserted_id = str(result.inserted_id)

            return Response(f"Item created successfully with id: '{inserted_id}'", status=HTTPStatus.CREATED)

        return Response(
            f"Item was not serialized successfully and could not be inserted. Following errors occurred: '"
            f"{serializer.errors}'",
            status=HTTPStatus.BAD_REQUEST)

    def put(self, request) -> Response:
        entityid = request.data.get("entityid")

        if not entityid:
            return Response(f"Required parameter 'entityid' is missing in the request. Actual content: {request.data}",
                            status=HTTPStatus.BAD_REQUEST)

        serializer = SamlSpSerializer(data=request.data)
        if serializer.is_valid():
            collection = get_collection(self._collection_name)

            sp = collection.find_one({"entityid": entityid})
            if sp:
                collection.update_one({"entityid": sp["entityid"]}, {"$set": serializer.validated_data})
                return Response(f"Updated item with entityid: '{entityid}'", HTTPStatus.OK)
            else:
                result = collection.insert_one(serializer.validated_data)
                inserted_id = str(result.inserted_id)

                return Response(
                    f"Item with entityid: '{entityid}' was not found so it was created with id: '{inserted_id}'",
                    HTTPStatus.CREATED)

        return Response(
            f"Item was not serialized successfully and could not be inserted. Following errors occurred: '"
            f"{serializer.errors}'",
            status=HTTPStatus.BAD_REQUEST)

    def delete(self, request) -> Response:
        entityid = request.data.get("entityid")

        if not entityid:
            return Response(f"Required parameter 'entityid' is missing in the request. Actual content: {request.data}",
                            status=HTTPStatus.BAD_REQUEST)

        collection = get_collection(self._collection_name)
        result = collection.delete_one({"entityid": entityid})

        if result.deleted_count == 1:
            return Response(f"Item with entityID '{entityid}' was deleted successfully", HTTPStatus.OK)

        return Response(f"Failed to delete item with entityID: '{entityid}'", status=HTTPStatus.BAD_REQUEST)


class SamlSp(SamlBaseEntity):
    _collection_name = "saml_sp"

    def __init__(self):
        super().__init__(self._collection_name)


class SamlIdp(SamlBaseEntity):
    _collection_name = "saml_idp"

    def __init__(self):
        super().__init__(self._collection_name)
