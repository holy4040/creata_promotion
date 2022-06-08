from rest_framework.exceptions import APIException

class PromotionCodeNotFound(APIException):
    status_code = 404
    default_detail = "The promotion code doesn't exist"