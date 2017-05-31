
import output

from .models import User


def check_user(user_id):
    """ 校验用户是否存在 """
    user = User.query.filter_by(u_id=user_id).first()
    if not user:
        return output()
    return output(user)