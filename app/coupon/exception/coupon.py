from core.exceptions import NotFoundException, BadRequestException


class CouponNotFoundException(NotFoundException):
    error_code = "coupon__not_found"
    message = "coupon not found"


class OutOfStockException(BadRequestException):
    error_code = "coupon__out_of_stock"
    message = "coupon out of stock"


class AlreadyObtainException(BadRequestException):
    error_code = "coupon__already_obtain"
    message = "already obtain"
