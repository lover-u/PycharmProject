

#现在需要一个写文件方法，将selenium的脚本运行结果写入test_result.log文件中

#首先创建写入方法



def write_result(str):
    writeresult=file(r'D:\eclipse4.4.1 script\my_selenium\model\test_result.log','a+')
    str1=writeresult.write(str+'\n')
    writeresult.close()
    return str

#如上str1=writeresult.write(str+'\n') 中写入的文件默认在一行显示，当调用此方法后，每次都会在该文件第一行写入

#在写入参数str后加“\n”则会在每次完成写入后，自动换行到下一行，下次写入时便会在下一行写入
