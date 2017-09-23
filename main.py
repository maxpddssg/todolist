#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.ioloop
import sys
import logging; logging.basicConfig(level=logging.INFO)
from application import application
import tornado.options
from tornado.options import options, define

define('port', '8080')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    logging.info('Server started at port: {}...'.format(options.port))
    tornado.ioloop.IOLoop.instance().start()