#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Float,
    TextAscii,
    Tuple,
)
from cmk.gui.plugins.wato import (
    RulespecGroupCheckParametersApplications,
    register_check_parameters,
)

register_check_parameters(
    RulespecGroupCheckParametersApplications,
    "db2_counters",
    _("DB2 Counters"),
    Dictionary(
        help=_("This rule allows you to configure limits for the deadlocks and lockwaits "
               "counters of a DB2."),
        elements=[
            (
                "deadlocks",
                Tuple(
                    title=_("Deadlocks"),
                    elements=[
                        Float(title=_("Warning at"), unit=_("deadlocks/sec")),
                        Float(title=_("Critical at"), unit=_("deadlocks/sec")),
                    ],
                ),
            ),
            (
                "lockwaits",
                Tuple(
                    title=_("Lockwaits"),
                    elements=[
                        Float(title=_("Warning at"), unit=_("lockwaits/sec")),
                        Float(title=_("Critical at"), unit=_("lockwaits/sec")),
                    ],
                ),
            ),
        ]),
    TextAscii(
        title=_("Instance"), help=_("DB2 instance followed by database name, e.g db2taddm:CMDBS1")),
    "dict",
)
