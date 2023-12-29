from datetime import datetime
nam=int(input('nhập năm:'))
thang=int(input('nhập tháng:'))
ngay=int(input('nhập ngày:'))
doi_ngay=datetime(nam,thang,ngay)
ngay_da_doi=doi_ngay.strftime("%d-%m-%Y")
print('ngày tháng năm vừa nhập:',ngay_da_doi)
