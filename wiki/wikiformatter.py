#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PythonDocGenerator:
    def __init__(self, options):
        self.encoding = options.get("encoding")
        self.outfile = options.get("outfile")

    def save(self, module, name):
        filename = self.outfile #module.attrib['filename']
        fh = open(filename, 'w')
        def write(v=''):
            fh.write(v)
            fh.write('\n')

        def lineno(o):
            return int(o.attrib['lineno'])


        link = 'http://ibpy.googlecode.com/svn/trunk/' + module.attrib['filename']

        summary = module.find('info/summary')
        description = module.find('info/description')

        if summary is not None:
            summary = summary.text
            write('#summary: %s' % summary)
            write()
        else:
            summary = ''
        if description is not None:
            description = description.text
            description = description.replace(summary, '')
            description = description.lstrip()
            write('_%s_' % description)
            write()


        def write_calls(functions, indent=0):
            functions.sort(key=lineno)
            offset = '  ' * indent
            moreoffset = offset + '  '


            for function in functions:
                fs = '%s==== %s ====' if not indent else '%s`%s`'
                write(fs % (offset, function.find('info/def').text))
                write()

                description = function.find('info/description')
                if description is not None and description.text:
                    for line in description.text.split('\n'):
                        line = line.strip()
                        write('%s_%s_' % (offset, line))
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
                write('_%s_' % description.text)
            write('defined at [%s line %s]' % (link, cls.attrib['lineno']))
            write()
            write_calls(cls.findall('method'), 1)


        write('')
        write('')
        return filename

    def done(self):
        print 'done'
