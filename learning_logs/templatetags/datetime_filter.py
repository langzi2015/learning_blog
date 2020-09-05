import pytz

from django import template
from datetime import datetime, timedelta

register = template.Library()


@register.filter()
def time_filter(data):
    utc_tz = pytz.timezone('UTC')
    now = datetime.now(tz=utc_tz)
    timestamp = (now - data).total_seconds()
    if timestamp < 60:
        return '刚刚'

    elif timestamp < 60 * 60:
        m = int(timestamp // 60)
        return '{}分钟前'.format(m)

    elif timestamp < 60 * 60 * 24:
        h = int(timestamp // (60 * 60))
        return '{}小时前'.format(h)

    else:
        data += timedelta(hours=8)
        return data.strftime("%Y{}%m{}%d{} %H:%M").format('年', '月', '日')
