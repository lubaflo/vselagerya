from rest_framework import viewsets, serializers
from .models import Camp, Document, Shift, Group, Review

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'file_url', 'status', 'checked_at')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'age_label', 'capacity', 'current', 'base_price', 'current_price', 'next_price')

class ShiftSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = Shift
        fields = ('id', 'title', 'date_start', 'date_end', 'groups')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'author', 'rating', 'text')

class CampSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True, read_only=True)
    shifts = ShiftSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Camp
        fields = ('id', 'name', 'region', 'short_desc', 'price_from', 'rating', 'image', 'documents', 'shifts', 'reviews')

class CampViewSet(viewsets.ModelViewSet):
    queryset = Camp.objects.all().order_by('id')
    serializer_class = CampSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all().order_by('id')
    serializer_class = ShiftSerializer
