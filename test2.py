# all the months and their values
January = 110
February = 45
March = 77
April = 90
May = 4
June = 15
July = 32
August = 45
September = 76
October = 22
November = 39
December = 12
#you pick after which month you want the values or the total
total_stamps = {January + February + March + April + May + June + July + August + September + October + November+ December}
stamps_afterfebruary = January + February
stamps_aftermarch = January + February + March
stamps_afterapril =January + February + March + April 
stamps_aftermay =January + February + March + April + May 
stamps_afterjune =January + February + March + April + May + June
stamps_afterjuly =January + February + March + April + May + June + July 
# say you wanted stamp count after july
print(stamps_afterjuly)
#rest of months
stamps_afteraugust =January + February + March + April + May + June + July + August 
stamps_afterseptember =January + February + March + April + May + June + July + August +September
stamps_afteroctober = January + February + March + April + May + June + July + August + September + October
stamps_afternovember = January + February + March + April + May + June + July + August + September + October + November 
stamps_afterdecember = January + February + March + April + May + June + July + August + September +October + November + December
# say you want total months
print(total_stamps)
