# xadmin
import xadmin
from xadmin import views
from .models import User


class GlobalSettings(object):
    site_title = '随身猿'
    site_footer = '随身猿公司'
    # 菜单折叠
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView,GlobalSettings)

# 默认xadmin 已经把权限6个表自动注册，
# 可以不用再注册 user
# 在注册就会报错
# xadmin.site.register(User)
