#!/usr/bin/env python
# -*- coding: utf-8 -*-

linkbase = 'http://ibpy.googlecode.com/svn/'

def outname(v):
    return v[9:-3].replace('/__init__', '').replace('/', '_') + '.wiki'

def pkgname(v):
    return v[9:-3].replace('/__init__', '').replace('/', '.')

def linkname(v):
    return linkbase + v[3:]

def lineno(elem):
    return int(elem.attrib['lineno'])


caps = [chr(n) for n in range(65,91)]


def wikiescape(text):
    return text # bah
    for word in text.split():
        if len([v for v in [c in caps for c in word] if v]):
	    text = text.replace(word, '!'+word)
    return text


class PythonDocGenerator:
    def __init__(self, options):
        pass

    def save(self, module, name):
        modulefile = module.attrib['filename']
        filename = outname(modulefile)
        link = linkname(modulefile)
        package = pkgname(modulefile)

        fh = open(filename, 'w')
        def write(value=''):
            fh.write(value + '\n')

        summary = module.find('info/summary')
        description = module.find('info/description')

        if summary is not None:
            summary = summary.text
        else:
            summary = 'Reference documentation for %s' % (package, )
        write('#summary %s' % summary)
        write('#labels API-Doc')
        write()

        if description is not None:
            description = description.text
            description = description.replace(summary, '')
            description = description.lstrip()
            write('_%s_' % wikiescape(description))
            write()

        def write_calls(functions, indent=0):
            functions.sort(key=lineno)
            offset = '  ' * indent
            moreoffset = offset + '  '


            for function in functions:
                fs = '%s==== %s ====' if not indent else '%s`%s`'
                defstr = function.find('info/def')
                if defstr is not None:
                    defstr = defstr.text.replace('\n', '')
                write(fs % (offset, defstr))
                write()

                description = function.find('info/description')
                if description is not None and description.text:
                    for line in description.text.split('\n'):
                        line = line.strip()
                        write('%s_%s_' % (offset, wikiescape(line)))
                else:
                    pass
                write()

                params = function.findall('info/param')
                if params:
                    write('%s{{{' % moreoffset)
                    for param in params:
                        name = param.attrib['name'].replace('*', '')
                        write('%s%s : %s' % (moreoffset, name, param.text or ''))
                    ret = function.find('info/return')
                    if ret is not None:
                        write('%sreturns: %s' % (moreoffset, ret.text, ))
                    write('%s}}}' % moreoffset)
                    write()
                write('%sdefined at [%s line %s]' % (offset, link, function.attrib['lineno']))
                write('%s====== . ======' % offset)
                write()

        write_calls(module.findall('function'))

        classes = module.findall('class')
        classes.sort(key=lineno)

        for cls in classes:
            name = cls.attrib['name']
            name = cls.find('info/def').text
            write('==== %s ====' % name)
            write()
            description = cls.find('info/description')
            if description is not None and description.text:
                write('_%s_' % wikiescape(description.text))
            write('defined at [%s line %s]' % (link, cls.attrib['lineno']))
            write()
            write_calls(cls.findall('method'), 1)


        write('')
        write('')
        return filename + ' ' + package

    def done(self):
        print 'done'
