__author__ = 'asus'

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice


fp=open("f1040nr.pdf","rb")

parser=PDFParser(fp)

#pdf文档的对象
doc=PDFDocument()

#连接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

#初始化文档
doc.initialize("")

#创建pdf的资源管理器
resource=PDFResourceManager()

#参数分析器
laparam=LAParams()

#创建一个聚合器
device=PDFPageAggregator()

#页面解释器
interpreter=PDFPageInterpreter(resource,device)

for page in doc.get_pages():
    #使用页面解释器来读取
    interpreter.process_page(page)
    #使用聚合器来获得内容
    layout=device.get_result()

    for out in layout:
        if hasattr(out,"get_text"):
            print(out.get_text())



