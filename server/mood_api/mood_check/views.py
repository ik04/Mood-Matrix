from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from textblob import TextBlob


# todo: find a way to prevent burpsuite attacks
# todo: add better validation


@api_view(["GET"])
def index(request):
    if request.method == "GET":
        return Response({"message": "Welcome to Mood Api"}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"error": "Method not allowed"},
        )


# todo: improve functionality
@api_view(["POST"])
def analyse(request):
    if request.method == "POST":
        diary_content = str(request.data.get("content"))
        text_blob = TextBlob(diary_content)
        sentiment_polarity = text_blob.sentiment.polarity
        return Response({"polarity": sentiment_polarity}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"error": "Method not allowed"},
        )
