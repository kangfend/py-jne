from .constants import JNE_HTTP_STATUS_CODE


class JneError(Exception):
    def __init__(self, message, error_code=None):
        self.error_code = error_code

        if error_code in JNE_HTTP_STATUS_CODE:
            message = 'JNE API returned %s (%s), %s' % (
                error_code,
                JNE_HTTP_STATUS_CODE.get(error_code),
                message
            )
        super(JneError, self).__init__(message)


class JneAPIError(JneError):
    pass
