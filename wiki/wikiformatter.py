#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO:

update all source docs

fix summary/description line endings.

add support for module variables.


"""
svnroot = 'http://ibpy.googlecode.com/svn/'


def output_filename(v):
    t = v[9:-3].replace('/__init__', '').split('/')
    if len(t) == 3 and t[-2] == 'ext':
        t = str.join('', [a.title() for a in t[:-1]]) + t[-1]
    else:
        t = str.join('', [a.title() for a in t])
    return 'ApiDoc' + t + '.wiki'


def package_name(v):
    return v[9:-3].replace('/__init__', '').replace('/', '.')


def format_url(v):
    return svnroot + v[3:]


def line_no(elem):
    return int(elem.attrib['lineno'])


def etext(elem, default=''):
    if elem is None:
        return default
    else:
        return elem.text


def write_callables(functions, write, link, indent=0):
    functions.sort(key=line_no)
    offset = '  ' * indent
    moreoffset = offset + '  '

    deffs = '%s=== function %s ===' if not indent else '%smethod *`%s`*'
    for function in functions:
        defstr = etext(function.find('info/def'))
        if defstr:
            defstr = defstr.replace('\n', '')
            write(deffs % (offset, defstr))
            write()

        description = etext(function.find('info/description'))
        if description:
            for line in description.split('\n'):
                line = line.strip()
                if line:
                    write('%s_%s _' % (offset, line))
            write()

        params = function.findall('info/param')
        if params:
            write('%s{{{' % moreoffset)
            for param in params:
                name = param.attrib['name']
                write('%s%s: %s' % (moreoffset, name, param.text or ''))
            ret = etext(function.find('info/return'))
            if ret:
                write('%sreturns: %s' % (moreoffset, ret, ))
            write('%s}}}' % moreoffset)
            write()

        write('%sdefined at [%s line %s]' % (offset, link, function.attrib['lineno']))
        write('%s====== . ======' % offset)
        write()

def write_variables(variables, write, link, indent=0):
    variables.sort(key=line_no)
    offset = '  ' * indent


class PythonDocGenerator:
    def __init__(self, options):
        pass

    def save(self, module, name):
        modulefile = module.attrib['filename']
        filename = output_filename(modulefile)
        link = format_url(modulefile)
        package = package_name(modulefile)

        fh = open(filename, 'w')
        def write(value=''):
            fh.write(value + '\n')

        summary = etext(module.find('info/summary'))
        description = etext(module.find('info/description'))

        if not summary:
            summary = 'Reference documentation for %s' % (package, )
        elif description.startswith(summary):
            description = description[len(summary):]

        write('#summary %s' % summary)
        write('#labels ApiDoc')
        write()

        if description:
            write('= Description =')
            write(description)
            write()

        write_variables(module.findall('variable'), write, link, 0)
        write_callables(module.findall('function'), write, link, 0)

        for cls in sorted(module.findall('class'), key=line_no):
            write('=== class %s ===' % etext(cls.find('info/def')))
            write()

            summary = etext(cls.find('info/summary'))
            description = etext(cls.find('info/description'))

            if summary:
                write('_%s_' % summary)

            if description:
                if description.startswith(summary):
                    description = description[len(summary):]
                write(description)
                write()

            write('class defined at [%s line %s]' % (link, cls.attrib['lineno']))
            write()
            write_callables(cls.findall('method'), write, link, 1)

        write()
        return False
