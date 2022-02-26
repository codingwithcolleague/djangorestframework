from .models import Singer,Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields  = ['id' , 'title' , 'singer' , 'duration']

class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True,read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    song = serializers.HyperlinkedIdentityField(many=True,read_only=True,view_name='song-detail')

    class Meta:
        model = Singer
        fields  = ['id' , 'name' , 'gender','song']


"""
2nd Way
"""

class SongHyperlinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields  = ['id' ,'url' , 'title' , 'singer' , 'duration']


"""
3rd Way
"""

class SingerSSSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Singer
        fields  = ['id' , 'name' , 'gender','song']
