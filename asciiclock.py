from dataclasses import dataclass
from datetime import datetime
import time


@dataclass
class AsciiClock:
    time: int

    _charset = (
        ("#####", "#   #", "#   #", "#   #", "#####"),
        ("  #  ", "###  ", "  #  ", "  #  ", "#####"),
        ("#####", "    #", "#####", "#    ", "#####"),
        ("#####", "    #", "#####", "    #", "#####"),
        ("#   #", "#   #", "#####", "    #", "    #"),
        ("#####", "#    ", "#####", "    #", "#####"),
        ("#####", "#    ", "#####", "#   #", "#####"),
        ("#####", "    #", "    #", "   # ", "  #  "),
        ("#####", "#   #", "#####", "#   #", "#####"),
        ("#####", "#   #", "#####", "    #", "#####"),
        (" ", "#", " ", "#", " "),
    )

    def __str__(self):
        digits = [int(x) for x in format(self.time % 1000000, "04d")] #added 2 zeros to add seconds
        digits.insert(2, 10)#only idea I have about this line is that it just add ":"
        digits.insert(5, 10)#so I copied it                         
        digits = [self._charset[x] for x in digits]

        return "\n".join(" ".join(l) for l in zip(*digits))


c = AsciiClock(1234)
print(c)

while True:
    time.sleep(1.0)

    t = datetime.now()
    c.time = t.hour * 10000 + t.minute * 100 + t.second # I don't know why we add 10000 100 etc

    print("\033[5A", c, sep="")