# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client.command import RESTCommand

from .exceptions import SetupdError
from .exceptions import SetupdServiceUnavailable
from .exceptions import InvalidSetupdError


class SetupdCommand(RESTCommand):

    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise SetupdServiceUnavailable(response)

        try:
            raise SetupdError(response)
        except InvalidSetupdError:
            RESTCommand.raise_from_response(response)