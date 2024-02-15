def timeInWords(h, m):
    # Write your code here
    hours = ['','one', 'two', 'three', 'four', 'five', 'six',
              'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    min = ["",'one', 'two', 'three', 'four', 'five', 'six',
              'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
              "thirteen",'fourteen', 'quarter', 'sixteen', 'seventeen',
              "eighteen", "nineteen", "twenty", "twenty one", "twenty two",
              "twenty three", "twenty four", "twenty five", "twenty six",
              "twenty seven", "twenty eight", "twenty nine"]
    
    hrs=hours[h]
    if m==00:
        return f"{hrs} o' clock"
    else:
        if m==1:
            return f"one minute past {hrs}"
        elif m<30 and m>1:
            minn =min[m]
            return f"{minn} minutes past {hrs}"
        elif m==30:
            return F"half past {hrs}"
        else:
            hrs=hours[h+1]
            minutes=min[30-(m-30)]
            return f"{minutes} minutes to {hrs}"

    
print(timeInWords(5,38))