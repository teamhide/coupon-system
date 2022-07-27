from core.exceptions import NotFoundException


class UserNotFoundException(NotFoundException):
    error_code = "user__not_found"
    message = "user not found"
