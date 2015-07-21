import time
import base64
import hashlib
import hmac
from mixcoatl.settings.load_settings import settings


def get_sig(http_method, path, endpoint=None):
    """Return a signature valid for use in making DCM API calls

    :param http_method: The `http_method` used to make the API call
    :param path: The `path` used in the API call
    """

    if endpoint:
        access_key = endpoint.access_key
        secret_key = endpoint.secret_key
        basepath = endpoint.basepath
    else:
        access_key = settings.access_key
        secret_key = settings.secret_key
        basepath = settings.basepath

    timestamp = int(round(time.time() * 1000))
    signpath = basepath + '/' + path
    parts = []
    parts.append(access_key)
    parts.append(http_method)
    parts.append(signpath)
    parts.append(timestamp)
    parts.append(settings.user_agent)
    # pylint: disable-msg=E1101
    dm = hashlib.sha256
    to_sign = ':'.join([str(x) for x in parts])
    d = hmac.new(secret_key, msg=to_sign, digestmod=dm).digest()
    b64auth = base64.b64encode(d).decode()
    return {'timestamp': timestamp,
            'signature': b64auth,
            'access_key': access_key,
            'ua': settings.user_agent}
