from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tracking.models import Category, Spending
from tracking.serializers import CategorySerializer, SpendingSerializer
from tracking.utils import ObjectGetting, adding_user_id
# Create your views here.


class CategoryList(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    # permission_classes = [AllowAny]

    def get(self, request):
        categories = Category.objects.filter(is_active=True, fk_user=request.user.id)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    @adding_user_id
    def post(self, request):
        request.data["name_category"] = request.data["name_category"].strip()
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            if category := Category.objects.filter(name_category=request.data["name_category"],
                                                   fk_user=request.data["fk_user"]):
                category.update(is_active=True)
            else:
                serializer.save()
            return Response({"detail": "Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        if not (category := ObjectGetting(Category, pk=pk, fk_user=request.user.id).get_model())[0]:
            return category[1]
        category = category[1]
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        request.data["name_category"] = request.data["name_category"].strip()

        if not (category := ObjectGetting(Category, pk=pk, fk_user=request.user.id).get_model())[0]:
            return category[1]
        category = category[1]

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        fk_user = request.user.id
        if not (category := ObjectGetting(Category, pk=pk, fk_user=fk_user).get_model())[0]:
            return category[1]
        category = category[1]

        if Spending.objects.filter(fk_category=pk, fk_user=fk_user):
            category.is_active = False
            category.save()
        else:
            category.delete()
        return Response({"detail": "Deleted"}, status=status.HTTP_200_OK)


class SpendingList(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        spending = Spending.objects.filter(fk_user=request.user.id)
        serializer = SpendingSerializer(spending, many=True)
        return Response(serializer.data)

    @adding_user_id
    def post(self, request):
        serializer = SpendingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpendingDetail(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        if not (spending := ObjectGetting(Spending, pk=pk, fk_user=request.user.id).get_model())[0]:
            return spending[1]
        spending = spending[1]

        serializer = SpendingSerializer(spending)
        return Response(serializer.data)

    @adding_user_id
    def put(self, request, pk):
        if not (spending := ObjectGetting(Spending, pk=pk, fk_user=request.user.id).get_model())[0]:
            return spending[1]
        spending = spending[1]

        serializer = SpendingSerializer(spending, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not (spending := ObjectGetting(Spending, pk=pk, fk_user=request.user.id).get_model())[0]:
            return spending[1]
        spending[1].delete()
        return Response({"detail": "Deleted"}, status=status.HTTP_200_OK)
