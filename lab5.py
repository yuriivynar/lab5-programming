class TimeConverter:

    def __init__(self, time = ""):
        self.time = time
    
    def outputConvertedTime(self):
      if ":" in self.time:
         hours, minutes, seconds = map(int, self.time.split(':'))
         total_seconds = hours * 3600 + minutes * 60 + seconds
         return total_seconds
      else:
         total_seconds = int(self.time)
         hours, remainder = divmod(total_seconds, 3600)
         minutes, seconds = divmod(remainder, 60)
         return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
    def __del__(self): #destructor
        print(f"TimeConverter {self.time} is destructed")

def main():
    time_converter = TimeConverter("15:47:15")
    seconds = time_converter.outputConvertedTime()
    print(f"{time_converter.time} = {seconds} секунд")

    time_converter = TimeConverter("156231")
    seconds = time_converter.outputConvertedTime()
    print(f"{time_converter.time} секунд = {seconds}")
main()