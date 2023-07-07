import us_states
import os
for i in os.listdir("us_states"):
    print(i.removesuffix(".py"))