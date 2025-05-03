
from rest_framework import serializers
from .models import Review

BAD_WORDS = ['fuck', 'motherfucker', 'fuckyou']  # Можно потом дополнить

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'dish', 'text', 'created_at']
        read_only_fields = ['user', 'created_at']

    def validate_text(self, value):
        for bad_word in BAD_WORDS:
            if bad_word in value.lower():
                raise serializers.ValidationError("Inappropriate language is not allowed.")
        return value
