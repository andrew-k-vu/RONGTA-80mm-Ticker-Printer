from escpos.printer import Win32Raw
import datetime

printer = Win32Raw("Replace Me With Your Printer Name")                                         # Enter your printer name in ()
date_time = datetime.datetime.now()

# Print ticket lines entered by user with date and time centered at the top of the receipt
printer.text("^^^^^^^^^^****************************^^^^^^^^^^")
printer.text((date_time.strftime("%B %d, %Y  |  %H%M LOCAL").center(48)))                       # Print a line: centered date and time
printer.text("\n\n")   

# User enters lines until typing 'done'
line_to_print = ''
while line_to_print != "done":                                                                  
    line_to_print = input("Enter a line then hit enter to write or type 'done' to stop: ")      # User entries into the receipt
    if line_to_print.lower() == "done" :                                                        # line_to_print.lower() adds redundancy for all iterations of the word 'done'
        break                                                                                   # Exit loop, print and cut when sentinal value is detected
    else :
        printer.text((line_to_print).center(48))                                                # Prints text centered. Removing () from line_to_print causes spacing issue
        printer.text("\n")                                                                      # Placing \n with the centered print command above causes spacing issue
        continue                                                                

printer.text("\n")
printer.text("^^^^^^^^^^****************************^^^^^^^^^^")

printer.cut()
