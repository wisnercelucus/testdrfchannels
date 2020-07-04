from rest_framework import serializers

from .models import *

class PostModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = ['id', 'content', 'title']