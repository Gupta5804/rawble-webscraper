from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pandas import ExcelWriter

writer = pd.ExcelWriter('pandas_simple(1).xlsx', engine='xlsxwriter')

xl = pd.ExcelFile("NuPlanet_Mastersheet (2).xlsx")
sheet2 = xl.parse("Sheet2")
df_alibaba = pd.DataFrame()
pd.set_option('display.max_colwidth', -1)

alibaba = "https://www.alibaba.com/?spm=a2700.7724838.scGlobalHomeHeader.6.4b477ae2Ow3j6e"
for i in range(10):
    #print(sheet2['Item Description'][i])
    driver = webdriver.Chrome()
    product = str(sheet2['Item Description'][i])
    driver.get(alibaba)

    search = driver.find_element_by_name('SearchText')
    search.send_keys(product)
    search.send_keys(Keys.RETURN)
    try:
        first_result = driver.find_element_by_css_selector(
            'body > div.l-page > div.l-page-main > div.l-main-content > div.l-grid.l-grid-sub > div.l-col-main > div.l-grid.l-grid-extra > div.l-col-main > div > div.l-theme-card-box.ns-theme-offer-attr.uf-theme-card-border.uf-theme-card-margin-bottom')
        first_result = first_result.find_elements_by_tag_name('a')
        if(first_result[0]):
            first_result[0].click()
            driver.switch_to.window(driver.window_handles[-1])
            driver.implicitly_wait(5)

            detail_box = driver.find_element_by_css_selector(
                '#J-ls-grid-desc > div.tab-body > div.tab-body-pane.ls-icon.ls-product.show > div > div > div.scc-wrapper.detail-module.module-productPackagingAndQuickDetail > div > div.do-content > div > div.do-entry.do-entry-separate > div.do-entry-list')
            title = detail_box.find_elements_by_tag_name('dt')
            title_value = detail_box.find_elements_by_tag_name('dd')
            cas_no=einecs_no=type=appearance=other_name=""
            for k in range(len(title)):
                if(title[k].text == "CAS No.:"):
                    cas_no = title_value[k].text
                elif(title[k].text == "EINECS No.:"):
                    einecs_no = title_value[k].text
                elif(title[k].text == "Type:"):
                    type = title_value[k].text
                elif(title[k].text == "Appearance:"):
                    appearance = title_value[k].text
                elif(title[k].text == "Other Names:"):
                    other_name = title_value[k].text
            print(cas_no,einecs_no,type,appearance,other_name)
            df_alibaba = df_alibaba.append({
                'Product Name':product,
                'Search Result':first_result[0].text,
                'CAS No.':cas_no,
                'EINECS No.':einecs_no,
                'Type':type,
                'Appearance':appearance,
                'Other Names':other_name,

            },ignore_index=True)
            driver.quit()
            #print(df_alibaba.head())
    except:
        driver.quit()
        pass

df_alibaba.to_excel(writer,sheet_name="alibaba")
writer.save()