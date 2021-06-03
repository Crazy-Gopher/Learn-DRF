## Serilizer:
  Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON,
  XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the 
  incoming data.
  
  The serializers in REST framework work very similarly to Django's Form and ModelForm classes. We provide a Serializer class which gives you a powerful, 
  generic way to control the output of your responses, as well as a ModelSerializer class which provides a useful shortcut for creating serializers that deal
  with model instances and querysets.
  
  
## Validation
1. Field-level validation
You can specify custom field-level validation by adding .validate_<field_name> methods to your Serializer subclass. These are similar to the .clean_<field_name> methods on
Django forms.

return: Your validate_<field_name> methods should return the validated value or raise a serializers.ValidationError

Example:
from rest_framework import serializers
class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_title(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value
      
      
Note: If your <field_name> is declared on your serializer with the parameter required=False then this validation step will not take place if the field is not included.
  
  
2. Object-level validation
To do any other validation that requires access to multiple fields, add a method called .validate() to your Serializer subclass. This method takes a single argument,
which is a dictionary of field values. It should raise a serializers.ValidationError if necessary, or just return the validated values. 

from rest_framework import serializers
class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data



3. Validators
Individual fields on a serializer can include validators, by declaring them on the field instance, for example:

  
def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

class GameRecord(serializers.Serializer):
    score = IntegerField(validators=[multiple_of_ten])



## Partial updates
By default, serializers must be passed values for all required fields or they will raise validation errors. You can use the partial argument in 
order to allow partial updates.

# Update `comment` with partial data
serializer = CommentSerializer(comment, data={'content': 'foo bar'}, partial=True)


## Dealing with nested objects
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class CommentSerializer(serializers.Serializer):
    user = UserSerializer()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    
Note: If a nested representation may optionally accept the None value you should pass the required=False flag to the nested serializer.

class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)  # May be an anonymous user.
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

Note: Similarly if a nested representation should be a list of items, you should pass the many=True flag to the nested serializer.

class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    edits = EditItemSerializer(many=True)  # A nested list of 'edit' items.
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    
## Writing .create() methods for nested representations
If you're supporting writable nested representations you'll need to write .create() or .update() methods that handle saving multiple objects.    
    
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


## ModelSerializer
The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
        fields = '__all__' # all fields
        exclude = ['users']

