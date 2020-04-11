# -*- coding: utf-8 -*-

import os
from datetime import datetime
from xlstpl.writer import BookWriter


def write_test():
    pth = os.path.dirname(__file__)
    fname = os.path.join(pth, 'example.xls')
    writer = BookWriter(fname)
    writer.jinja_env.globals.update(dir=dir, getattr=getattr)

    now = datetime.now()

    person_info = {'address': u'福建行中书省福宁州傲龙山庄', 'name': u'龙傲天', 'fm': 178, 'date': now}
    person_info2 = {'address': u'Somewhere over the rainbow', 'name': u'Hello Wizard', 'fm': 156, 'date': now}
    rows = [['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
            ]
    person_info['rows'] = rows
    person_info2['rows'] = rows
    payload0 = {'tpl_name': 'cn', 'sheet_name': u'表',  'ctx': person_info}
    payload1 = {'tpl_name': 'en', 'sheet_name': u'form', 'ctx': person_info2}
    payload2 = {'tpl_idx': 2, 'ctx': person_info2}
    payloads = [payload0, payload1, payload2]
    writer.render_book2(payloads=payloads)
    fname = os.path.join(pth, 'result10.xls')
    writer.save(fname)
    payloads = [payload2, payload1, payload0]
    writer.render_book2(payloads=payloads)
    writer.render_sheet(person_info2, 'form2', 1)
    fname = os.path.join(pth, 'result11.xls')
    writer.save(fname)


if __name__ == "__main__":
    write_test()
