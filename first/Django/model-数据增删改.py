#!/user/bin/python
#_*_coding:utf-8 _*_



choices
GENDER_CHOICE = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
gender = models.CharField(max_length=2,choices = GENDER_CHOICE)     # 这个字段相当于 不用建第三张表了   直接从内存中读取对应的字段信息