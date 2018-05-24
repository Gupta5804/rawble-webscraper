from selenium import webdriver
from selenium.webdriver.common.keys import Keys
alibaba = "https://www.alibaba.com/?spm=a2700.7724838.scGlobalHomeHeader.6.4b477ae2Ow3j6e"
driver = webdriver.Chrome()
driver.get(alibaba)
search = driver.find_element_by_name('SearchText')
search.send_keys("Sorbitol")
search.send_keys(Keys.RETURN)
first_result = driver.find_element_by_css_selector('body > div.l-page > div.l-page-main > div.l-main-content > div.l-grid.l-grid-sub > div.l-col-main > div.l-grid.l-grid-extra > div.l-col-main > div > div.l-theme-card-box.ns-theme-offer-attr.uf-theme-card-border.uf-theme-card-margin-bottom')
first_result = first_result.find_elements_by_tag_name('a')
first_result[0].click()
driver.switch_to.window(driver.window_handles[-1])
detail_box = driver.find_element_by_css_selector('#J-ls-grid-desc > div.tab-body > div.tab-body-pane.ls-icon.ls-product.show > div > div > div.scc-wrapper.detail-module.module-productPackagingAndQuickDetail > div > div.do-content > div > div.do-entry.do-entry-separate > div.do-entry-list')
title = detail_box.find_elements_by_tag_name('dt')
title_value = detail_box.find_elements_by_tag_name('dd')


print(title[0].text , " ," ,title_value[0].text)