# Serializers
- Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

- The serializers in REST framework work very similarly to Django's Form and ModelForm classes. We provide a Serializer class which gives you a powerful, generic way to control the output of your responses, as well as a ModelSerializer class which provides a useful shortcut for creating serializers that deal with model instances and querysets.

achraf 1234


### This ModelViewSet provides these endpoints automatically:

- list() – GET /books_all/

- retrieve() – GET /books_all/<id>/

- create() – POST /books_all/

- update() – PUT /books_all/<id>/

- partial_update() – PATCH /books_all/<id>/

- destroy() – DELETE /books_all/<id>/