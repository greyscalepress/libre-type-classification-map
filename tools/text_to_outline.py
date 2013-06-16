import scribus

if scribus.haveDoc():
    page = 1
    pagenum = scribus.pageCount()
    while (page <= pagenum):
        scribus.gotoPage(page)
        d = scribus.getPageItems()
        for item in d:
            if (item[1] == 4):
                    scribus.traceText(item[0])
        page += 1
