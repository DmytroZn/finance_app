from rest_framework.response import Response
from rest_framework import status


class ObjectGetting:
    def __init__(self, obj, pk):
        self._obj = obj
        self._pk = pk

    def get_model(self):
        try:
            self._res = self._obj.objects.get(pk=self._pk)
        except self._obj.DoesNotExist:
            return False, Response({"msg": "Not_Found"}, status=status.HTTP_404_NOT_FOUND)
        return True, self._res
