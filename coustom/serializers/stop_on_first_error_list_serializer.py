from rest_framework import serializers

class StopOnFirstErrorListSerializer(serializers.ListSerializer):
    def to_internal_value(self, data):
        if isinstance(data, list):
            ret = []
            errors = []
            for item in data:
                try:
                    validated = self.child.run_validation(item)
                    ret.append(validated)
                except serializers.ValidationError as exc:
                    errors.append(exc.detail)
                    break

            if errors:
                raise serializers.ValidationError(errors)
            return ret
        raise serializers.ValidationError(
            {self.field_name: 'Expected a list of items but got type "{}".'.format(
                type(data).__name__)
             }
        )