#!/usr/bin/env python2
# -*- coding: utf-8 -*- 

import PyV8

with PyV8.JSLocker():
    ctxt = PyV8.JSContext()

def tes():
    with PyV8.JSLocker():
        ctxt.enter()
        func = ctxt.eval("""(function(){function hello(){return "Hello world.";}return hello();})""")
        print(func())
        ctxt.leave()
        PyV8.JSUnlocker()
        PyV8.JSEngine.collect()

if __name__ == '__main__':
    tes()

