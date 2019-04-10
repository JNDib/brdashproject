import re
from django import template
from datetime import timedelta
from django.template import defaultfilters
from django.utils.translation import (
    gettext as _, ngettext, npgettext_lazy, pgettext,
)
from django.utils.translation import ngettext_lazy, gettext
from django.utils.html import avoid_wrapping

register = template.Library()

TIME_STRINGS = {
    'year': ngettext_lazy('%d year', '%d years'),
    'month': ngettext_lazy('%d month', '%d months'),
    'week': ngettext_lazy('%d week', '%d weeks'),
    'day': ngettext_lazy('%d day', '%d days'),
    'hour': ngettext_lazy('%d hour', '%d hours'),
    'minute': ngettext_lazy('%d minute', '%d minutes'),
}

TIMESINCE_CHUNKS = (
    (60 * 60 * 24 * 365, 'year'),
    (60 * 60 * 24 * 30, 'month'),
    (60 * 60 * 24 * 7, 'week'),
    (60 * 60 * 24, 'day'),
    (60 * 60, 'hour'),
    (60, 'minute'),
)


def timesince(delta, time_strings=None):
    """
    Take two datetime objects and return the time between d and now as a nicely
    formatted string, e.g. "10 minutes". If d occurs after now, return
    "0 minutes".

    Units used are years, months, weeks, days, hours, and minutes.
    Seconds and microseconds are ignored.  Up to two adjacent units will be
    displayed.  For example, "2 weeks, 3 days" and "1 year, 3 months" are
    possible outputs, but "2 weeks, 3 hours" and "1 year, 5 days" are not.

    `time_strings` is an optional dict of strings to replace the default
    TIME_STRINGS dict.

    Adapted from
    http://web.archive.org/web/20060617175230/http://blog.natbat.co.uk/archive/2003/Jun/14/time_since
    """
    if time_strings is None:
        time_strings = TIME_STRINGS

    # ignore microseconds
    since = delta.days * 24 * 60 * 60 + delta.seconds
    if since <= 0:
        # d is in the future compared to now, stop processing.
        return avoid_wrapping(gettext('0 minutes'))
    for i, (seconds, name) in enumerate(TIMESINCE_CHUNKS):
        count = since // seconds
        if count != 0:
            break
    result = avoid_wrapping(time_strings[name] % count)
    if i + 1 < len(TIMESINCE_CHUNKS):
        # Now get the second item
        seconds2, name2 = TIMESINCE_CHUNKS[i + 1]
        count2 = (since - (seconds * count)) // seconds2
        if count2 != 0:
            result += gettext(', ') + avoid_wrapping(time_strings[name2] % count2)
    return result

@register.filter
def naturalduration(delta):	
	"""
    For date and time values show how many seconds, minutes, or hours ago
    compared to current timestamp return representing string.
    """
	if not isinstance(delta, timedelta):  # if not timedelta filter is invalid
		return delta

	if delta.days != 0:
		# Translators: delta will contain a string like '2 months' or '1 month, 2 weeks'
		return _('%(delta)s') % {'delta': timesince(delta, time_strings={
			# Translators: 'naturaltime-past' strings will be included in
			# '%(delta)s ago'
			'year': npgettext_lazy('naturaltime-past', '%d year', '%d years'),
			'month': npgettext_lazy('naturaltime-past', '%d month', '%d months'),
			'week': npgettext_lazy('naturaltime-past', '%d week', '%d weeks'),
			'day': npgettext_lazy('naturaltime-past', '%d day', '%d days'),
			'hour': npgettext_lazy('naturaltime-past', '%d hour', '%d hours'),
			'minute': npgettext_lazy('naturaltime-past', '%d minute', '%d minutes')
		})}
	elif delta.seconds == 0:
		return _('0')
	elif delta.seconds < 60:
		return ngettext(
			# Translators: please keep a non-breaking space (U+00A0)
			# between count and time unit.
			'a second', '%(count)s seconds', delta.seconds
		) % {'count': delta.seconds}
	elif delta.seconds // 60 < 60:
		count = delta.seconds // 60
		return ngettext(
			# Translators: please keep a non-breaking space (U+00A0)
			# between count and time unit.
			'a minute', '%(count)s minutes', count
		) % {'count': count}
	else:
		count = delta.seconds // 60 // 60
		return ngettext(
			# Translators: please keep a non-breaking space (U+00A0)
			# between count and time unit.
			'an hour', '%(count)s hours', count
		) % {'count': count}


@register.filter
def dashify(value):
	""" return an 11 digit part number with dashes.
	e.g. 00000000000 becomes 00-0000-0000-0; if value is not 11 characters,
	return the value """
	
	prodstring = str(value)
	
	if not len(str(value)) == 11:
		return value
		
	return "%s-%s-%s-%s" % (prodstring[0:2], prodstring[2:6], prodstring[6:10], prodstring[10])
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	