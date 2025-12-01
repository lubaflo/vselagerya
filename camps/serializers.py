from rest_framework import serializers
from .models import Camp, Program, ProgramShift, CampDocument


class CampDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampDocument
        fields = ("id", "name", "file", "uploaded_at")


class ProgramShiftSerializer(serializers.ModelSerializer):
    seats_left = serializers.ReadOnlyField()
    fill_percent = serializers.ReadOnlyField()

    class Meta:
        model = ProgramShift
        fields = ("id", "start_date", "end_date", "seats_total", "seats_taken", "seats_left", "fill_percent")


class ProgramSerializer(serializers.ModelSerializer):
    shifts = ProgramShiftSerializer(many=True, read_only=True)

    class Meta:
        model = Program
        fields = ("id", "title", "description", "duration_days", "price", "max_children", "shifts")


class CampSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True)
    documents = CampDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Camp
        fields = (
            "id", "title", "description", "region", "address",
            "geo_lat", "geo_lng", "age_from", "age_to",
            "food_description", "accommodation_description",
            "is_verified", "programs", "documents"
        )
