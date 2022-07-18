from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tracking.models import Category, Spending
from tracking.serializers import CategorySerializer, SpendingSerializer
# Create your views here.


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data["name_category"] = request.data["name_category"].strip()
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            if category := Category.objects.filter(name_category=request.data["name_category"]):
                category.update(is_active=True)
            else:
                serializer.save()
            return Response({"msg": "Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"msg": "Not_Content"}, status=status.HTTP_204_NO_CONTENT)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        request.data["name_category"] = request.data["name_category"].strip()

        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"msg": "Not_Content"}, status=status.HTTP_204_NO_CONTENT)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Updated"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"msg": "Not_Content"}, status=status.HTTP_204_NO_CONTENT)
        if Spending.objects.filter(fk_category=pk):
            category.is_active = False
            category.save()
        else:
            category.delete()
        return Response({"msg": "Deleted"}, status=status.HTTP_201_CREATED)


class SpendingList(APIView):
    def get(self, request, format=None):
        spending = Spending.objects.all()
        serializer = SpendingSerializer(spending, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SpendingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpendingDetail(APIView):
    def get(self, request, pk):
        try:
            category = Spending.objects.get(pk=pk)
        except Spending.DoesNotExist:
            return Response({"msg": "Not_Content"}, status=status.HTTP_204_NO_CONTENT)
        serializer = SpendingSerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        spending = Spending.objects.get(pk=pk)
        serializer = SpendingSerializer(spending, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Updated"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            spending = Spending.objects.get(pk=pk)
        except Spending.DoesNotExist:
            return Response({"msg": "Not_Content"}, status=status.HTTP_204_NO_CONTENT)
        spending.delete()
        return Response({"msg": "Deleted"}, status=status.HTTP_201_CREATED)
