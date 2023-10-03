def month_amount(month, year):
    match month:
        case "Jan" | "Mar" | "May" | "Jul" | "Aug" | "Oct" | "Dec":
            print("31")
        case "Apr" | "Jun" | "Sep" | "Nov":
            print("30")
        case "Feb":
            if year % 4 == 0:
                print("29")
            else:
                print("28")


print("Month is the first three letter eg: Jan")
month = input("Please input a month: ")
year = int(input("Please input a year: "))

month_amount(month, year)
