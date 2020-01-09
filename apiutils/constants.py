# encoding: utf-8

from apiview.code import Code


DELETE_CODE = Code((
    ('NORMAL',  False, '正常'),
    ('DELETED', True,  '已经删除'),
))

CHANGE_LOG_STATUS_CODE = Code((
    ('PROCESSING',  0,  '处理中'),
    ('SUCCESS',     10, '成功'),
    ('FAIL',        11, '失败'),
))
