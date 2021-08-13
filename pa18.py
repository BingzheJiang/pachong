#初次使用selenium
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
#创建浏览器对象
web=Chrome()
#打开一个网址
web.get("http://www.lagou.com")
print(web.title)
#找到某个元素，点击它
el=web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click()#点击事件
# time.sleep(1)
el2=web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER)
li_list=web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
time.sleep(1)
for li in li_list:
    job_name=li.find_element_by_tag_name("h3").text
    job_price=li.find_element_by_xpath("./div/div/div[2]/div/span").text
    job_company=li.find_element_by_xpath('./div[1]/div[2]/div[1]/a').text
    print(job_name,job_price,job_company)
