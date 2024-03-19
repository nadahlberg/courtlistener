from rest_framework import serializers
from rest_framework.serializers import ValidationError


class CitationRequestSerializer(serializers.Serializer):
    text_citation = serializers.CharField(required=False)
    reporter = serializers.CharField(max_length=100, required=False)
    volume = serializers.IntegerField(required=False)
    citation_page = serializers.CharField(required=False)

    def validate(self, data):
        reporter = data.get("reporter")
        text_citation = data.get("text_citation")
        volume = data.get("volume")
        citation_or_reporter_provided = any([reporter, text_citation])

        # make sure users provide either a reporter or a text citation.
        if not all([len(data), citation_or_reporter_provided]):
            raise ValidationError(
                {
                    "non_field_errors": [
                        "You must either provide a 'text citation' or 'reporter'."
                    ]
                }
            )

        # Enforces mutually exclusive fields: reporter and text_citation.
        if all([reporter, text_citation]):
            raise ValidationError(
                {
                    "non_field_errors": [
                        "Invalid request. Provide either a 'text citation' or 'reporter', not both."
                    ]
                }
            )

        # Make sure users provide a volume when they use the reporter
        # field to lookup citations.
        if reporter and not volume:
            raise ValidationError({"volume": ["This field is required."]})

        return data
