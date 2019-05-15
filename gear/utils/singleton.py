# Copyright (c) 2018 The VeChainThor developers
# Copyright (c) 2019 The PlayMaker developers

# Distributed under the GNU Lesser General Public License v3.0 software license, see the accompanying
# file LICENSE or <https://www.gnu.org/licenses/lgpl-3.0.html>

class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance
