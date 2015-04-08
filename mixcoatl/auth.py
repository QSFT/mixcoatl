import time
import base64
import hashlib
import hmac


def get_sig(http_method, config, path):
    """Return a signature valid for use in making DCM API calls

    :param http_method: The `http_method` used to make the API call
    :param path: The `path` used in the API call
    """
    timestamp = int(round(time.time() * 1000))
    signpath = config.basepath + '/' + path
    parts = []
    parts.append(config.access_key)
    parts.append(http_method)
    parts.append(signpath)
    parts.append(timestamp)
    parts.append(config.user_agent)
    # pylint: disable-msg=E1101
    dm = hashlib.sha256
    to_sign = ':'.join([str(x) for x in parts])
    d = hmac.new(config.secret_key, msg=to_sign, digestmod=dm).digest()
    b64auth = base64.b64encode(d).decode()
    return {'timestamp': timestamp,
            'signature': b64auth,
            'access_key': config.access_key,
            'ua': config.user_agent}
