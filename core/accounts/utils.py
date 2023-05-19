from kavenegar import *


def send_otp_code(phone_number, code):
    """
    This function ....
    Args:
        phone_number(int)
        code:(int)
    Return:
        ...
    Rais:
        ...
    """
    try:
        api = KavenegarAPI('54325078707872505A6A654168745145656B39335544484A557')
        params = {'receptor': phone_number, 'message': f'{code} کد تایید شما '}
        response = api.sms_send(params)
        print(response.messageid)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
