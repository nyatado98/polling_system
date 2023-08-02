from numbers import Number

from django import template

from bitpoll.base.models import BitpollUser
from bitpoll.poll.models import Poll
from bitpoll.poll.util import PartialDateTime

register = template.Library()


@register.filter
def group_title(value):
    if isinstance(value, PartialDateTime):
        return value.format()
    else:
        return value


@register.filter
def percentage(value: Number) -> str:
    if value is not None:
        return '{0:.1f}%'.format(value * 100)
    return 'n/a'


@register.filter
def or_none(value: object) -> object:
    if value:
        return value
    return 'n/a'


@register.filter
def has_voted(poll: Poll, user: BitpollUser) -> bool:
    return poll.has_voted(user)


@register.filter
def get_own_vote_pk(poll: Poll, user: BitpollUser) -> int:
    return poll.get_own_vote(user).pk


@register.filter
def get_tz_name_no_date_utc(poll: Poll, user: BitpollUser) -> str:
    return poll.get_tz_name_no_date_utc(user)


@register.simple_tag
def is_initial_choice(initial: list, date, time):
    if (date, time) in initial:
        return True

    return False
