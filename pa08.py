from lxml import etree
html="""
<book>
 <id>1</id>
 <name>野花遍地⾹</name>
 <price>1.23</price>
 <nick>臭⾖腐</nick>
 <author>
 <nick id="10086">周⼤强</nick>
 <nick id="10010">周芷若</nick>
 <nick class="joy">周杰伦</nick>
 <nick class="jolin">蔡依林</nick><div>
 <nick>惹了</nick>
 </div>
 </author>
 <partner>
 <nick id="ppc">胖胖陈</nick>
 <nick id="ppbc">胖胖不陈</nick>
 </partner>
</book>
"""
et=etree.XML(html)
# result=et.xpath("/book")
# result=et.xpath("/book//nick/text()")
# print(result)
result2=et.xpath("/book/*/nick/text()")
print(result2)

