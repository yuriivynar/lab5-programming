class TimeConverter:
    """
    create class TimeConverter
    """

    def __init__(self, time = ""):
        """
        Created initialisator
        """
        self.time = time

    def output_converted_time(self):
        """
        Converted time    
        """
        if ":" in self.time:
            hours, minutes, seconds = map (int, self.time.split(':'))
            total_seconds = hours * 3600 + minutes * 60 + seconds
            return total_seconds
        total_seconds = int(self.time)
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def __del__(self): 
        """
        Deleted constructot
        """
        print(f"TimeConverter {self.time} is destructed")

def main():
    """
    Created method, which have input parameters
    """
    time_converter1 = TimeConverter("15:47:15")
    seconds = time_converter1.output_converted_time()
    print(f"{time_converter1.time} = {seconds} секунд")

    time_converter2 = TimeConverter("156231")
    seconds = time_converter2.output_converted_time()
    print(f"{time_converter2.time} секунд = {seconds}")

main()
