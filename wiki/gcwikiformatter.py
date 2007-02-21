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
    offset = '  ' * indent
    moreoffset = offset + '  '

    deffs = '%s=== %s (function) ===' if not indent else '%smethod *`%s`*'
    for function in sorted(functions, key=line_no):
        defstr = etext(function.find('info/def'))
        if defstr:
            defstr = defstr.replace('\n', ' ')
            write(deffs % (offset, defstr))
            write()

        description = etext(function.find('info/description'))
        if description:
            write('%s_%s _' % (offset, description.replace('\n', ' ')))
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
    varfs = '%s=== %s (variable) ===' if not indent else '%smember *`%s`*'

    for var in sorted(variables, key=line_no):
        vdef = etext(var.find('info/def'))
        name = etext(var.find('info/name'))
        summary = etext(var.find('info/summary'))
        descrip = etext(var.find('info/description'))

        write(varfs % (offset, vdef))
        write()

        if descrip:
            write('%s _%s_' % (offset, descrip.replace('\n', ' ')))
        elif summary:
            write('%s _%s_' % (offset, summary))
        write()
        write('%sdefined at [%s line %s]' % (offset, link, var.attrib['lineno']))
        write('%s====== . ======' % offset)
        write()


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
            write('=== %s (class) ===' % etext(cls.find('info/def')))
            write()

            summary = etext(cls.find('info/summary'))
            description = etext(cls.find('info/description'))

            if not description:
                write('_%s_' % summary)
            else:
                write(description.replace('\n', ' '))
                write()

            write('class defined at [%s line %s]' % (link, cls.attrib['lineno']))
            write()
            write_variables(cls.findall('variable'), write, link, 1)
            write_callables(cls.findall('method'), write, link, 1)

        write()
        return False
