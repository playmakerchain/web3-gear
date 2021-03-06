# Copyright (c) 2018 The VeChainThor developers
# Copyright (c) 2019 The PlayMaker developers

# Distributed under the GNU Lesser General Public License v3.0 software license, see the accompanying
# file LICENSE or <https://www.gnu.org/licenses/lgpl-3.0.html>

from threading import Thread


class ThreadWithReturn(Thread):
    '''
    The function is executed in a multi-threaded manner, and the result of the function execution can 
    be obtained by the get method after the thread ends (if the function has a return value)
    '''

    def __init__(self, target=None, args=None, kwargs=None):
        super(ThreadWithReturn, self).__init__(target=target, args=args, kwargs=kwargs)
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self._return = self.target(*self.args, **self.kwargs)

    def get(self, timeout=None):
        self.join(timeout)
        try:
            return self._return
        except AttributeError:
            raise RuntimeError("Something went wrong.  No `_return` property was set")


def spawn(target, *args, **kwargs):
    thread = ThreadWithReturn(
        target=target,
        args=args,
        kwargs=kwargs,
    )
    thread.daemon = True
    thread.start()
    return thread
