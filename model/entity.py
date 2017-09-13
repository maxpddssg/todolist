#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Entity:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get(name):
        return Entity(name)